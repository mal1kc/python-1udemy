from flask import Flask, app,render_template,request
import requests

base_url ="https://api.github.com/users/"

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form["githubname"]
        user_info = requests.get(base_url+username).json()
        repos = requests.get(base_url+username+"/repos").json()
        
        if "message" in user_info:
            return render_template("index.html",error = "Kullanıcı Bulunamadı...")
        else:

            return render_template("index.html",profile = user_info,repos = repos)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    