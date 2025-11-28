from flask import Flask, jsonify, render_template
import random


app = Flask(__name__)

questions = [
    {
        "question": "What does EC2 stand for?",
        "options": [
            "Elastic Compute Cloud",
            "Elastic Cloud Container",
            "Elastic Cluster Control",
        ],
        "answer": "Elastic Compute Cloud",
    },
    {
        "question": "Which AWS service is used for object storage?",
        "options": ["EC2", "S3", "RDS"],
        "answer": "S3",
    },
    {
        "question": "Which Linux command lists files?",
        "options": ["ls", "pwd", "cd"],
        "answer": "ls",
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "HyperText Markup Language",
            "HighText Machine Language",
            "Hyper Tool Multi Language",
        ],
        "answer": "HyperText Markup Language",
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_question")
def get_question():
    return jsonify(random.choice(questions))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
