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

