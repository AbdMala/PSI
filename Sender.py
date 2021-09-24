from utils import *
import hashlib


class Sender:
    def __init__(self, secretKey, N, g, w, h):
        self.N = N
        self.w = w
        self.h = h
        self.g = g
        self.secretKey = secretKey

    def computeSender(self, publickey):
        """

        :return: returns a list composed of s, f, Ext
        """
        primes = prf(self.secretKey, [self.w])

        Roh = getRandom(self.N)
        s = getRandom(self.N)

        Fs = pow(int(self.g), Roh, self.N)
        f = pow(Fs, primes[0], self.N)

        hRoh = pow(int(self.h), Roh, self.N)

        #######################
        sByte = str(s).encode('utf-8')
        msg = str(hRoh).encode('utf-8')
        h = hashlib.sha3_256()
        h.update(msg + sByte)
        Ext = int(h.hexdigest(), 16)
        ########################
        encExt = publickey.encrypt(Ext, 32)
        result = [s, f, encExt]
        return result
