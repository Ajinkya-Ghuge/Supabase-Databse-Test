# 📋 Supabase Feedback CLI App

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

A simple command-line Python application that collects user feedback from the terminal and stores it in a cloud PostgreSQL database using Supabase.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [What is Supabase?](#-what-is-supabase)
- [What I Learned](#-what-i-learned)
- [How the Program Works](#-how-the-program-works)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Example Output](#-example-terminal-output)
- [Future Improvements](#-future-improvements)

---

## 🗂 Project Overview

This project is a beginner-friendly CLI (Command-Line Interface) application built with Python. It demonstrates how to connect a Python script to a real cloud database using Supabase.

When you run the program, it prompts you to enter your **name** and a **feedback message**. That information is then sent over the internet and stored in a PostgreSQL database table called `feedback` — no manual SQL or backend server required.

**Technologies Used:**

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| ⚡ Supabase | Cloud database platform and API |
| 🐘 PostgreSQL | Relational database (hosted by Supabase) |
| 🔐 python-dotenv | Load environment variables from `.env` file |

---

## ⚡ What is Supabase?

[Supabase](https://supabase.com) is an open-source backend platform that provides a **hosted PostgreSQL database** along with **automatically generated APIs**. This means your application can store and retrieve data without you needing to build or manage a full backend server from scratch.

Think of it as a ready-made backend — you create a project on Supabase, define your tables, and immediately get a secure API you can call directly from your code.

> 💡 Supabase is often described as an open-source alternative to Firebase, but it uses PostgreSQL under the hood — making it a great tool for learning real relational databases.

---

## 🎓 What I Learned

Building this project helped me practice and understand several important concepts:

- ✅ **Connecting a Python app to a cloud database** using the Supabase Python client
- ✅ **Inserting data into a PostgreSQL table** programmatically via an API
- ✅ **Using environment variables** to protect sensitive credentials (API keys, URLs)
- ✅ **Taking user input from the terminal** with Python's built-in `input()` function
- ✅ **Managing project dependencies** with a `requirements.txt` file
- ✅ **Publishing a project** using Git and GitHub, including ignoring sensitive files with `.gitignore`

---

## ⚙️ How the Program Works

Here is a step-by-step breakdown of what happens when you run `app.py`:

1. **Environment variables are loaded** — `python-dotenv` reads your `.env` file and makes the Supabase URL and API key available to the script securely.
2. **Supabase client is initialized** — The script connects to your Supabase project using the credentials from the `.env` file.
3. **User is prompted for input** — The program asks the user to type their name and a feedback message directly in the terminal.
4. **Data is sent to Supabase** — The script calls the Supabase API to insert the name and feedback into the `feedback` table in the PostgreSQL database.
5. **Confirmation is displayed** — The program prints a success message so the user knows their feedback was saved.

```
Run app.py
    │
    ▼
Load .env file (URL + API Key)
    │
    ▼
Connect to Supabase
    │
    ▼
Ask user: Name + Feedback
    │
    ▼
Insert data into "feedback" table
    │
    ▼
Print success message ✅
```

---

## 📁 Project Structure

```
supabase-feedback-cli/
│
├── app.py              # Main Python script — runs the program
├── .env                # Stores your Supabase URL and API key (never share this!)
├── .gitignore          # Tells Git to ignore sensitive files like .env
└── requirements.txt    # Lists all Python packages needed to run the project
```

> ⚠️ **Important:** Your `.env` file contains sensitive credentials. Make sure `.env` is listed in your `.gitignore` so it is **never uploaded to GitHub**.

---

## 🛠 Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/supabase-feedback-cli.git
cd supabase-feedback-cli
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Mac/Linux
venv\Scripts\activate           # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Your Supabase Project

1. Go to [https://supabase.com](https://supabase.com) and create a free account.
2. Create a new project.
3. In the **Table Editor**, create a table called `feedback` with the following columns:

| Column Name | Data Type |
|---|---|
| `id` | `int8` (primary key, auto-increment) |
| `name` | `text` |
| `message` | `text` |
| `created_at` | `timestamptz` (default: `now()`) |

4. Go to **Project Settings → API** and copy your **Project URL** and **anon public API key**.

### 5. Create Your `.env` File

Create a file called `.env` in the root of the project and add your Supabase credentials:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-public-api-key
```

> 🔒 Never commit this file to GitHub. It is already listed in `.gitignore` to keep your credentials safe.

---

## ▶️ How to Run

Once everything is set up, run the program with:

```bash
python app.py
```

The program will start in your terminal and prompt you for input.

---

## 💻 Example Terminal Output

```
$ python app.py

Welcome to the Feedback App!
Please enter your name: Alex
Please enter your feedback: This app is really easy to use and a great learning project!

✅ Thank you, Alex! Your feedback has been saved successfully.
```

After running the program, you can log in to your Supabase dashboard and view the submitted data directly in the `feedback` table.

---

## 🔮 Future Improvements

Here are some features that could be added to extend this project:

- [ ] **View all feedback** — Add an option to read and display all stored feedback from the database
- [ ] **Delete feedback** — Allow users to remove their own entries by ID
- [ ] **Timestamps** — Display when each piece of feedback was submitted
- [ ] **Input validation** — Prevent empty submissions or enforce a character limit
- [ ] **Export to CSV** — Let users download all feedback as a spreadsheet
- [ ] **Web interface** — Build a simple front-end using Flask or FastAPI to display feedback in a browser

---

## 🙌 Acknowledgements

- [Supabase Documentation](https://supabase.com/docs)
- [Supabase Python Client](https://github.com/supabase/supabase-py)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

---

> Made with ❤️ and Python
