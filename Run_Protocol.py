from Receiver import *
from Sender import *
import random
from Crypto.PublicKey import RSA
from Crypto import Random
import ast


def protocol(Sr, senderSet):
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    publickey = key.publickey()

    p = 12009342892403487151
    q = 16745092048479459697
    N = p * q
    g = findGenerator(N)

    for Ss in senderSet:
        sKey = getRandom(1000)
        receiver = Receiver(sKey, g, N, Sr)
        h = receiver.hashReceiver()
        sender = Sender(sKey, N, g, Ss, h)
        senderParameters = sender.computeSender(publickey)
        s = senderParameters[0]
        f = senderParameters[1]
        R = senderParameters[2]
        for i in range(len(Sr)):
            Ri = receiver.checkIntersection(s, f, i, publickey)
            dec_Ri = key.decrypt(ast.literal_eval(str(Ri)))
            dec_R = key.decrypt(ast.literal_eval(str(R)))
            if dec_R == dec_Ri:
                print("There is an intersection with index:", i)

    return 0


rein = random.sample(range(2, 1000), 200)
print("This is a random receiver set of 200 elements (SR):", rein)

print("Enter users number (e.g. 2):")
users = int(input())

start = 1
while start <= users:
    print("User", start, "give your set (e.g 42 122 1337 2021):")
    print("If you want to input a random set with 100 elements, enter 'r' as an input!")
    senInput = input()
    if senInput == "r":
        ranIn = random.sample(range(2, 1000), 100)
        print("SS:", ranIn)
        print("It will take about 5 minutes to finish the execution!")
        protocol(rein, ranIn)
    else:

        senIn = list(map(int, senInput.split()))
        protocol(rein, senIn)
    start += 1

print("Running protocol is done")
