from utils import *
import hashlib


class Receiver:

    def __init__(self, secretKey, g, N, Sr):
        self.N = N
        self.Sr = Sr
        self.secretKey = secretKey
        self.g = g
        self.PRF_Primes = prf(self.secretKey, self.Sr)
        self.r = getRandom(self.N)

    def hashReceiver(self):

        tmp = pow(int(self.g), self.r, self.N)
        for i in self.PRF_Primes:
            tmp = pow(tmp, i, self.N)
        h = tmp
        return h

    def checkIntersection(self, s, f, i, publickey):

        primesI = self.PRF_Primes
        reV = primesI[i]
        del primesI[i]
        tmp = pow(f, self.r, self.N)
        for j in primesI:
            tmp = pow(tmp, j, self.N)
        secArg = tmp
        primesI.insert(i, reV)
        #############################
        sByte = str(s).encode('utf-8')
        msg = str(secArg).encode('utf-8')
        ha = hashlib.sha3_256()
        ha.update(msg + sByte)
        extractor = int(ha.hexdigest(), 16)
        ##############################
        encExtractor = publickey.encrypt(extractor, 32)
        return encExtractor
