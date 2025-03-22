from app import app


@app.route("/")
def index():
    return "<h1>Learning Flask</h1>"
