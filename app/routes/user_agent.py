from utils import get_header_data

def user_agent(user_agent_header:str | None) -> bytes:
    """Returns the user agent based on the header

    Args:
        user_agent_header (str): User Agent Header

    Returns:
        bytes: _description_
    """
    
    if user_agent_header is None:
        response = b"HTTP/1.1 400 Bad Request\r\n\r\nMissing User-Agent header"
    else:
        header_data = get_header_data(user_agent_header)

        response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(header_data)}\r\n"
        "\r\n"
        f"{header_data}"
        ).encode("utf-8")

    return response