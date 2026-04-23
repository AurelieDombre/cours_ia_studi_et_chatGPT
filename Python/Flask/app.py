from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search.html")

@app.route('/search', methods=['POST'])
def search():
    text = request.form["recherche"]
    return redirect(url_for('success', recherche=text))

@app.route('/success')
def success():
    text = request.args.get("recherche")
    return render_template("success.html", recherche=text)

if __name__ == "__main__":
    app.run(debug=True)