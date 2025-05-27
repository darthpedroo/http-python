import os
import pathlib
DIRECTORY_PATH = pathlib.Path().resolve().parent


def get_headers(request:str) -> list[str]:
    """Gets the headers from an http request (should be a string)

    Args:
        request (str): the http request in a string format

    Returns:
        list[str]: The list of the headers
    """

    headers = []

    for index, header in enumerate(request.split('\r\n')):
        if header == "":
            break
        if index == 0:
            continue
        else:
            headers.append(header)
    
    return headers

def get_header(headers_list:list[str], header_name:str)-> str | None:
    
    """Checks if a header is present in a certain list

    Args:
        headers_list (list[str]): List of the headers
        header_name (str): Name of the header to search in the list

    Returns:
        str: The header (if it's present in the request)
        None: If the header is not in the request
    """

    for header in headers_list:
        current_header_name = header.split(":")[0]
        if current_header_name == header_name:
            return header
            
    return None

def get_header_data(header:str)->str:
    """Gets the value field from a header

    Args:
        header (str): A header with proper http format

    Returns:
        str: header value field
    """

    if not is_valid_header(header):
        raise ValueError("Malformed header")

    header_name, value = header.split(":", 1)
    return value.strip().split(" ")[0]

def is_valid_header(header: str) -> bool:
    """Validates whether a given string is a well-formed HTTP header.

    Args:
        header (str): The header string to validate.

    Returns:
        bool: True if the header is valid (has format 'Key: Value'), False otherwise.
    """
    if ":" not in header:
        return False

    key, _, value = header.partition(":")
    return bool(key.strip()) and bool(value.strip())

def concatenate_path(file_path:str)->str:
    """Concatenates a local path with the base dir url

    Args:
        file_path (str): The local path

    Returns:
        str: full path
    """
    return f"{DIRECTORY_PATH}{file_path}"

def get_file(file_path:str, file_name:str)-> str | None:
    """Gets a file from a path based on a name

    Args:
        file_path (str): Path to the folder of files
        file_name (str): File name 

    Returns:
        str | None: 
            Str if the file is in the folder
            None if the file is not in the folder
    """
    full_file_path = concatenate_path(file_path)
    files = os.listdir(full_file_path)


    for file in files:
        if file == file_name:
            return f"{full_file_path}/{file_name}"
    return None

def get_file_size(full_file_path:str):
    return os.path.getsize(full_file_path)

def read_file(full_file_path:str) -> str:
    with open(full_file_path, 'rb') as file: #Tenemos que usar rb en vez de r para leerlo en bytes
        file_data = file.read()
    
    return file_data

def write_file(full_file_path: str, content) -> None:
    """ Creates and writes a file

    Args:
        path (str): path to the desired file
        content (bytes): data to write to the file
    """
    with open(full_file_path, "w") as f:
        f.write(content)

def get_body(request: str) -> str:
    """
    Gets the body from an HTTP request

    Args:
        request (str): http request

    Returns:
        str: Body of the http response
    """
    parts = request.split("\r\n\r\n", 1)  
    return parts[1] if len(parts) > 1 else ""
