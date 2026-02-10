# 🗼 Paris Tourist Chatbot using OpenAI API

## 📌 Project Title
**Paris Tourist Chatbot (Peterman Reality Tours Guide)**

---

## 📖 Project Description
The **Paris Tourist Chatbot** is a Python-based chatbot application powered by the **OpenAI Chat Completions API**.  
It simulates an **expert Parisian travel guide** representing *Peterman Reality Tours* and responds to common tourist-related questions about Paris landmarks and culture.

This project was built to demonstrate:
- How to structure chatbot conversations using OpenAI’s **role-based messaging system**
- How to maintain conversation context using a **conversation list**
- How to generate consistent outputs using `temperature=0.0`
- How to control response size using `max_tokens=100`

The chatbot is designed to answer predefined tourist questions such as:
- Driving distance between famous landmarks
- Location-based tourist queries
- Must-see artworks in museums

**Target Audience:**  
This project is intended for students, beginner AI developers, and engineers learning how to integrate the OpenAI API into Python applications.

---

## 🎯 Problem Statement
Tourists often need quick, reliable, and easy-to-understand information about Parisian landmarks and cultural attractions.  
This chatbot solves the problem by offering short, accurate responses in a friendly professional tone.

---

## 🛠️ Features
- Role-based conversation format (`system`, `user`, `assistant`)
- Multiple question handling using a loop
- Conversation history tracking using a Python list of dictionaries
- Deterministic responses with `temperature=0.0`
- Response token control using `max_tokens=100`

---

## 📂 Project Structure
```
DataCamp-Projects/Associate AI Engineer for Developers/Planning a Trip to Paris with the OpenAI API/
│
├── chatbot.py          # Main script that calls the OpenAI API
├── README.md           # Project documentation
└── requirements.txt    # Dependencies list 
```

---

## 📑 Table of Contents
- [Project Title](#-project-title)
- [Project Description](#-project-description)
- [Problem Statement](#-problem-statement)
- [Features](#️-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [How It Works](#-how-it-works)
- [Configuration](#-configuration)
- [Technologies Used](#-technologies-used)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## ✅ Prerequisites
Before running this project, make sure you have:

- **Python 3.8+**
- **pip** (Python package installer)
- An **OpenAI API Key**
- Basic understanding of Python and APIs

---

## 📥 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/vijay1379/DataCamp-Projects.git
cd "DataCamp-Projects/Associate AI Engineer for Developers/Planning a Trip to Paris with the OpenAI API"
```

### 2️⃣ Create a Virtual Environment (Recommended)

#### For macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
Install the OpenAI library:

```bash
pip install -r requirements.txt
```

---

## 🔑 Set Up OpenAI API Key

You must store your OpenAI API key as an environment variable.

### macOS / Linux:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Windows (PowerShell):
```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

Restart the terminal after setting the key.

---

## ▶️ Usage

### Run the Program
Execute the chatbot script:

```bash
python chatbot.py
```

---

## 🧾 Code Implementation

The chatbot uses a **conversation list** which stores all messages in the following format:

```python
conversation = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]
```



## 🖥️ Sample Output

Example output from running the script:

```
User: How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?
Response: The Louvre Museum is approximately 3 miles away from the Eiffel Tower by car, depending on traffic.

User: Where is the Arc de Triomphe?
Response: The Arc de Triomphe is located at Place Charles de Gaulle, at the western end of the Champs-Élysées in Paris.

User: What are the must-see artworks at the Louvre Museum?
Response: Must-see artworks include the Mona Lisa by Leonardo da Vinci, the Venus de Milo, and the Winged Victory of Samothrace.
```

---

## ⚙️ How It Works

### Step-by-Step Process
1. The program starts with a **system message** defining the chatbot personality.
2. A list of tourist questions is stored in `questions`.
3. Each question is appended into the `conversation` list as a `user` message.
4. The conversation is sent to the OpenAI API using:
   - `temperature=0.0` for consistent responses
   - `max_tokens=100` to keep answers concise
5. The assistant's response is appended back into the conversation list.
6. The chatbot prints responses sequentially.

---

## 🔧 Configuration

You can modify chatbot behavior by adjusting these values:

### Model Selection
```python
model = "gpt-4o-mini"
```

### Temperature (Creativity Control)
```python
temperature = 0.0
```
- `0.0` = deterministic, factual, consistent
- `0.7+` = more creative, varied answers

### Max Tokens (Response Length Control)
```python
max_tokens = 100
```
- Smaller value = shorter responses  
- Higher value = longer, more detailed answers  

---

## 🧰 Technologies Used
- **Python 3**
- **OpenAI Python SDK**
- **GPT-4o-mini model**
- Environment Variables for API key handling

---

## 🚀 Future Enhancements
Possible improvements for future versions:
- Add real-time tourist data integration (maps / directions API)
- Add a GUI or web interface (Flask / Streamlit)
- Allow free-form user input instead of fixed questions
- Add error handling for API failures
- Add logging and conversation export to JSON

---

## 📜 License
This project is for educational purposes.  
You may use and modify it freely.

---

## 👤 Author
**Your Name**  
📧 Email: vijaykumar98863@gmail.com
🌍 GitHub: https://github.com/vijay1379

---
