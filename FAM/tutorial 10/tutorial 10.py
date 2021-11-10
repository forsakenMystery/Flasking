from flask import Flask
from admin.second import second1

app = Flask(__name__)
app.register_blueprint(second1, url_prefix="/admin")

@app.route("/")
def test():
    return "test"

if __name__ == "__main__":
    app.run(debug=True)