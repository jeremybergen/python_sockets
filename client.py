import socket

host = "127.0.0.1"
port = 2345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # (host, port)
        # [host, port]
        # s.send(b'Hello world\r\n')
        send_string1 = bytearray([0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20])
        send_string2 = bytearray([0x77, 0x6f, 0x72, 0x6c, 0x64, 0x0d, 0x0a])
        mynum = 12345
        print(f"{mynum.to_bytes(4, 'little')}")

        mystring = "This is my string"
        # s.send(send_string2 + send_string1)
        s.send(mystring.encode())
        data = s.recv(1024)
        print(f"Received back from server {data.decode('utf-8')}")

main()