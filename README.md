# EC2 Flask Tech Quiz Game

A simple interactive quiz game deployed on an Amazon EC2 instance using a Python Flask backend. Users can answer cloud, Linux, and programming-related multiple-choice questions, making it a great beginner-friendly project to demonstrate EC2 hosting, security groups, Linux configuration, and Flask application deployment.

## 🚀 **Features**

- Random Tech Quiz Questions
- Flask Backend API (`/get_question`)
- Interactive Frontend
- Deployed on AWS EC2
- Lightweight & Fast

## 🏗️ **Architecture Overview**

```
User Browser
     │
     ▼
Internet (HTTP Request)
     │
     ▼
AWS Security Group (Allows Port 5000/80)
     │
     ▼
Amazon EC2 Instance (Amazon Linux 2)
     │
     ▼
Flask Web Application  (Serves index.html & Provides /get_question API)
```

## 📦 **Project Structure**

```
techquiz/
│── app.py
│── templates/
│     └── index.html
│── static/
      └── style.css (optional)
```

## ⚙️ **How It Works**

1. A user opens the app through the EC2 public IP.
2. The frontend sends a request to `/get_question`.
3. Flask returns a random question + options in JSON format.
4. User selects an answer → frontend checks correctness.
5. The user can click **Next Question** to fetch a new one.
6. All processing happens on the EC2-hosted Flask backend.

## 🔧 **AWS Services Used**

1. **Amazon EC2**
2. **Security Groups**
3. **EC2 Key Pair**

## 🛠️ **Setup Instructions**

**1.** Launch EC2 Instance
**2.** SSH into EC2
**3.** Install Dependencies
**4.** Upload Your Project
**5.** Run Application
**6.** Open in Browser

-> Refer to the full documentation for detailed implementation steps.

**📄Documentation**: [documentation.pdf](https://github.com/user-attachments/files/23960141/aws-ec2-flask-deployment.pdf)

## 🌐 **Live Demo (Optional)**

![Image](https://github.com/user-attachments/assets/77a3369b-3db6-460a-a4a4-4779f983b262)
