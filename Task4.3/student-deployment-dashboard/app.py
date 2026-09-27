from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        application="Student Deployment Dashboard",
        version="1.0",
        environment="Production",
        container_status="Running",
        deployment_platform="Docker"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)