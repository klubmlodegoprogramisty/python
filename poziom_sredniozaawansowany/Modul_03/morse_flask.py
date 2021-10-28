from flask import Flask, request
from morse import *


# tworzymy główny obiekt aplikacji
app = Flask("Morse Alphabet")

# definiujemy akcję związaną z URL: "/"
@app.route("/", methods=["POST", "GET"])
def code_form():
    post = """
    <h1> Morse coding </h1> <hr>
    <form method="POST" action="/">
    Enter text to code: <input type="text" name="text"><br>
    <input type="submit" value="Decode">
    </form>"""

    if request.method == "GET":
        return post
    else:
        decoded = morse_decode(request.form["text"])
        morse_text = f"""
        <h1> Morse coding </h1> <hr>
        text to code: <pre>{request.form['text']}</pre> <br>
        Morse coding: <br> <pre>{decoded}</pre>
        """
        return morse_text


# start - uruchamiamy serwer WWW pod adresem http://127.0.0.1:5000
app.run()
