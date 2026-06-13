# 🏥 Health Monitoring Application

> A machine learning web app that predicts a patient's health status based on key vitals and lifestyle inputs.

Built as a final year group project using Flask and scikit-learn with a Decision Tree classifier trained on real health data.

## What it does

Enter a patient's vitals and lifestyle details. The app runs them through a trained ML model and instantly predicts:

- ✅ **Perfectly okay**
- ⚠️ **May be a chance of ill**
- 🚨 **Ill, must consult a doctor**

## Input Parameters

| Parameter | Description |
|---|---|
| Gender | Male / Female |
| Age | Patient's age |
| BMI | Body Mass Index |
| Temperature | Body temperature |
| SBP | Systolic Blood Pressure |
| Pulse | Heart rate |
| Alcohol | Drinker or not |
| Smoker | Smoker or not |
| Sleep Hours | Average hours of sleep |

## How it works

```
User enters vitals (Flask form)
          │
          ▼
  Preprocessing
  (Label Encoding for categorical fields)
          │
          ▼
  Decision Tree Classifier
  (trained on DATASET.csv, saved via joblib)
          │
          ▼
  Prediction output on screen
  (Okay / Possible illness / See a doctor)
```

## Tech Stack

| Layer | Tech |
|---|---|
| Web Framework | Flask |
| ML Model | Decision Tree (scikit-learn) |
| Data Processing | Pandas, NumPy |
| Model Persistence | joblib |
| Frontend | HTML, Bootstrap 4, CSS |
| Notebook | Jupyter (preprocessing + model training) |

## Setup

### 1. Install dependencies

```bash
pip install flask scikit-learn pandas numpy joblib
```

### 2. Train the model (if `model.save` is missing)

Open and run `preprocessing.ipynb`. It cleans the dataset, trains the Decision Tree, and saves `model.save` via joblib.

### 3. Run the app

```bash
cd "Health Monitoring app"
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Project Structure

```
Health Monitoring app/
├── app.py                  # Flask app, routes and prediction logic
├── preprocessing.ipynb     # Data cleaning, model training, model export
├── DATASET.csv             # Health dataset used for training
├── model.save              # Trained Decision Tree model (joblib)
├── templates/
│   └── index.html          # Input form + result display
└── static/
    ├── health.jpg          # Background image
    └── css/style.css       # Styles
```

## Team

Final year group project.

| Name | GitHub |
|---|---|
| Hari (primary developer) | [@hari72328](https://github.com/hari72328) |
| Saumya Srinivasan | [@SaumyaSrinivasan](https://github.com/SaumyaSrinivasan) |

*ML-based health status prediction using patient vitals.*
