import socket  # noqa: F401
import re
import threading
import os
from utils import get_headers, get_header, get_header_data, get_file, get_file_size, read_file
from concurrent.futures import ThreadPoolExecutor

PORT = 4221
FILES_PATH = "/files_data"
def handle_client(client_socket):
    print("Client being handled !!!!")
    
    
    with client_socket:
        try:
            data = client_socket.recv(1024)
            request = data.decode()

            request_line = request.split("\r\n")[0]
            http_method , uri, http_protocol = request_line.split(" ")

            uri:str

            headers = get_headers(request)

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

            elif (uri == '/user-agent'):

                current_header = get_header(headers, "User-Agent")
                    
                if current_header == None:
                    response = b"HTTP/1.1 400 Bad Request\r\n\r\nMissing User-Agent header"
                else:
                    header_data = get_header_data(current_header)

                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/plain\r\n"
                        f"Content-Length: {len(header_data)}\r\n"
                        "\r\n"
                        f"{header_data}"
                    ).encode("utf-8")
            
            elif (uri.startswith('/files/')):
                file_name = uri[len("/files/"):]
                
                current_file_path = get_file(FILES_PATH,file_name) # Obtener el archivo si existe

                if current_file_path == None:
                    response =b"HTTP/1.1 404 Not Found\r\n\r\n"
                else:
                    file_size = get_file_size(current_file_path)
                    file_data = read_file(current_file_path)

                    headers = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: application/octet-stream\r\n"
                        f"Content-Length: {file_size}\r\n"
                        "\r\n"
                    ).encode('utf-8')

                    response = headers + file_data  # file_data debe ser bytes, no str
            else:
                response =b"HTTP/1.1 404 Not Found\r\n\r\n"
                
            client_socket.sendall(response)

        except Exception as Ex:
            print("Error en el handle client ", Ex)
def main():
    print("Server escuchando en el puerto: ", PORT)
    server_socket = socket.create_server(("::", PORT), family=socket.AF_INET6, reuse_port=True)  #Para ipv6

    with ThreadPoolExecutor(max_workers=50) as executor:
        while True:
            client_socket, addr = server_socket.accept()
            executor.submit(handle_client, client_socket)


if __name__ == "__main__":
    main()
