AI CRM - Interaction Logger :

1 : Overview 
This project is an AI-powered CRM system that converts unstructured user interaction text into structured CRM data.

2 : Features 
- Extracts HCP Name
- Generates interaction summary
- Detects sentiment
- Suggests follow-up actions

3 : Tech Stack 
- Backend: FastAPI
- Frontend: React
- AI Model: Groq API
- Environment: Python, Node.js

4 :Project Structure
backend/
main.py
agent.py
frontend/
src/

** Setup Instructions:-

1 : Backend 
bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload

2 : Frontend 
bash
cd frontend
npm install
npm start

3 : Environment Variables 
Create .env file inside backend:
GROQ_API_KEY=your_api_key_here

4 : API Endpoint
POST/chat

Request :
JSON
{
  "text": "Met Dr. Sharma. He liked Product X but asked for pricing."
}

Response : 
JSON
{
  "HCP Name": "Dr. Sharma",
  "Summary": "...",
  "Sentiment": "Positive",
  "Follow-up": "Send pricing details"
}

OUTCOMES : 
Transforms raw interaction text into structured CRM-ready insights.


