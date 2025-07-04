# EduChain MCP Integration Server

This project implements an **MCP-compatible Flask server** that integrates with the [`educhain`](https://github.com/satvik314/educhain) Python library to dynamically generate educational content for Claude Desktop.

It provides three core educational tools:

- 🧠 Multiple-Choice Questions (MCQs)
- 📘 Lesson Plans
- 🃏 Flashcards (Bonus)

---

## 🚀 Features

- 📡 Exposes REST API endpoints for Claude Desktop integration
- 🔐 Uses `.env` file to securely manage OpenAI API keys
- 📦 Lightweight and easy to deploy
- 🧪 Includes sample responses and test script

---

## 🛠️ Technologies Used

- Python 3.10+
- Flask
- EduChain (via `educhain` package)
- dotenv (`python-dotenv` for secure API handling)
- Claude Desktop MCP Protocol (local JSON config)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abanindra3/educhain-mcp.git
cd educhain-mcp
2. Create and Activate Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
pip install flask python-dotenv
4. Create .env File
Create a .env file in the root directory and add your OpenAI API key:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
5. Run the Server
bash
Copy
Edit
python mcp_server.py
Server will run at:
📍 http://localhost:5000

6. Test the Endpoints
You can run:

bash
Copy
Edit
python test_server.py
Or test manually using Postman/Hoppscotch with these POST endpoints:

Endpoint	Purpose	Sample Payload
/generate_mcqs	Generate MCQs	{ "topic": "Python loops", "count": 5 }
/generate_lesson_plan	Create a lesson plan	{ "subject": "Algebra" }
/generate_flashcards	Generate flashcards (bonus)	{ "topic": "OOP in Java", "count": 6 }
