from python_enigma import enigma


rotors_setting = [("I", "A"), ("II", "B"), ("III", "C")]
machine = enigma.Enigma(catalog="default", stecker="AQ BJ",
                        rotors=rotors_setting, reflector="Reflector B", operator=True, word_length=5, stator="military")
machine.set_wheels("ABC")

print("""I am going to try to print HI PYTON using the stecker settings
      AQ and BJ and rotors I, II, III from the whermacht set.
      The ringstellungs (pol. ustawienia wirników) 
      are A, B, and C respectively.""")

crypted = machine.parse("hello python")
print(f"Crypted text is: {crypted}")
print("If I feed that back through, it decrypts to:")
machine.set_wheels("ABC")
print(f"Back decrypted: {machine.parse(crypted)}")
