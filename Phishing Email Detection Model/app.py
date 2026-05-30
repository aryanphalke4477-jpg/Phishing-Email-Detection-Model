from flask import Flask
from flask import render_template
from flask import request

from model import train_model
from model import predict_email

app = Flask(__name__)

model, vectorizer, accuracy, matrix = train_model()

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        email_text = request.form["email"]

        prediction = predict_email(
            email_text,
            model,
            vectorizer
        )

        history.append({
            "email": email_text[:50],
            "result": prediction
        })

    return render_template(
        "index.html",
        prediction=prediction,
        accuracy=accuracy,
        matrix=matrix,
        history=history
    )

if __name__ == "__main__":
    app.run(debug=True)