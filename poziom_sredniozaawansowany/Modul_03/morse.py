morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "Ą": ".-.-",
    "Ć": "-.-..",
    "Ę": "..-..",
    "Ł": ".-..-",
    "Ń": "--.--",
    "Ó": "---.",
    "Ś": "...-...",
    "Ż": "--..-.",
    "Ź": "--..-",
}


def morse_decode(text: str) -> str:
    if type(text) is not str:
        return f"Bad input type: {type(text)}."

    decoded = ""
    letter_separator = "/"
    word_separator = "#"

    for letter in text.upper():
        if letter in morse_alphabet:
            decoded += morse_alphabet[letter] + letter_separator
        elif letter == " ":
            decoded += word_separator

    return decoded


decoded = morse_decode("SOS nadaje rudy102")
print(decoded)
