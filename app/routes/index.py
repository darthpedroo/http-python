def index() -> bytes:
    """Returns index function

    Returns:
        bytes: http response
    """
    response = b"HTTP/1.1 200 OK\r\n\r\n"
    return response