# --- Standard library imports ---
import base64        # For encoding/decoding binary data (e.g., images)
import os            # For interacting with the operating system (paths, files, etc.)
import random        # For generating random values (e.g., filenames, IDs)
import zipfile       # For creating and extracting ZIP files
from io import BytesIO  # For handling in-memory byte streams (e.g., sending files via Flask)

# --- Third-party library imports ---
import cv2           # OpenCV for image processing and computer vision tasks
import numpy as np    # NumPy for numerical operations and array manipulations
from flask import Flask, jsonify, render_template, request, send_file  # Flask web framework components


# If you use CNN
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

app = Flask(__name__)

# --- CONFIGURATION ---
DETECTOR_TYPE = 'CNN'  # 'CNN' or 'HAAR'

total_images = 3
consecutive_smile_frames = 3  # Frames of smile required
current_smile_streak = 0
images_captured = 0
folder_code = None
folder_path = None

# --- FACE/SMILE DETECTION ---
faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")

if DETECTOR_TYPE == 'HAAR':
    smileCascade = cv2.CascadeClassifier("dataset/haarcascade_smile.xml")
elif DETECTOR_TYPE == 'CNN':
    model = load_model("cnnModel/training/output/smile_model.h5")
    labels = ['not_smiling', 'smiling']

# --- UTILS ---
def generate_new_folder():
    folder_code = str(random.randint(100000, 999999))
    folder_path = os.path.join("static/images", folder_code)
    os.makedirs(folder_path, exist_ok=True)
    return folder_code, folder_path

# --- ROUTES ---
@app.route('/')
def index():
    global folder_code, folder_path, images_captured, current_smile_streak
    folder_code, folder_path = generate_new_folder()
    images_captured = 0
    current_smile_streak = 0
    return render_template('index.html', folder_code=folder_code)

@app.route('/process_frame', methods=['POST'])
def process_frame():
    global images_captured, current_smile_streak, folder_path

    if images_captured >= total_images:
        return jsonify({
            'images_captured': images_captured,
            'smile_detected': False,
            'alert': False,
            'message': 'Session complete! All images captured.',
            'smile_streak': current_smile_streak,
            'required_streak': consecutive_smile_frames
        })

    data = request.get_json()
    img_data = data['image'].split(',')[1]
    img_bytes = base64.b64decode(img_data)
    npimg = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        return jsonify({
            'images_captured': images_captured,
            'smile_detected': False,
            'alert': False,
            'message': 'Invalid frame received.',
            'smile_streak': current_smile_streak,
            'required_streak': consecutive_smile_frames
        })

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    smile_detected_in_frame = False
    message = "Looking for faces..."

    if len(faces) == 0:
        message = "No face detected."
        current_smile_streak = 0
    else:
        message = "Face detected, analyzing smile..."
        for (x, y, w, h) in faces:
            roi_gray = gray[y + h//2: y + h, x: x + w]  # lower half
            if roi_gray.size == 0:
                continue

            if DETECTOR_TYPE == 'HAAR':
                smiles = smileCascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=20, minSize=(25, 15))
                if len(smiles) > 0:
                    smile_detected_in_frame = True
                    break
            elif DETECTOR_TYPE == 'CNN':
                roi_resized = cv2.resize(roi_gray, (28, 28)).astype("float") / 255.0
                roi_resized = img_to_array(roi_resized)
                roi_resized = np.expand_dims(roi_resized, axis=0)
                preds = model.predict(roi_resized)
                label_idx = preds.argmax(axis=1)[0]
                label = labels[label_idx]
                if label == 'smiling':
                    smile_detected_in_frame = True
                    break

    # Update smile streak
    if smile_detected_in_frame:
        current_smile_streak += 1
        message = f"Smile detected! ({current_smile_streak}/{consecutive_smile_frames})"
    else:
        current_smile_streak = 0
        if len(faces) > 0:
            message = "Face detected, please smile!"

    alert_triggered = False
    if current_smile_streak >= consecutive_smile_frames:
        os.makedirs(folder_path, exist_ok=True)
        img_path = os.path.join(folder_path, f"image_{images_captured+1}.jpg")
        cv2.imwrite(img_path, img)
        images_captured += 1
        current_smile_streak = 0
        alert_triggered = True
        message = f"Perfect smile captured! ({images_captured}/{total_images})"

    return jsonify({
        'images_captured': images_captured,
        'smile_detected': smile_detected_in_frame,
        'alert': alert_triggered,
        'message': message,
        'smile_streak': current_smile_streak,
        'required_streak': consecutive_smile_frames
    })

@app.route('/get_images')
def get_images():
    if folder_code is None or not os.path.exists(folder_path):
        return jsonify({"images": []})

    images = [f"{folder_code}/{img}" for img in sorted(os.listdir(folder_path)) if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return jsonify({"images": images})

@app.route('/download_images')
def download_images():
    try:
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zipf:
            for i in range(images_captured):
                img_filename = f"image_{i+1}.jpg"
                img_path = os.path.join(folder_path, img_filename)
                if os.path.exists(img_path):
                    zipf.write(img_path, arcname=img_filename)
        zip_buffer.seek(0)
        return send_file(zip_buffer, mimetype='application/zip', as_attachment=True, download_name=f"{folder_code}_images.zip")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/gallery')
def gallery():
    gallery_data = []
    images_root = os.path.join('static/images')
    if os.path.exists(images_root):
        for folder_code_entry in os.listdir(images_root):
            folder_path_entry = os.path.join(images_root, folder_code_entry)
            if os.path.isdir(folder_path_entry):
                images = [f"/static/images/{folder_code_entry}/{img}" for img in sorted(os.listdir(folder_path_entry)) if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
                if images:
                    gallery_data.append({'id': folder_code_entry, 'images': images})
    gallery_data.sort(key=lambda x: x['id'], reverse=True)
    return render_template('gallery.html', gallery=gallery_data)

@app.route('/edit_image', methods=['POST'])
def edit_image():
    data = request.get_json()
    session_id = data['session_id']
    image_path = data['image_path']
    image_data = data['image_data']
    filename = os.path.basename(image_path)
    folder_path = os.path.join('static/images', session_id)
    if not os.path.exists(folder_path):
        return jsonify({'success': False, 'error': 'Session not found'})

    img_bytes = base64.b64decode(image_data.split(',')[1])
    img_file_path = os.path.join(folder_path, filename)
    with open(img_file_path, 'wb') as f:
        f.write(img_bytes)
    return jsonify({'success': True})

if __name__ == '__main__':
    os.makedirs("static/images", exist_ok=True)
    app.run(debug=True, host="0.0.0.0", port=5000)
