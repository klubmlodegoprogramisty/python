encrypted_text = "PTBOV ZSXUW KKRNH ABFOC WRWEF PJPVN THX"

rotors_settings = {1: [("I", "A"), ("II", "B"), ("III", "C")],
                    2: [("I", "A"), ("II", "C"), ("III", "B")],
                    3: [("I", "B"), ("II", "A"), ("III", "C")],
                    4: [("I", "B"), ("II", "C"), ("III", "A")],
                    5: [("I", "C"), ("II", "B"), ("III", "A")],
                    6: [("I", "C"), ("II", "A"), ("III", "B")]}

reflectors = {1: "Reflector B Thin", 2: "Reflector C Thin", 3: "Reflector A",
            4: "Reflector B", 5: "Reflector C"}
combination_number = 0

for rotors_setting in rotors_settings:
    for reflector in reflectors:
        combination_number += 1
        machine = Enigma(
            stecker="AQ BJ",
            rotors=rotors_settings[rotors_setting],
            reflector=reflectors[reflector],
            operator=True,
            word_length=5,
            stator="military",
        )
        machine.set_wheels("ABC")
        decrypted_text = machine.parse(encrypted_text)

        print("Combination:", combination_number)
        print("Decrypted is:", decrypted_text)
        print("Rotors setting:", rotors_settings[rotors_setting])
        print("Reflector:", reflectors[reflector])
        print("-----------------------------------------------------------")
