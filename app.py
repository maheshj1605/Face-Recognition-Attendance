from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Face Recognition Attendance System</h1>
    <p>My online attendance project is working!</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
