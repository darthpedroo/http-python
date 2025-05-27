import socket  # noqa: F401
import re


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    

    while True:
        client_socket, addr = server_socket.accept() # wait for client
        with client_socket:
            data = client_socket.recv(1024)
            request = data.decode()

            request_line = request.split("\r\n")[0]

            method , uri, protocol = request_line.split(" ")
            
            if (uri == "/"):
                response = b"HTTP/1.1 200 OK\r\n\r\n"
            
            elif (uri.startswith("/echo/")):

                echo_value = uri[len("/echo/"):]
                response_body = echo_value

                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain\r\n"
                    f"Content-Length: {len(response_body)}\r\n"
                    "\r\n"
                    f"{response_body}"
                ).encode('utf-8')

            else:
                response =b"HTTP/1.1 404 Not Found\r\n\r\n"
            
            client_socket.sendall(response)

if __name__ == "__main__":
    main()
