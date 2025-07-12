import os
import requests
from flask import Flask, request, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(_name_)
app.secret_key = "sekreti_yt_i_fortesuar"

api_key = os.getenv("GROQ_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "")

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

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                response_text = response.json()["choices"][0]["message"]["content"]
            else:
                response_text = f"[GABIM {response.status_code}] {response.text}"

        except Exception as e:
            response_text = f"[GABIM NE SERVER] {str(e)}"

    return render_template("chat.html", response=response_text)
