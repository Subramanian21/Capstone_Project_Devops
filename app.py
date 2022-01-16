from flask import Flask

## Start flask app
app = Flask(__name__)

@app.route('/')
def greetings():
    return "<h2>Hello World!</h2><br><h3>My name is Subramanian and this is my Capstone Project</h3>"


if __name__ == '__main__':
    ## Run app on localhost with port 80
    app.run(host="0.0.0.0", port=80)