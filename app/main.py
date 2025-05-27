import socket  # noqa: F401
from utils import get_headers, get_header, get_header_data, get_file, get_file_size, read_file, concatenate_path, get_body
from routes.index import index
from routes.echo import echo
from routes.user_agent import user_agent
from routes.get_file_route import get_file_route
from routes.write_file_route import write_file_route
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
                response = index()
                
            elif (uri.startswith("/echo/")):
                
                echo_value = uri[len("/echo/"):]
                response = echo(echo_value)

            elif (uri == '/user-agent'):

                user_agent_header = get_header(headers, "User-Agent")
                response = user_agent(user_agent_header)
            
            elif (uri.startswith('/files/') and http_method == "POST"):
                print(request)
                body = get_body(request)
                
                new_file_name = uri[len('/files/'):]
                new_file_path = f"{FILES_PATH}/{new_file_name}"
                full_path = concatenate_path(new_file_path)
                response = write_file_route(full_path, body)
                
            elif (uri.startswith('/files/') and http_method == "GET"):

                file_name = uri[len("/files/"):]
                current_file_path = get_file(FILES_PATH,file_name) 
                response = get_file_route(current_file_path)

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
