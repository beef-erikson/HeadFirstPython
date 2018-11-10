import requests

"""Demonstrates the difference between using a listcomp and generator
"""

urls = ('http://google.com', 'http://twitter.com', 'http://youtube.com')

# uses listcomp to cycle through urls - note the delay.
for response in [requests.get(url) for url in urls]:
    print(len(response.content), '->', response.status_code, '->', response.url)
print('-------------')


# uses a generator to cycle through urls - processes one at a time
for response in (requests.get(url) for url in urls):
    print(len(response.content), '->', response.status_code, '->', response.url)
