# Implement a URL shortener with the following methods:
# shorten(url), which shortens the url into a 
# six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string 
# into the original url. If no such shortened string exists, return null.

import hashlib

class shortUrl:
    def __init__(self):
        self.url_map = dict()
        self.m = hashlib.sha256
        self.name = "http://short.pl/"

    def shorten(self, url):
        sha = self.m(url.encode()).hexdigest()
        hash = sha[:6]
        self.url_map[hash] = url
        return self.name + hash

    def restore(self, short_url):
        hash = short_url.replace(self.name, "")
        return self.url_map[hash]