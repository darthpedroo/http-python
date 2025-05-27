from utils import get_file_size, read_file

def get_file_route(file_path:str | None)->bytes:
    """Gets a file based on a path 

    Args:
        file_path (str): Path to the desired file

    Returns:
        bytes: _description_
    """

    if file_path is None:
        response =b"HTTP/1.1 404 Not Found\r\n\r\n"
    else:
        file_size = get_file_size(file_path)
        file_data = read_file(file_path)

        headers = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/octet-stream\r\n"
        f"Content-Length: {file_size}\r\n"
        "\r\n"
        ).encode('utf-8')
        response = headers + file_data  # file_data debe ser bytes, no str
    return response