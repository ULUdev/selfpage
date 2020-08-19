import sys
import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8080
socket.bind((host, port))
print("starting Server")
socket.listen(5)
try:
    print(f"[SERVER] running on: {port}")
    print("[SERVER] stop server with Ctrl-c")
    while True:
        conn, addr = socket.accept()
        data = conn.recv(1024).decode()
        filename = data.split()[1]
        filetype = ""
        print(f"[SERVER] new request: {filename}")
        if filename == "/" or filename == "/index":
            filename = "/sites/index.html"
        if filename.endswith(".html"):
            filetype = "text/html"
        elif filename.endswith(".css"):
            filetype = "text/css"
        elif filename.endswith(".js"):
            filetype = "text/javascript"
        elif filename.endswith(".png"):
            filetype = "image/png"
        conn.send("HTTP/1.0 200 OK\n".encode())
        if filetype == "":
            conn.send("\n".encode())
        else:
            conn.send(f"content-type: {filetype}\n".encode())
        file = filename.split("/", maxsplit=1)[1]
        try:
            if filename.endswith(".png"):
                file = open(file, "rb").read()
            else:
                file = open(file).read()
            conn.send(file.encode())
            
        except:
            conn.send("HTTP/1.0 404\n\nNot found".encode())
        conn.close()
except KeyboardInterrupt:
    print("\n[SERVER] stopping")
    socket.close()
    sys.exit()