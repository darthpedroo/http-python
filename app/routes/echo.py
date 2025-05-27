def echo(echo_value: str) -> bytes:
    """Returns a response with a value

    Args:
        echo_value (str): The value that is passed to the echo function to render

    Returns:
        bytes: http response
    """
    
    response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/plain\r\n"
                        f"Content-Length: {len(echo_value)}\r\n"
                        "\r\n"
                        f"{echo_value}"
                    ).encode('utf-8')
    return response