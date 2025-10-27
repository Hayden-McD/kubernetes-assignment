from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("homepage.html")

# This runs only if the file is run using python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
