from flask import Flask, render_template

app = Flask(__name__)

myUsers = ["Jean", "Arnaud", "Michael"]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Home",
        text="Bonjour a",
        users=myUsers,
    )


@app.route("/extension")
def extend():
    return render_template("extend.html", title="Extension", users=myUsers)


if __name__ == "__main__":
    app.run(debug=True)
