
# 📸 Smile Capture Booth — Project Setup & Tweaking Guide

Welcome to the **Smile Capture Booth Setup Guide!**  
This document helps you set up the project locally, tweak configurations, and understand how everything fits together — step by step with visuals.

---

## ⚙️ Project Overview

The **Smile Capture Booth** detects smiles using **OpenCV (Python)** and captures photos automatically.  
It’s built with **Flask (backend)** and **HTML/CSS/JS (frontend)** for a smooth interactive experience.

---

## 🧰 Prerequisites

Before starting, make sure you have:

- **Python 3.9+**
- **pip** (Python package manager)
- **A working webcam**
- **Git** installed

---

<details>
<summary>🚀 <b>Step 1 — Clone the Repository</b></summary>

```bash
git clone https://github.com/YOUR-USERNAME/Smile.git
cd Smile
````

</details>

---

<details>
<summary>🧩 <b>Step 2 — Create a Virtual Environment</b></summary>

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

</details>

---

<details>
<summary>📦 <b>Step 3 — Install Dependencies</b></summary>

```bash
pip install -r requirements.txt
```

</details>

---

<details>
<summary>▶️ <b>Step 4 — Run the Application</b></summary>

```bash
python app.py
```

Now open your browser and visit:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

</details>

---

<details>
<summary>🧠 <b>Step 5 — Tweak the Variables</b></summary>

Open **`app.py`** and locate this section:

```python
# Configuration
SMILE_THRESHOLD = 1.3              # Adjust smile detection sensitivity
MAX_IMAGES = 3                     # Number of photos per session
IMAGE_SAVE_PATH = "static/images"  # Folder to save captures
```

You can modify:

* **`SMILE_THRESHOLD`** → Lower = easier smile detection; higher = stricter
* **`MAX_IMAGES`** → Number of images captured before stopping
* **`IMAGE_SAVE_PATH`** → Directory where images are stored

</details>

---

<details>
<summary>🖼️ <b>Step 6 — Visual Guide (with Screenshots)</b></summary>

**1️⃣ Home Screen (Camera Ready)**
Displays the live webcam feed with the “Start Capture” button.

**2️⃣ Smile Detection**
When you smile, the app automatically captures images.

**3️⃣ Gallery View**
After capturing, go to the Gallery page to view all images.

*(You can replace these with your own screenshots later.)*

</details>

---

<details>
<summary>🎨 <b>Step 7 — Theme & Background Customization</b></summary>

Add or replace your background images in:

```
/static/images/
```

</details>

---

<details>
<summary>🧹 <b>Step 8 — Clear Old Captures (Optional)</b></summary>

You can manually delete old photos.

**Windows:**

```bash
del static\images\*
```

**Mac/Linux:**

```bash
rm static/images/*
```

</details>

---

<details>
<summary>⚙️ <b>Step 9 — Folder Structure</b></summary>

```
Smile/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── gallery.html
├── static/
│   ├── images/
│   └── docs/         ← Screenshots folder
└── docs/
    └── SETUP.md
```

</details>

---

<details>
<summary>💡 <b>Step 10 — Troubleshooting</b></summary>

| Issue              | Solution                            |
| ------------------ | ----------------------------------- |
| Camera not working | Allow camera permission in browser  |
| Smile not detected | Lower the `SMILE_THRESHOLD` value   |
| Images not saving  | Check the `static/images` path      |
| Flask error        | Ensure `app.py` is running properly |

</details>

---

<details>
<summary>🌍 <b>Step 11 — Deployment Tips</b></summary>

For production deployment, install **Gunicorn**:

```bash
pip install gunicorn
gunicorn app:app
```

You can also deploy using:

* **Render**
* **Heroku**
* **Vercel (Flask adapter)**

</details>

---

✅ You’re now ready to **run, tweak, and customize** your own Smile Capture Booth!
📸 Capture your smiles, explore new UI themes, and contribute enhancements.

Made with ❤️ and a lot of smiles 😄

```
