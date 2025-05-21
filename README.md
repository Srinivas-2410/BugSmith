# BugSmith – AI-Powered Bug Report Assistant

BugSmith is an AI-based tool designed to help testers and developers file rich, structured bug reports effortlessly. Powered by cutting-edge LLMs (Gemini/GPT), BugSmith generates detailed reproduction steps, suggests bug categories, and provides code insights from a short bug description.

---

## ✨ Features

- **Simple Form-Based Bug Entry:** Easy UI for testers to describe bugs.
- **AI-Generated Detailed Reports:** Automatically expands brief input into a comprehensive report.
- **PDF Export:** Download bug reports as professional PDFs.
- **One-Click GitHub Issue Creation:** Instantly create GitHub issues from generated reports.
- **Customizable Severity & Environment:** Capture essential metadata.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI Integration:** Gemini API (Google Generative AI)
- **PDF Generation:** ReportLab
- **Frontend:** HTML, CSS
- **Other:** GitHub API integration, python-dotenv

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Gemini API key](https://ai.google.dev/)
- (Optional) GitHub Personal Access Token for issue creation

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Srinivas-2410/BugSmith.git
    cd BugSmith
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the repo root:
      ```
      GEMINI_API_KEY=your_gemini_api_key_here
      # For GitHub issue creation (optional)
      GITHUB_TOKEN=your_github_token_here
      GITHUB_REPO=yourusername/yourrepo
      ```
4. **Run the application:**
    ```sh
    python app.py
    ```

5. **Open in your browser:**  
   Visit [http://localhost:5000](http://localhost:5000)

---

## 📝 Usage

1. Fill in the bug description, severity, and environment.
2. Click "Generate Report" to get a detailed AI-generated bug report.
3. Download as PDF or create a GitHub issue directly from the interface.

---

## 📂 Project Structure

```
BugSmith/
├── app.py                  # Flask app routes
├── requirements.txt
├── utils/
│   ├── ai_engine.py        # AI bug report logic (Gemini/GPT)
│   └── pdf_generator.py    # PDF export logic
├── github/
│   └── issue_creator.py    # GitHub issue creation logic
├── templates/
│   └── index.html          # Web UI
├── static/
   └── styles.css          # Styling

```

---

## 🤖 How it Works

- The user submits a bug summary, severity, and environment.
- BugSmith prompts Gemini/GPT to generate:
  - Steps to reproduce
  - Bug category (UI, Backend, Logic, etc.)
  - Suspected code component (if possible)
  - Severity and environment context
- The report can be saved as PDF or filed as a GitHub issue.

---

## 🛡️ License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Flask](https://flask.palletsprojects.com/)
- [ReportLab](https://www.reportlab.com/)
- [GitHub REST API](https://docs.github.com/en/rest)

---

*Happy Bug Hunting with BugSmith!*
