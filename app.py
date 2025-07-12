from flask import Flask, request, render_template
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("GROQ_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "model": "llama3-8b-8192"
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
        else:
            content = "Gabim në marrjen e përgjigjes."

        return render_template("chat.html", response=content)

    return render_template("chat.html")
