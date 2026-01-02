# 📊 Retail Sales Prediction Web Application

A full-stack machine learning web application that predicts retail sales based on date, store, and promotional factors. The system combines a trained ML regression model with a Flask backend API and a responsive frontend dashboard.

---

## 🚀 Features

* Predicts daily retail sales using historical data
* Date-based input with automatic feature extraction
* REST API built with Flask
* Interactive sales trend visualization
* Fully deployed backend and frontend

---

## 🧠 Machine Learning

* **Model type:** Regression
* **Input features:**

  * Store ID
  * Promotion indicator
  * Holiday indicator
  * Day, Month, Day of Week (derived from date)
* **Output:** Predicted sales value
* **Dataset:** Retail sales dataset with promotional and holiday indicators

The model is trained offline and served through a Flask API for real-time predictions.

---

## 🏗️ Tech Stack

### Backend

* Python
* Flask
* Flask-CORS
* Pandas
* Scikit-learn
* Joblib

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Deployment

* **Backend:** Render
* **Frontend:** Vercel

---

## 🌐 Live Demo

* **Frontend:** *(Vercel deployment link)*
* **Backend API:** *(Render deployment link)*

Example API usage:

```
/predict?store=1&promo=0&holiday=0&day=15&month=7&dow=1
```

---

## 📁 Project Structure

### Backend

```
app.py
requirements.txt
sales_forecast_model.pkl
```

### Frontend

```
index.html
```

---

## ⚙️ How It Works

1. User selects a date and store details on the frontend
2. Frontend extracts date components automatically
3. Data is sent to the Flask backend via REST API
4. ML model predicts sales
5. Results are displayed with a line chart for trend visualization

---

## 📌 Key Learnings

* End-to-end ML project development
* Feature engineering from date inputs
* Building and consuming REST APIs
* Full-stack deployment using cloud platforms
* Debugging real-world deployment issues

---

## 📄 Resume Description

**Retail Sales Prediction Web Application**

* Built a full-stack machine learning web application to forecast retail sales
* Developed a Flask REST API to serve ML predictions
* Designed a responsive frontend with interactive data visualization
* Deployed backend on Render and frontend on Vercel

---

## ✨ Future Improvements

* Support for multiple stores and longer forecasting horizons
* More advanced time-series models
* Authentication and data upload support
* UI enhancements and analytics dashboard

---

## 🙌 Acknowledgements

This project was built as a hands-on learning experience to understand real-world ML deployment and full-stack integration.
