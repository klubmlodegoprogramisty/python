from message_digest import *
from podstawieniowy import *
import PySimpleGUI as sg

layout = [
    [sg.Text("Some Complex GUI application - just for testing")],
    [sg.Txt("-----------------------------------" * 2)],
    [sg.Text("Choose file to create digest"), sg.FileBrowse("Text file")],
    [sg.Button("Create_Digest")],
    [sg.Txt("Choose file to check digest"), sg.FileBrowse("Message Data")],
    [sg.Txt("Choose file with digest"), sg.FileBrowse("Digest file")],
    [sg.Button("Check_Digest")],
    [sg.Txt("-----------------------------------" * 2)],
    [sg.Txt("Text for GP:"), sg.Input()],
    [sg.Button("GP_Crypt"), sg.Button("GP_Decrypt")],
    [sg.Txt("-----------------------------------" * 2)],
    [sg.Txt("Tekst for MC:"), sg.Input()],
    [sg.Button("MC_Crypt"), sg.Button("MC_Decrypt")],
    [sg.Output(size=(60, 20))],
    [sg.Button("EXIT")],
]

window = sg.Window("Main application", layout)
while True:
    # rozpakowywanie tupli (pythoniznm) - pobieramy dane (values) z
    # formularza i wczytujemy wciśnięty przycisk (event)
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "EXIT"):
        break
    if event == "Create_Digest":
        if not values["Text file"]:
            print("No text file!")
            continue
        message = Message_Digest(values["Text file"])
        digest_file = values["Text file"].split(".")[0] + ".digest"
        digest_value = message.create_digest()
        message.save_digest(digest_file)
        print(f"HEX Digest: {digest_value}")

    if event == "Check_Digest":
        if not values["Digest file"]:
            print("No digest file!")
            continue
        if not values["Message Data"]:
            print("No message file!")
            continue
        message = Message_Digest(values["Message Data"])
        digest_file = values["Digest file"]
        if message.check_digest(digest_file):
            print("Message orginal and OK.")
        else:
            print("Message corrupted or changed!")

    if event == "GP_Crypt":
        if not values[0]:
            print("No value for GP_Crypt")
            continue
        some_cipher = Skaut_Cipher(values[0])
        if some_cipher.encrypt("GP"):
            print("Crypt OK")
        else:
            print("Some Error on crypt.")
        print(f"Encrypted with GP: {some_cipher.return_encrypted()}")

    if event == "GP_Decrypt":
        if not values[0]:
            print("No value for GP_Decrypt")
            continue
        some_cipher = Skaut_Cipher(values[0], direction="D")
        if some_cipher.decrypt("GP"):
            print("Decrypt OK")
        else:
            print("Some Error on decrypt.")
        print(f"Decrypted with GP: {some_cipher.return_decrypted()}")

    if event == "MC_Crypt":
        if not values[1]:
            print("No value for MC_Crypt")
            continue
        some_cipher = Skaut_Cipher(values[1])
        if some_cipher.encrypt("MC"):
            print("Crypt OK")
        else:
            print("Some Error on crypt.")
        print(f"Encrypted with MC: {some_cipher.return_encrypted()}")

    if event == "MC_Decrypt":
        if not values[1]:
            print("No value for MC_Decrypt")
            continue
        some_cipher = Skaut_Cipher(values[1], direction="D")
        if some_cipher.decrypt("MC"):
            print("Decrypt OK")
        else:
            print("Some Error on decrypt.")
        print(f"Decrypted with MC: {some_cipher.return_decrypted()}")


window.close()
