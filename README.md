# 🤖 Simple-Agent(Gemini API)

This is a terminal-based multi-agent chatbot system powered by Google's Gemini API. Choose from different agent personalities such as **Greeting Agent**, **Motivational Coach**, **Tech Guru**, and more!

---
## ⚙️ Requirements

- Python 3.10+
- [`uv`](https://github.com/astral-sh/uv) (faster Python package manager)
- [Google Gemini API Key](https://makersuite.google.com/app/apikey)

---

## 🔐 Step 1: Add Your API Key

Create a `.env` file in the root folder:

```
GEMINI_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your actual Gemini API key.

---

## 🧪 Step 2: Install Dependencies Using `uv`

Open your terminal and run:

```bash
cd your-folder-name
uv venv                         # Create virtual environment
uv pip install python-dotenv openai  # Install required packages
Alternatively, if you have a requirements.txt, use:

uv pip install -r requirements.txt
```

---

🚀 Step 3: Run the Application
Activate your virtual environment and run the app:

**macOS/Linux**

`source .venv/bin/activate`

**Windows**

`.venv\Scripts\activate`

**Run the chatbot**

`uv run main.py`

---

🧠 Agent Options (Currently Available):

1	Greeting Agent

2	Motivational Coach

3	Wise Scholar

4	Tech Guru

5	Friendly Storyteller

You can easily add more agents to the agents dictionary in main.py.

---

❗ Troubleshooting

**API Key Error**:

If you get ValueError: `GEMINI_API_KEY` not found, make sure your `.env` file is correctly placed and formatted.

**Missing Modules**:

If you see ModuleNotFoundError, make sure you’ve installed all dependencies via uv pip install.

**🛠️ Customization Ideas**:

Add more agents like Weather Bot, Cooking Expert, or Fitness Coach

Add a chat loop to keep the conversation going

Build a GUI using Streamlit or Tkinter

---

Happy coding! 🎉

**Build with ❤ by [Faria Mustaqim](https://github.com/Zaibunis)**
