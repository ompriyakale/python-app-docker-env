Here’s a complete, best-practice Python + .env + Docker setup:

📁 1. Project structure
python-app-docker-env/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
Dockerfile


🐍 2. Python app
app.py

📦 3. Dependencies
requirements.txt
python-dotenv is used to load .env files into Python.

4. Environment template (SAFE for Git)
.env.example

🚫 5. Git ignore (IMPORTANT)
👉 This ensures real secrets are NOT pushed to GitHub.

🐳 6. Dockerfile

🚀 7. Build Docker image

▶️ 8. Run locally (with .env file)
First create your real .env:
docker run --env-file .env python-app-docker-env
🎯 Output
Hello Ompriya from Pune!


🧠 Key best practices used here

✔ .env not committed
✔ .env.example shared
✔ python-dotenv for local dev
✔ Docker uses --env-file
✔ Clean separation of code and secrets
