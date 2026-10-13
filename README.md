# ai-knowledge-assistant
AI Knowledge Assistant
A beginner-friendly Python AI project.

The purpose of this project is to learn:

Variables
Functions
Classes
Objects
Lists
Dictionaries
File Handling
JSON
Error Handling
GitHub Repository Structure
before moving to:

OpenAI APIs
Azure OpenAI
Vector Databases
Embeddings
RAG
LangChain
LangGraph
Repository Structure
ai-knowledge-assistant/
│
├── data/
│   └── knowledge_base.txt
│
├── output/
│   └── chat_history.json
│
├── src/
│   ├── chatbot.py
│   ├── file_handler.py
│   ├── knowledge_search.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
How The Application Works
User
 ↓
Ask Question
 ↓
main.py
 ↓
Chatbot Class
 ↓
Read Knowledge Base
 ↓
Search Information
 ↓
Return Answer
 ↓
Save To JSON
File Responsibilities
knowledge_base.txt
Contains information that the chatbot uses to answer questions.

Example:

Azure is Microsoft's cloud computing platform.
file_handler.py
Responsible for:

Opening files
Reading files
Returning file content
knowledge_search.py
Responsible for:

Searching information
Finding matching text
Returning results
chatbot.py
Responsible for:

Creating chatbot object
Greeting users
Returning answers
main.py
Responsible for:

Running application
Reading knowledge
Asking questions
Saving results
Python Concepts Used
Variables
Store data.

Example:

question = "What is Azure?"
Functions
Perform actions.

Example:

read_knowledge_file()
Classes
Blueprints.

Example:

class Chatbot
Objects
Created from classes.

Example:

bot = Chatbot()
Dictionaries
Store key-value pairs.

Example:

{
  "question": "Azure",
  "answer": "Microsoft Cloud"
}
File Handling
Used to read and save files.

JSON
Used to save conversations.

Error Handling
Prevents crashes.

Example:

try:
    ...
except:
    ...
Running The Project
Create Virtual Environment
python -m venv venv
Activate Environment
Windows

venv\Scripts\activate
Mac/Linux

source venv/bin/activate
Run Application
Move into source folder:

cd src
Run:

python main.py
Example Run
Output:

Hello, I am AI Assistant

Ask a question:
Azure

Answer:
Azure is Microsoft's cloud computing platform.

Conversation saved successfully.
Generated Output
chat_history.json

{
    "question": "Azure",
    "answer": "Azure is Microsoft's cloud computing platform."
}
What You Learned
This project demonstrates:

✅ Variables

✅ Functions

✅ Classes

✅ Objects

✅ File Handling

✅ Dictionaries

✅ JSON

✅ Error Handling

✅ Repository Structure

✅ Git Fundamentals
