import socket

SECRET_KEY = b"my_secret_key"  # Keep this the same on both devices

def xor_encrypt_decrypt(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

HOST = "0.0.0.0"
PORT = 45678

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for a secure connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    decrypted_msg = xor_encrypt_decrypt(data, SECRET_KEY).decode()
    print("Stealth Message:", decrypted_msg)

conn.close()
