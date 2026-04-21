# Venture-Capitalist-Startup-Analyzer
An AI-powered tool that analyzes startup websites and generates structured, VC-style business insights using a local language model.

🧠 Overview

VC Startup Analyzer is an AI-powered tool that:

Takes a startup website URL
Extracts meaningful content
Uses a local LLM (via Ollama)
Generates structured VC-style insights

✨ Features
🔗 URL → Instant analysis
🧠 AI-powered business understanding
📊 Structured JSON output
⚡ Runs locally (no API cost)
🔒 Privacy-friendly

📸 Demo
🔹 Input
python vc_summary.py https://www.linear.app/
🔹 Output
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
🐍 Python
🌐 Requests
🧹 BeautifulSoup
🧠 Ollama (LLM runtime)
🎨 Streamlit (optional UI)

📁 Project Structure
.
├── vc_summary.py        # Main backend script
├── app.py               # Streamlit UI (optional)
├── venv/                # Virtual environment
└── README.md

🛠️ Setup
1. Clone the repo
git clone <your-repo-url>
cd <project-folder>
2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install requests beautifulsoup4 lxml
4. Install Ollama

👉 https://ollama.com/

5. Pull model
ollama run phi3

(Wait for download → press Ctrl + C)

6. Start Ollama server
ollama serve

▶️ Usage
Run CLI version
python vc_summary.py <url>

Example:

python vc_summary.py https://www.perplexity.ai/
Run Web App (optional)
pip install streamlit
streamlit run app.py

⚠️ Limitations
❌ JS-heavy sites (e.g., LinkedIn, LeetCode)
❌ Login-required pages
⚠️ Output quality depends on model (phi3 vs llama3)
🚀 Future Improvements
📊 Investment scoring
🧠 Better prompt engineering
🌐 Support dynamic websites (Selenium/Playwright)
📈 Competitor analysis
🎨 Enhanced UI dashboard
💡 How It Works
URL → HTML → Clean Text → LLM → VC Insights

🧑‍💻 Author

Built as a mini AI product demonstrating:

LLM integration
Backend + AI pipeline
Real-world system design
⭐ If you like this project

Give it a star ⭐ — helps a lot!
