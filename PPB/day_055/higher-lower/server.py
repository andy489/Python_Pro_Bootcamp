from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

number_gifs = [
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cHE1ZXptY2JvOG55MXRoMjdlZjN4am93ZDhsZ2V2YnpkM2U0ZHQwdCZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/26gs9hWZig4XobSTe/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ejByaWN4YjJjeGxraXZqdnE4cXA3OWViYTk1MTJ2M3U4MGUwNG0xcSZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/l0ExncehJzexFpRHq/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ejByaWN4YjJjeGxraXZqdnE4cXA3OWViYTk1MTJ2M3U4MGUwNG0xcSZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/26gsqQxPQXHBiBEUU/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ejByaWN4YjJjeGxraXZqdnE4cXA3OWViYTk1MTJ2M3U4MGUwNG0xcSZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/l0EwYkyU1JCExVquc/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cHE1ZXptY2JvOG55MXRoMjdlZjN4am93ZDhsZ2V2YnpkM2U0ZHQwdCZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/d1E1szXDsHUs3WvK/giphy.gif",

    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmE3NGU1cWNubWpyN3dsd2pkOWR1YmwzYnViZ2N3dWVibGhrdG4wZiZlcD12MV9"
    "pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0ExvMqtnw7aTzPCE/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cHE1ZXptY2JvOG55MXRoMjdlZjN4am93ZDhsZ2V2YnpkM2U0ZHQwdCZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/l0Ex9pftnvPgw0nPa/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cHE1ZXptY2JvOG55MXRoMjdlZjN4am93ZDhsZ2V2YnpkM2U0ZHQwdCZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/l0ExiSoCkhCfSm94k/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ejByaWN4YjJjeGxraXZqdnE4cXA3OWViYTk1MTJ2M3U4MGUwNG0xcSZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/26gsasKHkeH0VP8d2/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ejByaWN4YjJjeGxraXZqdnE4cXA3OWViYTk1MTJ2M3U4MGUwNG0xcSZlcD12MV9"
    "naWZzX3JlbGF0ZWQmY3Q9Zw/26gsjCWitFy3euTeM/giphy.gif",
]

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" height=360/>')

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return ('<h1 style="color: purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" height=360/>')

    elif guess < random_number:
        return ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" height=360/>')
    else:
        return ('<h1 style="\'"color: green"\'">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" height=360/>'
                f'<img src="{number_gifs[guess]}" height=360/>')


if __name__ == "__main__":
    app.run(debug=True)