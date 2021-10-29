decrypted_text = "Jawny komunikat"

rotors_setting = [("I", "A"), ("II", "B"), ("III", "C")]
machine = Enigma(
    stecker="AQ BJ",
    rotors=rotors_setting,
    reflector="Reflector B",
    operator=True,
    word_length=5,
    stator="military",
)
machine.set_wheels("ABC")
encrypted_text = machine.parse(decrypted_text)

print("Enrypted is:", encrypted_text)
