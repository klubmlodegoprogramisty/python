import hashlib


class Message_Digest:
    def __init__(self, message_file: str):
        self.hash = None
        self.hexdigest = None
        self.bytedigest = None
        self.ready = False
        self.error = ""
        try:
            with open(message_file, encoding="UTF-8") as file:
                self.data = file.read()
                self.bytes_data = self.data.encode()
            self.ready = True
        except Exception as e:
            self.error = f"Error on open -> {e}"

    def create_digest(self) -> str:
        if not self.ready:
            return "Not ready"
        self.hash = hashlib.new("sha512_256")
        self.hash.update(self.bytes_data)
        self.hexdigest = self.hash.hexdigest()
        self.bytedigest = self.hash.digest()
        return self.hexdigest.upper()

    def show_error(self) -> str:
        e = self.error
        self.error = ""
        return e

    def get_hexdigest(self) -> str:
        if not self.hexdigest:
            return "Not ready"
        return self.hexdigest.upper()

    def get_bytedigest(self) -> bytes:
        if not self.byedigest:
            return "Not ready"
        return self.bytedigest

    def save_digest(self, digest_file: str) -> bool:
        if not self.hexdigest:
            return False
        try:
            with open(digest_file, mode="w") as file:
                file.write(self.get_hexdigest())
        except Exception as e:
            self.error = f"Error on save -> {e}"
            return False
        return True

    def check_digest(self, digest_file: str) -> bool:
        with open(digest_file, encoding="UTF-8") as file:
            hexdigest = file.read()
        return self.create_digest() == hexdigest


# testowanie - tworzymy plik, zapisujemy skrót
# potem weryfikujemy plik ze skrótem
# na końcu tworzymy plik identyczny tylko z jedną dodatkową spacją
# i też weryfikujemy w środowisku IDLE REPL
# >>> hash_file = Message_Digest("message.txt")
# >>> hash_file.create_digest()
# '0FE45452D72B31469A9BCBB8E5DD188CD4D8E0A856A325C0F0D7E85DECF20EC6'
# >>> hash_file.save_digest("message.digest")
# True
# >>> hash_file.check_digest("message.digest")
# True
# >>> new_file = Message_Digest("message_2.txt")
# >>> new_file.check_digest("message.digest")
# False

# skrypt do wykonania :
hash_file = Message_Digest("message.txt")
hex_digest = hash_file.create_digest()
print(f"Created: {hex_digest}")
if hash_file.save_digest("message.digest"):
    print("Digest saved")
    d_saved = True
else:
    print(f"Oopps: {hash_file.show_error()} ")
    d_saved = False

if d_saved:
    check_file_1 = Message_Digest("message.txt")
    check_file_2 = Message_Digest("message_2.txt")
    checked_1 = check_file_1.check_digest("message.digest")
    checked_2 = check_file_2.check_digest("message.digest")
    print(f"File message.txt identical: {checked_1}")
    print(f"File message_2.txt identical: {checked_2}")

# efekt działania:
# Created: 0FE45452D72B31469A9BCBB8E5DD188CD4D8E0A856A325C0F0D7E85DECF20EC6
# Digest saved
# File message.txt identical: True
# File message_2.txt identical: False
