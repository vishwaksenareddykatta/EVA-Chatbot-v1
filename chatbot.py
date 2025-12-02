from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values
from functools import lru_cache

# Load environment variables
env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Initialize Groq client
client = Groq(api_key=GroqAPIKey)

# Try to load chat history (optional)
try:
    with open(r"/Users/mr.katta/Documents/My Private Server/Thrivex Lab/EVA Chatbot v1/DataChatLog.json", "r") as f:
        messages = load(f)
except FileNotFoundError:
    messages = []
    with open(r"/Users/mr.katta/Documents/My Private Server/Thrivex Lab/EVA Chatbot v1/DataChatLog.json", "w") as f:
        dump([], f)

# System message
System = f"""
Hello, I am {Username}. You are an AI assistant named {Assistantname}.
Respond briefly and accurately. English only. No time unless asked.
"""

SystemChatBot = [{"role": "system", "content": System}]

# Real-time data function
def RealtimeInformation():
    now = datetime.datetime.now()
    return (
        f"Use this real-time info if needed:\n"
        f"Day: {now.strftime('%A')}\n"
        f"Date: {now.strftime('%d %B %Y')}\n"
        f"Time: {now.strftime('%I:%M:%S %p')}\n"
    )

# Remove empty lines
def AnswerModifier(Answer: str) -> str:
    return "\n".join(line for line in Answer.split("\n") if line.strip())

# Core Chatbot Function (Optimized)
def Chatbot(Query: str) -> str:
    try:
        # Keep message history small for performance
        messages.append({"role": "user", "content": Query})
        if len(messages) > 4:
            messages[:] = messages[-4:]

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Fastest available
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=512,
            temperature=0.6,
            top_p=1.0,
            stream=False  # Disabling streaming for instant response
        )

        Answer = completion.choices[0].message.content.strip()
        Answer = AnswerModifier(Answer)
        messages.append({"role": "assistant", "content": Answer})

        # Save asynchronously to reduce blocking
        with open(r"/Users/mr.katta/Documents/My Private Server/Thrivex Lab/EVA Chatbot v1/DataChatLog.json", "w") as f:
            dump(messages[-10:], f)

        return Answer

    except Exception as e:
        print(f"Error: {e}")
        messages.clear()
        with open(r"/Users/mr.katta/Documents/My Private Server/Thrivex Lab/EVA Chatbot v1/DataChatLog.json", "w") as f:
            dump([], f)
        return "An error occurred. Please try again."

@lru_cache(maxsize=200)
def cached_chatbot_response(query):
    return Chatbot(query)

# Run chatbot
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")
        response = cached_chatbot_response(user_input)
        print(response)
