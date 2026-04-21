# Venture-Capitalist-Startup-Analyzer
An AI-powered tool that analyzes startup websites and generates structured, VC-style business insights using a local language model.

🧠 Overview

VC Startup Analyzer is an AI-powered tool that:

1. Takes a startup website URL
2. Extracts meaningful content
3. Uses a local LLM (via Ollama)
4. Generates structured VC-style insights

✨ Features
1. 🔗 URL → Instant analysis
2. 🧠 AI-powered business understanding
3. 📊 Structured JSON output
4. ⚡ Runs locally (no API cost)
5. 🔒 Privacy-friendly

📸 Demo
1. 🔹 Input - python vc_summary.py https://www.linear.app/
2. 🔹 Output
{
  "one_liner": "AI-powered project management tool for modern teams",
  "problem": "Teams struggle with slow and inefficient workflows",
  "solution": "Provides fast, streamlined issue tracking and collaboration",
  "target_customers": "Product and engineering teams",
  "business_model": "SaaS subscription",
  "moat": "Speed, UX, and developer-first design"
}

🏗️ Architecture
User
  ↓
Streamlit UI (optional)
  ↓
Python Backend
  ↓
Web Scraper (requests + BeautifulSoup)
  ↓
Ollama (Local LLM)
  ↓
Structured VC Summary (JSON)

⚙️ Tech Stack
1. 🐍 Python
2. 🌐 Requests
3. 🧹 BeautifulSoup
4. 🧠 Ollama (LLM runtime)
5. 🎨 Streamlit (optional UI)

📁 Project Structure
.
├── vc_summary.py        # Main backend script
├── app.py               # Streamlit UI (optional)
├── venv/                # Virtual environment
└── README.md

🛠️ Setup
1. Clone the repo - git clone <your-repo-url>
cd <project-folder>
2. Create virtual environment
   2.1. python3 -m venv venv
   2.2. source venv/bin/activate
3. Install dependencies - pip install requests beautifulsoup4 lxml
4. Install Ollama - 👉 https://ollama.com/
5. Pull model - ollama run phi3
6. Start Ollama server - ollama serve

▶️ Usage
Run CLI version - python vc_summary.py <url>

Example:

1. python vc_summary.py https://www.perplexity.ai/
2. Run Web App (optional)
3. pip install streamlit
4. streamlit run app.py

⚠️ Limitations
1. ❌ JS-heavy sites (e.g., LinkedIn, LeetCode)
2. ❌ Login-required pages
3. ⚠️ Output quality depends on model (phi3 vs llama3)
4. 🚀 Future Improvements
5. 📊 Investment scoring
6. 🧠 Better prompt engineering
7. 🌐 Support dynamic websites (Selenium/Playwright)
8. 📈 Competitor analysis
9. 🎨 Enhanced UI dashboard
10. 💡 How It Works - URL → HTML → Clean Text → LLM → VC Insights

⭐ If you like this project

Give it a star ⭐ — helps a lot!
