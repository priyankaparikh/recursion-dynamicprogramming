# avoid global variables
# avoid importing ready python libraries
# avoid sending raw strings across the network
import random

class Codec:
    def __init__(self):
        self.length = 6
        self.tiny_url = "http://tinyurl.com/"
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lookup = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        def rand_str():
            rand_chars = []
            for i in xrange(self.length):
                rand_chars.append(self.alphabet[random.randint(0, len(self.alphabet) - 1)])
            return "".join(rand_chars)

        temp = rand_str()
        while temp in self.lookup:
            temp = rand_str()
        self.lookup[temp] = longUrl

        return self.tiny_url + temp


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        return self.lookup[shortUrl[len(self.tiny_url):]]

# codec optimised
class Codec2:
    def __init__(self):
        self.counter = 0
        self.int2url = {}

    tiny = "http://tinyurl.com/"

    def encode(self, longUrl):

        count =  self.counter
        self.counter += 1
        self.int2url[count] = longUrl
        return Codec2.tiny + str(count)

    def decode(self, shortUrl):

        count = int(shortUrl[len(codec2.tiny):])
        return self.int2url[count]
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
