import sys
import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting
host = "localhost"
port = 8080
socket.bind((host, port))
print("starting Server")

#listening
socket.listen(5)
try:
    print(f"[SERVER] running on: {port}")
    print("[SERVER] stop server with Ctrl-c")
    while True:

        #get data
        conn, addr = socket.accept()
        data = conn.recv(1024).decode()
        filename = data.split()[1]
        filetype = ""

        #routing
        if filename == "/" or filename == "/index" or filename == "/index.html":
            filename = "/pages/index.html"
        elif filename == "/about" or filename == "/about.html":
            filename = "/pages/about.html"
        elif filename == "/projects" or filename == "/projects.html":
            filename = "/pages/projects.html"
        elif filename == "/discord" or filename == "/discord.html":
            filename = "/pages/discord.html"

        #mimetype
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

            #filetype
            if filetype == "":
                filetype = "\n".encode()
            else:
                filetype = f"content-type: {filetype}\n".encode()

            #PNG Images
            if filename.endswith(".png"):
                file = open(file, "rb").read()
                out = file

            #textdocuments
            else:
                file = open(file).read()
                out = file.encode()
                print(f"[SERVER] new request: {filename} 200")

            #sending
            conn.send("HTTP/1.0 200 OK\n".encode())
            conn.send(filetype + "\r\n".encode())
            conn.send(out)

        #Error 404
        except:
            conn.send("HTTP/1.0 404\n\n".encode())
            erpg = open("pages/error.html").read()
            conn.send(erpg.encode())
            print(f"[SERVER] new request: {filename} 404")
        conn.close()

#stopping server
except KeyboardInterrupt:
    print("\n[SERVER] stopping")
    socket.close()
    sys.exit()
