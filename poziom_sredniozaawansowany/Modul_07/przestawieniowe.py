class Skaut_Cipher:
    def __init__(self, text: str, direction: str = "E") -> None:
        """
        direction: E -> for encryption - default
        direction: D -> for decryption
        """
        self.direction = direction
        self.input_text = text.upper() if self.direction == "E" else ""
        self.text_encrypted = text.upper() if self.direction == "D" else ""
        self.text_decrypted = ""
        self.cipher_types = ("GP", "MC")
        self.cipher_type = None
        self.cipher_ok = False
        self.codes_enc_gp = ("G", "D", "R", "P", "L", "K")
        self.codes_dec_gp = ("A", "E", "Y", "O", "U", "I")
        self.codes_enc_mc = ("M", "T", "L", "C", "D", "K")
        self.codes_dec_mc = ("O", "Y", "E", "U", "A", "I")

    def change_letters(self, text: str, codes_in: tuple, codes_out: tuple) -> str:
        returned_text = ""
        for letter in text:
            if letter in codes_in:
                pos = codes_in.index(letter)
                letter = codes_out[pos]
            elif letter in codes_out:
                pos = codes_out.index(letter)
                letter = codes_in[pos]
            returned_text += letter
        return returned_text

    def encrypt(self, cipher: str) -> bool:
        self.cipher_type = cipher
        self.cipher_ok = self.cipher_type in self.cipher_types
        if not self.cipher_ok:
            return False
        if self.direction != "E":
            return False
        if self.cipher_type == "GP":
            self.text_encrypted = self.change_letters(
                self.input_text, self.codes_enc_gp, self.codes_dec_gp
            )
        elif self.cipher_type == "MC":
            self.text_encrypted = self.change_letters(
                self.input_text, self.codes_enc_mc, self.codes_dec_mc
            )
        return True

    def decrypt(self, cipher: str) -> bool:
        self.cipher_type = cipher
        self.cipher_ok = self.cipher_type in self.cipher_types
        if not self.cipher_ok:
            return False
        if self.direction != "D":
            return False
        if self.cipher_type == "GP":
            self.text_decrypted = self.change_letters(
                self.text_encrypted, self.codes_dec_gp, self.codes_enc_gp
            )
        elif self.cipher_type == "MC":
            self.text_decrypted = self.change_letters(
                self.text_encrypted, self.codes_dec_mc, self.codes_enc_mc
            )
        return True

    def output(self) -> None:
        print(f"Input: {self.input_text}")
        print(f"Encrypted: {self.text_encrypted}")
        print(f"Decrypted: {self.text_decrypted}")

    def return_encrypted(self) -> str:
        return self.text_encrypted

    def return_decrypted(self) -> str:
        return self.text_decrypted
