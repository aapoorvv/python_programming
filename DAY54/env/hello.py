from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_function():    
        str = function()
        return f"<b>{str}</b>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():    
        str = function()
        return f"<u>{str}</u>"
    return wrapper_function


@app.route("/")
def hello_world():
    return  ' <h1 style="text-align: center">Hello, World!</h1>'\
            '<p>This is a paragraph.</p>'\
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXZwZ2U1eWpvazE5ZHptamEzajY4a2swYTFkb2V5OXlxcXB3MzRtNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wofyg8nxsWEmtR7eOK/giphy.gif" width=300>'

@app. route("/bye")
@make_bold
@make_underline
def greet() :
    # return '<em><b>Bye</b></em>'
    return "bye"

@app.route("/<name>/<int:number>")
def geet(name,number) :
    return f"Hello there {number} {name}!"

if __name__ ==  "__main__":
    app.run(debug=True)