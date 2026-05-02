# 🚀 Machine Learning Flask App

A simple and clean **Machine Learning Web App** built using **Flask** and **Scikit-learn**.
This app allows users to input feature values and get real-time predictions from a trained model.

---

## 📌 Features

* Train multiple ML models (Logistic Regression, SVM, Random Forest)
* Automatically selects the **best performing model**
* Saves the trained model using **joblib**
* Simple and clean **Flask web interface**
* Ready to deploy or extend

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* NumPy
* HTML + CSS 🎨

---

## 📂 Project Structure

```
project/
│── app.py
│── saved_models/
│     └── Random_Forest.joblib
│── templates/
│     └── index.html
│── static/
│     └── style.css
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app

```
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 How It Works

1. User enters feature values in the form
2. Flask receives the input
3. Input is passed to the trained ML model
4. Model returns prediction
5. Result is displayed on the UI

---

## 🧠 Model Info

* Models Used:

  * Logistic Regression
  * Support Vector Machine (SVM)
  * Random Forest (Best Model Selected)
* Evaluation Metrics:

  * Accuracy
  * Confusion Matrix
  * Classification Report

---

## 💾 Model Saving

The best model is automatically saved using:

```
joblib.dump(model, "saved_models/model.joblib")
```

---

## 🔥 Future Improvements

* Add data visualization 📊
* Improve UI/UX 🎨
* Add model selection option
* Deploy on cloud (Render / AWS / HuggingFace)

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Your Name

---

⭐ If you like this project, don't forget to give it a star!
