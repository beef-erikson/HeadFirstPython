from url_utils import gen_from_urls
from pprint import pprint

"""Generates a dictionary of urls and response content length
"""

urls = ('http://google.com', 'http://twitter.com', 'http://youtube.com')

# Example of function's full use
for response_length, status, url in gen_from_urls(urls):
    print(response_length, '->', status, '->', url)
print('-------')


# Create dictionary with key being url and value being length of content
urls_length = {url: size for size, _, url in gen_from_urls(urls)}

pprint(urls_length)
