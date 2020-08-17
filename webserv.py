import socket
import sys

def load_img(file):
    with open(file, "rb") as file:
        return file.read()

port = 8080
host = "localhost"
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[SERVER] created socket")
try:
    socket.bind((host, port))
except Exception as e:
    print(f"[SERVER] error occured: {e}")
    sys.exit()
socket.listen(10)
try:
    print(f"[SERVER] listening on port: {port}")
    while True:
        conn, addr = socket.accept()
        print(f"[SERVER] new request: {addr}")
        try:
            data = conn.recv(1024).decode()
            filename = data.split()[1]
            if filename == "/":
                filename = "/index/index.html"
            if ".png" in filename or ".ico" in filename:
                outdat = load_img(filename)
            else:
                file = open(filename[1:])
                outdat = file.read()
                file.close()
            conn.send("HTTP/1.0 200 OK\r\n\r\n".encode())
            #conn.send("content-type: text/html\n".encode())
            for i in range(0, len(outdat)):
                conn.send(outdat[i].encode())
            conn.close()
        except Exception:
            conn.send("404 Not found".encode())
            conn.close()
except KeyboardInterrupt:
    print("\n[SERVER] going down")
    socket.close()
