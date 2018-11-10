import requests

"""Utilities for fucking around with url data
"""


def gen_from_urls(urls: tuple) -> tuple:
    """Returns the length of content, status code, and url from tuple parameter
    """
    for response in (requests.get(url) for url in urls):
        yield len(response.content), response.status_code, response.url
