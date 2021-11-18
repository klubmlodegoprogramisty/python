# do wykonania w trybie REPL/IDLE
import hashlib
hash = hashlib.new('sha512_256')
with open("message.txt", encoding='UTF-8') as f:
    data = f.read()
data
data_bytes = data.encode()
data_bytes
hash.update(data_bytes)
hash.hexdigest()
hash.digest()
