import random
from flask import Flask
app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route("/")
def home():
    return  '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHNrM2xyODQ2amcyZWM4ZnozZDdxOHR2d3JydTN5NjAyeHEwcXBtYiZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/gxz5yu2YXuXx2N2eoM/giphy.gif" width=300>'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)


