import socket
 
def main():
    host = "127.0.0.1"
    port = 2345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            print(f"Received connection from {addr}")
            while True:
                data = conn.recv(1024)
                print(f"Received {data}")
                if not data:
                    break
                conn.sendall(data)
        

main()