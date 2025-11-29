from flask import Flask, jsonify, render_template

# Import "flask" could not be resolved error
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
    {
        "question": "Which AWS service is used for relational databases?",
        "options": ["Lambda", "RDS", "EFS"],
        "answer": "RDS",
    },
    {
        "question": "What command shows the current working directory in Linux?",
        "options": ["pwd", "ls", "mkdir"],
        "answer": "pwd",
    },
    {
        "question": "Which protocol is used to securely transfer files?",
        "options": ["FTP", "SFTP", "HTTP"],
        "answer": "SFTP",
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Power Unit",
            "Central Program Utility",
        ],
        "answer": "Central Processing Unit",
    },
    {
        "question": "Which AWS service is serverless compute?",
        "options": ["EC2", "Lambda", "ECS"],
        "answer": "Lambda",
    },
    {
        "question": "Which command creates a new directory in Linux?",
        "options": ["touch", "mkdir", "rm"],
        "answer": "mkdir",
    },
    {
        "question": "What does CSS stand for?",
        "options": [
            "Computer Style Sheet",
            "Cascading Style Sheets",
            "Creative Styling System",
        ],
        "answer": "Cascading Style Sheets",
    },
    {
        "question": "Which AWS service is used for NoSQL databases?",
        "options": ["DynamoDB", "Redshift", "Aurora"],
        "answer": "DynamoDB",
    },
    {
        "question": "Which command is used to remove a file in Linux?",
        "options": ["rm", "del", "erase"],
        "answer": "rm",
    },
    {
        "question": "Which protocol is used for secure web browsing?",
        "options": ["HTTP", "HTTPS", "SSH"],
        "answer": "HTTPS",
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
