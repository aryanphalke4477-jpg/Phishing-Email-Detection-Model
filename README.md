# Phishing Email Detection Model

1) Overview

The Phishing Email Detection Model is a Machine Learning-based cybersecurity project that identifies whether an email is **Phishing** or **Safe** based on its textual content and URL-related features.

The system uses **Natural Language Processing (NLP)** techniques and **Scikit-learn** to analyze email content, extract meaningful features, and classify messages to help users identify potential phishing attacks.

2) Features
* Email content analysis
* Phishing vs Safe email classification
* TF-IDF feature extraction
* URL pattern detection
* Machine Learning prediction using Naive Bayes
* Accuracy evaluation
* Confusion Matrix visualization
* Prediction history tracking
* Dark-themed responsive user interface
* Flask web application

3) Technologies Used

# Backend
* Python
* Flask
  
# Machine Learning
* Scikit-learn
* Pandas
* NumPy

# Frontend
* HTML
* CSS

# Concepts
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Text Classification
* Supervised Machine Learning

4) Project Structure

```text
Phishing Email Detection Model/
│
├── app.py
├── model.py
├── emails.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

5) Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/phishing-email-detection-model.git
```

### 2. Navigate to Project Folder

```bash
cd phishing-email-detection-model
```

### 3. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

---

6) Running the Application

Start the Flask server:

```bash
py app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

7) Dataset

The project uses a dataset containing examples of:

* Phishing emails
* Legitimate emails

Each email is labeled as:

| Label | Meaning  |
| ----- | -------- |
| 1     | Phishing |
| 0     | Safe     |

---

8) Machine Learning Workflow

1. Load email dataset
2. Preprocess text
3. Extract URL-related features
4. Apply TF-IDF vectorization
5. Split dataset into training and testing sets
6. Train Naive Bayes classifier
7. Evaluate accuracy
8. Generate confusion matrix
9. Predict user-provided email content

---

9) Sample Predictions

### Example 1

Input:

```text
Verify your bank account immediately by clicking this link.
```

Output:

```text
Phishing
```

### Example 2

Input:

```text
Team meeting scheduled tomorrow at 10 AM.
```

Output:

```text
Safe
```

10) Performance Metrics

The application displays:

* Model Accuracy
* Confusion Matrix
* Prediction Results
* Prediction History

These metrics help evaluate the effectiveness of the machine learning model.

11) Future Enhancements

* Larger phishing datasets
* Real-time email scanning
* Email attachment analysis
* Deep Learning integration
* Browser extension support
* Email API integration
* Advanced URL reputation checking

12) Learning Outcomes

This project demonstrates practical implementation of:

* Cybersecurity concepts
* Phishing detection techniques
* Natural Language Processing
* Machine Learning classification
* Flask web development
* Data preprocessing and evaluation

---

## Author

Aryan Phalke

Cybersecurity & Machine Learning Internship Project
