![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

# 🤖 Mini AI

A lightweight AI-inspired learning assistant built with Python.  
This project can search Wikipedia, learn about a topic, summarize information, and store knowledge locally using memory.


---

## ✨ Features

- 🌐 Learns topics directly from Wikipedia
- 🧠 Local memory system using JSON
- ⚡ Fast topic retrieval from saved memory
- 📚 Automatic text summarization
- 💾 Saves learned knowledge for future use
- 🖥️ Simple terminal-based interface

---

## 🚀 How It Works

1. User enters a topic  
2. The agent searches Wikipedia  
3. Extracts useful information  
4. Generates a summary  
5. Stores the result in memory  
6. Reuses saved knowledge later

---

## 📸 Example

```bash
🤖 Mini AI
====================

🧠 What should I learn?
> python

🌐 Learning...

📚 Learned Summary:

Python is a high-level programming language...

🧠 Memory System

The AI stores learned topics inside:

memory.json

Example:
{
    "python": "Python is a programming language..."
}

When the same topic is requested again:
🧠 Found in memory!

No additional web request is needed.

🛠️ Tech Stack

* Python 3
* requests
* BeautifulSoup4
* JSON storage

📦 Installation

1️⃣ Clone repository

git clone https://github.com/samanmokhtari/miniAi.git

2️⃣ Open project

cd miniAi

3️⃣ Install dependencies

pip3 install -r requirements.txt

▶️ Run Project

python3 main.py

📁 Project Structure
miniAi/
│
├── main.py
├── learner.py
├── memory.json
├── requirements.txt
└── README.md

📚 Example Topics

Try learning:

* Python
* Docker
* Linux
* Artificial Intelligence
* Machine Learning
* Cybersecurity


⚠️ Notes

* Requires internet connection
* Requires proxy in iran
* Wikipedia availability may vary
* Some topics may not exist

🔮 Future Improvements

* 🤖 OpenAI integration
* 🌐 Multi-source learning
* 💬 Chat mode
* 📄 Markdown note generation
* 🧠 Smarter memory system
* 🎙️ Voice input support

💡 Why This Project?

This project demonstrates:

* API requests
* Web scraping concepts
* Local AI memory systems
* Data persistence
* CLI application architecture

Perfect for beginner-to-intermediate Python portfolios.

📜 License

MIT License — free to use and modify.

⭐ Support

If you like this project, give it a ⭐ on GitHub!
