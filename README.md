# 🚀 EVA Chatbot v1 — Lightweight, Fast & Intelligent Python AI Assistant

EVA Chatbot v1 is a fully local, real-time conversational assistant powered by Groq’s ultra-fast LLaMA-3.1-8B-Instant model.
It is designed for speed, accuracy, minimal memory usage, and persistent chat history, making it perfect for personal AI terminals, CLI assistants, automation projects, or lightweight server-side bots.


## ✨ Key Features
### 🔹 ⚡ Ultra-Fast Groq Inference
Runs on llama-3.1-8b-instant, giving near-instant responses with low latency.

### 🔹 🧠 Smart Conversation Memory
Stores chat history in a JSON file and automatically trims messages to keep performance high.

### 🔹 📅 Real-Time Awareness
Injects current day, date, and time into the system prompt for smarter, context-aware replies.

### 🔹 🔍 Optimized Response Engine

Includes:
Automatic empty-line cleanup
Temperature & top-p tuned for balanced creativity
Lightweight LRU caching (@lru_cache) for repeated queries

### 🔹 🔐 Env-Based Configuration

Your:

Username
Assistant name
Groq API key

…are safely loaded from a .env file.

### 🔹 💾 Automatic Log Persistence
Chat messages (up to last 10) are saved locally without slowing down responses.

### 🔹 💬 Command-Line Interface
Run the chatbot directly in the terminal — simple, clean, always ready.


## 🗂️ File Overview
chatbot.py — Core logic, API calls, chat memory, CLI loop
DataChatLog.json — Auto-generated conversation memory
.env — Stores environment variables (Username, Assistantname, GroqAPIKey)


## 🛠️ Tech Stack
Python 3
Groq API
LLaMA-3.1-8B-Instant
dotenv
LRU Cache
JSON for persistent logs

