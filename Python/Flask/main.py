from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        prenom = request.form["firstname"]
        nom = request.form["lastname"]
        return redirect(url_for('success', prenom=prenom, nom=nom))

@app.route('/success/<prenom>/<nom>')
def success(prenom, nom):
    return f'Bonjour {prenom} {nom}'

if __name__ == "__main__":
    app.run(debug=True)