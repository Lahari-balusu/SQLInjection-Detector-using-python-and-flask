from flask import Flask, render_template, request, jsonify
from detection import detect_sql_injection

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    user_input = request.form.get("user_input")
    is_sql_injection = detect_sql_injection(user_input)

    result = {
        "input": user_input,
        "is_sql_injection": is_sql_injection
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
