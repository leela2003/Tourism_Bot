# 🇮🇳 Indian States Tourism Telegram Bot

This project is a **Telegram chatbot** built with Python that provides **top tourism destinations** for any Indian state.  
It uses a dataset (`indian_states_tourism_places.csv`) containing all Indian states and their famous tourist attractions.

---

## 🌟 Features

- 📍 Get top tourist destinations by typing an Indian state name  
- 💬 Interactive Telegram chatbot using `python-telegram-bot`  
- 🧾 External dataset stored in a CSV file  
- 🧠 Handles user input dynamically (case insensitive)  
- ⚡ Simple, fast, and works perfectly in VS Code  

---

## 🖼️ Project Screenshots

Here’s a glimpse of how the bot works in Telegram 👇

### 🗨️ Example Chat 1
![Tourism Bot Chat 1](./58991db4-76b1-4498-aa4c-a4c8c216946d.png)

### 🗨️ Example Chat 2
![Tourism Bot Chat 2](./848032e3-6217-4d58-a5c0-645ff1b9f453.png)

---

## 🗂️ Folder Structure

```
tourism_bot_project/
│
├── bot.py                           # Main Python script
├── indian_states_tourism_places.csv # Dataset file
├── README.md                        # Documentation
├── requirements.txt                 # Python dependencies
├── Example1.png  # Screenshot 1
└── Example2.png  # Screenshot 2
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/tourism-bot.git
cd tourism-bot
```

### 2️⃣ Install Required Libraries
```bash
pip install python-telegram-bot==13.15 pandas urllib3==1.26.15
```

### 3️⃣ Create a Telegram Bot
1. Open [@BotFather](https://t.me/BotFather) on Telegram  
2. Send `/newbot`  
3. Give it a name and username  
4. Copy your **bot token**

### 4️⃣ Add Your Token to `bot.py`
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

### 5️⃣ Run the Bot
```bash
python bot.py
```

You’ll see:
```
✅ Dataset loaded successfully!
🤖 Bot is running... Press Ctrl+C to stop.
```

---

## 🧠 Example Interaction

**User:** `/start`  
**Bot:** 👋 Welcome to the Incredible India Tourism Bot 🇮🇳  
**User:** `Kerala`  
**Bot:** 🌍 *Top Tourism Places in Kerala:*  
Kochi, Munnar, Alleppey, Kovalam  

---

## 💡 Future Enhancements
- 📸 Add images for each state  
- 🌐 Deploy bot on Render or AWS  
- 🔍 Add nearby attractions using Google Maps API  
- 🧭 Add chatbot UI using Streamlit  

---

## 👩‍💻 Author

**Leelavathi Somisetti**  
🎓 B.E. Artificial Intelligence & Machine Learning (2021–2025)  
📧 [leelavathisomisetti79@gmail.com](mailto:leelavathisomisetti79@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/leelavathi-somisetti)

---

## 📜 License
Licensed under the **MIT License** — feel free to use, modify, and share.
