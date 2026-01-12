from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model/fraud_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    if request.method == "POST":
        data = [[
            float(request.form["amount"]),
            float(request.form["oldbalanceOrg"]),
            float(request.form["newbalanceOrig"]),
            float(request.form["oldbalanceDest"]),
            float(request.form["newbalanceDest"])
        ]]
        result = model.predict(data)[0]
        prediction = "Fraud Transaction 🚨" if result == 1 else "Legitimate Transaction ✅"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)