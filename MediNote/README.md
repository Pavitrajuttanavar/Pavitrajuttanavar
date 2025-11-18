# ⭐ MediNote – Voice-Based Medicine Reminder

MediNote is a simple and effective **medicine reminder system** that alerts users with **sound + voice notifications**.
It helps elderly people, busy students, and patients remember their medicines on time.

---

## 🚀 Features
- 🔔 Automatic medicine reminders (sound + voice)
- 🗣️ Voice alert: “Time to take your medicine”
- ⏰ Add reminders with medicine name + time
- 💾 Save notes using a Flask backend
- 🟢 Works in any browser (Chrome recommended)
- 🎧 No installation needed except Python for backend

---

## 🖥️ How It Works
1. Start the backend server (`python app.py`)
2. Open `index.html` in browser (Live Server recommended)
3. Add a medicine + time
4. At the exact reminder time, the system:
   - Plays a sound
   - Speaks the reminder using SpeechSynthesis API

---

## 📦 Project Structure
```
MediNote/
│── index.html    → Frontend (UI + reminder logic + voice)
│── app.py        → Backend (Flask API to save notes)
│── screenshots/  → Demo images (optional)
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Install Flask
```sh
pip install flask
```

### 2️⃣ Run the backend
```sh
python app.py
```
Backend runs at:
```
http://127.0.0.1:5000
```

### 3️⃣ Open the frontend
**Option A — Recommended**  
Use Live Server in VS Code:  
Right-click `index.html` → **Open with Live Server**

**Option B**  
Double-click `index.html` to open in browser  
(Note: Save button may not work without Live Server)

---

## 🔊 Demo Output
At reminder time:
- A beep sound plays  
- System speaks:  
  **“Time to take your medicine: <medicine-name>”**  
- Reminder highlights in red  

---

 

## 📚 Future Improvements
- WhatsApp / SMS reminders  
- Mobile app (Flutter)  
- Cloud database  
- Multiple reminders per medicine  

---

## 👩‍💻 Author / Team
**Laxmi Jalikatti** 
**Pavitra J**
**Dikshita M**
**Ramya M**
Hackathon Project – MediNote (2025)

---
