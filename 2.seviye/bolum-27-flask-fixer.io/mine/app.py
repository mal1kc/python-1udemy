from flask import Flask, render_template, request
import requests

FİXER_URL = (
    "http://data.fixer.io/api/latest?access_key=***REMOVED***"
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    info = dict()
    if request.method == "POST":
        firstCurrency = request.form["firstCurrency"]
        secondCurrency = request.form["secondCurrency"]

        amount = float(request.form["amount"])

        response = requests.get(FİXER_URL)
        jsonData = response.json()
        result = (
            jsonData["rates"][secondCurrency] / jsonData["rates"][firstCurrency]
        ) * amount
        print(
            "{0:,.2f} {1} = {3:,.2f} {2}".format(
                amount, firstCurrency, secondCurrency, result
            )
        )
        info["amount"] = amount
        info["firstCurrency"] = firstCurrency
        info["result"] = result
        info["secondCurrency"] = secondCurrency
        return render_template("index.html", info=info)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
