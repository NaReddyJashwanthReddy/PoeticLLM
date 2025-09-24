# Text Rewriter App — Poetic & Humorous Styles

## Overview

The **Text Rewriter App** is a Streamlit-based application that allows users to rewrite text in different tones (currently **humorous** and **poetic**) using a generative LLM. The app leverages configurable prompt templates to guide the model’s responses and provides a simple, interactive web UI.

---

## Features

* 🎭 **Style transfer**: Rewrite text into *humorous* or *poetic* forms
* 📝 **Prompt templates**: Choose between *Simple*, *Conversational*, or *RolePlaying* prompting strategies
* ⚡ **Interactive UI**: Built with Streamlit for quick experimentation and usability
* 🔐 **Environment configuration**: Secrets and API keys are managed via `.env` and `config.yaml`
* 🪵 **Logging & error handling**: Centralized logging and exception management

---

## Project Structure

```
.
├── app.py                # Streamlit app entry point
├── config.yaml           # Configuration file for runtime settings
├── .env                  # Environment variables (e.g., API keys)
├── Model/
│   └── model.py          # LLM wrapper for text rewriting
└── utils/
    ├── logger.py         # Logging utilities
    └── handler.py        # Exception handler
```

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-org/text-rewriter-app.git
cd text-rewriter-app
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### `.env`

The `.env` file stores sensitive keys (e.g., API keys).
Example:

```env
api_key="your_api_key_here"
```

### `config.yaml`

Holds runtime parameters like model settings, default style, and template configuration.
Adjust as needed before running the app.

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Access the UI at:
👉 [http://localhost:8501](http://localhost:8501)

---

## How It Works

1. User enters text in the input box
2. Selects a **prompt template** (Simple, Conversational, RolePlaying)
3. Chooses a **style** (Humorous or Poetic)
4. Submits form → Model rewrites text according to style and template
5. Output is displayed in the UI

---

## Example

**Input:**

```
The sun is rising, and people are waking up for work.
```

**Output (Poetic, Simple Template):**

```
Golden light spills across the earth,
Stirring souls from dreams to daily toil.
```

**Output (Humorous, Conversational Template):**

```
The sun clocked in early today,  
Meanwhile, humans hit snooze for the fifth time.
```

---

## Logging & Error Handling

* All model calls and app events are logged via `utils/logger.py`
* Errors are captured and handled gracefully with `utils/handler.py`

---

## Roadmap

* Add more **styles** (formal, sarcastic, academic, etc.)
* Extend **prompt template library**
* Multi-language support
* Deploy on cloud (AWS/GCP/Azure/Streamlit Cloud)

---

## Contributors

* **N. Jasheanth Reddy**
* Open to contributions via PRs and issues

---

Do you want me to extend this README with **MLOps production-level details** (MLflow, Docker, CI/CD, monitoring) like I did for the previous one, or keep this one lightweight and app-focused?
