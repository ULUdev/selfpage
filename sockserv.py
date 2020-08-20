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
        if filename == "/" or filename == "/index":
            filename = "/sites/index.html"
        elif filename == "/about":
            filename = "/sites/about.html"
        elif filename == "/projects":
            filename = "/sites/projects.html"
        if filename.endswith(".html"):
            filetype = "text/html; charset=UTF-8"
        elif filename.endswith(".css"):
            filetype = "text/css; charset=UTF-8"
        elif filename.endswith(".js"):
            filetype = "text/javascript; charset=UTF-8"
        elif filename.endswith(".png"):
            filetype = "image/png"
        file = filename.split("/", maxsplit=1)[1]
        try:
            if filetype == "":
                filetype = "\n".encode()
            else:
                filetype = f"content-type: {filetype}\n".encode()
            if filename.endswith(".png"):
                file = open(file, "rb").read()
                out = file
            else:
                file = open(file).read()
                out = file.encode()
                print(f"[SERVER] new request: {filename} 200")
            conn.send("HTTP/1.0 200 OK\n".encode())
            conn.send(filetype)
            conn.send(out)
        except:
            conn.send("HTTP/1.0 404\n\n".encode())
            erpg = open("sites/error.html").read()
            conn.send(erpg.encode())
            print(f"[SERVER] new request: {filename} 404")
        conn.close()
except KeyboardInterrupt:
    print("\n[SERVER] stopping")
    socket.close()
    sys.exit()