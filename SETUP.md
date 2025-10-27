# 📸 Smile Capture Booth — Project Setup & Tweaking Guide

Welcome to the **Smile Capture Booth Setup Guide!**  
This document will help you run the project locally, tweak variables, and understand how everything fits together — step by step with visuals.

---

## ⚙️ Project Overview

This project detects smiles using **OpenCV (Python)** and captures photos automatically.  
It’s built with **Flask (backend)** and **HTML/CSS/JS (frontend)**.

---

## 🧰 Prerequisites

Make sure you have:

- Python 3.9+
- pip (Python package manager)
- A webcam
- Git installed

---

## 🚀 Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Smile.git
cd Smile

##🧩 Step 2 — Create Virtual Environment
```bash
python -m venv venv
# Activate the environment
# For Windows:
```bash
venv\Scripts\activate
# For Mac/Linux:
```bash
source venv/bin/activate
###📦 Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
##▶️ Step 4 — Run the Application
```bash
python app.py

###🧠 Step 5 — Tweak the Variables
Open app.py and locate this section:
```bash
# Configuration
SMILE_THRESHOLD = 1.3         # Adjust smile detection sensitivity
MAX_IMAGES = 3                # How many photos per session
IMAGE_SAVE_PATH = "static/images"   # Where captures are saved
You can modify:

SMILE_THRESHOLD: Lower = easier smile detection; higher = stricter.

MAX_IMAGES: Number of images captured before stopping.

IMAGE_SAVE_PATH: Directory where images are stored.

##🖼️ Step 6 — Visual Guide (with Screenshots)
1️⃣ Home Screen (Camera Ready)

Displays the live webcam feed with “Start Capture” button.


2️⃣ Smile Detection

When you smile, the app captures images automatically.


3️⃣ Gallery View

After capturing, go to the Gallery page to view all images.


(You can replace these with your own screenshots later.)

##🎨 Step 7 — Theme & Background Customization

You can add your own background images in:
```bash
/static/images/

##🧹 Step 8 — Clear Old Captures (Optional)

You can manually delete old photos:

del static\images\*        # Windows
rm static/images/*         # mac/linux

##⚙️ Step 9 — Folder Structure
Smile/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── gallery.html
├── static/
│   ├── images/
│   └── docs/       ← Screenshots folder
└── docs/
    └── SETUP.md

##💡 Step 10 — Troubleshooting
Issue	Solution
Camera not working	Allow browser permission
Smile not detected	Lower SMILE_THRESHOLD
Images not saving	Check static/images path
Flask error	Make sure app.py is running
##🧠 Step 11 — Deployment Tips

For production:

pip install gunicorn
gunicorn app:app


You can also deploy using Render, Heroku, or Vercel (Flask adapter).

✅ You’re now ready to run, tweak, and customize your own Smile Capture Booth.
📸 Capture your smiles, explore UI themes, and contribute enhancements!

Made with ❤️ and a lot of smiles 😄
