from flask import Flask
myapp = Flask(__name__)
@myapp.route("/")
def hello():
    return ("Flask mega tutorial")
if __name__ == "__main__":
    myapp.run(debug=True)
