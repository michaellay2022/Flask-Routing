from flask import Flask
app = Flask(__name__)

# Create a root route ("/") that responds with "Hello World!"


@app.route('/')
def hello_world():
    return 'Hello World!'

# Create a route that responds with "Dojo!"


@app.route("/Dojo")
def dojo():
    return "Hello Dojo! "

# Create a route that responds with "Hi" and whatever name is in the URL after /say/


@app.route("/say/<name>")
def say_name(name):
    # capitalize is used to capitalize even user input lower case.
    return f"Hi {name.capitalize()}!"


@app.route("/repeat/<int:num>/<string:word>")
def repeat_word(num, word):
    verti_word = ""
    for i in range(0, num):
        verti_word += f'<h1> {word.capitalize()} </h1>'

    # return f'{word * num}'
    return verti_word


if __name__ == "__main__":
    app.run(debug=True)
