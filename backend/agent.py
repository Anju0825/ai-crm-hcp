from groq import Groq
from tools import *
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_agent(user_input):
    try:
        print("User Input:", user_input)

        # 🔥 Tool Routing Logic (LangGraph style)
        if "edit" in user_input.lower():
            return edit_interaction_tool(user_input)

        elif "history" in user_input.lower():
            return get_history_tool()

        elif "follow" in user_input.lower():
            return suggest_followup_tool()

        # 🔥 Default → AI Processing
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Extract structured CRM data:

{user_input}

Return:
- HCP Name
- Summary
- Sentiment
- Follow-up
"""
                }
            ]
        )

        ai_output = response.choices[0].message.content

        return log_interaction_tool(ai_output)

    except Exception as e:
        return {"error": str(e)}