# 📏 Height & Weight Prediction Using Simple Linear Regression

## 📌 Project Overview

This project is a **Height & Weight Prediction Web Application** developed using **Simple Linear Regression (SLR)**, a supervised machine learning algorithm.

The application predicts a person's weight based on their height using a trained Linear Regression model.

The machine learning model is integrated with a **Flask web application**, providing a user-friendly interface built using HTML and CSS.

🌐 **Live Application:** https://slr-model-ml.onrender.com/

## 🚀 Features

- Predicts weight based on the height entered by the user.
- Implements Simple Linear Regression for prediction.
- Interactive and responsive web interface.
- Built using Flask for backend integration.
- Displays prediction results directly on the webpage.
- Deployed on Render for online accessibility.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming and ML implementation |
| Scikit-learn | Simple Linear Regression model |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Flask | Backend web framework |
| HTML | Webpage structure |
| CSS | Webpage styling |
| Pickle | Saving and loading the trained model |
| Git & GitHub | Version control |
| Render | Web application deployment |

## 🧠 Machine Learning Algorithm

### Simple Linear Regression

Simple Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value based on a single independent variable.

The mathematical equation is:

**Y = mX + c**

Where:

- **Y** = Predicted Weight
- **X** = Input Height
- **m** = Regression coefficient (slope)
- **c** = Intercept

The model learns the relationship between height and weight from the training dataset and uses this relationship to make predictions.

## ⚙️ How the Application Works

1. The user opens the Height & Weight Prediction website.
2. The user enters a height value.
3. The HTML form sends the input to the Flask backend.
4. Flask passes the input to the trained Linear Regression model.
5. The model predicts the corresponding weight.
6. Flask displays the predicted weight on the webpage.

**Workflow:**

User Input (Height) → Flask Backend → Trained SLR Model → Predicted Weight → Webpage

## 📂 Project Structure

```text
SLR_Model/
│
├── app.py
├── SLR_model.pkl
├── Procfile
├── requirements.txt
├── test.py
│
├── templates/
│   └── index.html
│
└── README.md
```

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Lakshmiprasanna-9/SLR_Model.git
```

### 2. Navigate to the project directory

```bash
cd SLR_Model
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask application

```bash
python app.py
```

### 6. Open the application

Visit:

http://127.0.0.1:5000/

## 🌐 Deployment

The application is deployed on **Render**, a cloud hosting platform.

**Live Website:**

https://slr-model-ml.onrender.com/

The deployment uses:

- GitHub for source code management.
- Render for hosting.
- Gunicorn as the production WSGI server.
- Flask for handling HTTP requests and predictions.

## 📈 Applications

- Understanding the fundamentals of regression-based prediction.
- Demonstrating machine learning model integration with web applications.
- Learning end-to-end ML application development.
- Practicing Flask deployment and cloud hosting.

## ⚠️ Limitations

- Predictions depend on the quality and range of the training dataset.
- The model uses height as its only input feature.
- Predictions may be inaccurate for values outside the training range.
- The application is intended for educational purposes and should not be used for medical or health assessments.

## 👩‍💻 Author

**Lakshmi Prasanna**

---



**Developed using Python, Machine Learning, Flask, HTML, and CSS.**
