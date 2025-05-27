from utils import write_file

def write_file_route(new_file_path:str, content)->bytes:
    try:
        write_file(new_file_path, content)
        response = (
        "HTTP/1.1 201 Created\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    ).encode("utf-8")

    
    except ArithmeticError as ex:
        response = b"HTTP/1.1 500 Internal server Error\r\n\r\n"

    return response
