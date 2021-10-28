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
