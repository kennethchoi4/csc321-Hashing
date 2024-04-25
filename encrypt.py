import time
from Crypto.Hash import SHA256
import random

# number of letters that are different between two strings
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for c1, c2 in zip(s1, s2):
        # print(c1, c2)
        if c1 != c2:
            distance += 1
    # print(distance)
    return distance

def task1():
    # Part A
    hash = SHA256.new()
    user_input = input("Enter a string to hash: ")

    # update the hash with the user input converted to bytes
    hash.update(user_input.encode())
    print(hash.hexdigest())
    
    # Part B
    hash = SHA256.new()
    string1 = "hello"
    string2 = "hellp"
    if (hamming_distance(string1, string2) != 1):
        raise ValueError("Strings must be of hamming distance 1")

    # print the hex digest hash of string1 and string2
    hash.update(string1.encode())
    print(hash.hexdigest())
    hash.update(string2.encode())
    print(hash.hexdigest())

    # Part c: target collisions
    # generate two strings that result in the same hash, but are different

    # create cryptographically safe random number generator
    r = random.SystemRandom()

    # generate a random string
    # string_length = r.randint(1,5)
    string_length = 25
    og_string = ''.join(r.choice("abcdefghijklmnopqrstuvwxyz") for i in range(string_length))

    # get user input for bit domain
    # bit_domain = int(input("Enter the bit domain: "))
    # while bit_domain < 8 and bit_domain > 256:
    #     bit_domain = int(input("Enter the bit domain: "))
    
    # run loop for graph
    times = {}
    for b in range(8, 52, 2):
        flag = True
        # while flag:
        #     x = input("Continue?")
        #     flag = False
        start = time.time()
        hashes = {}
        print(f"\tGenerating strings for collision ({b} bits) ...\n")
        while True:
            s = ''.join(r.choice("abcdefghijklmnopqrstuvwxyz") for i in range(string_length))
            # make sure its not the same string
            while s in hashes.values():
                s = ''.join(r.choice("abcdefghijklmnopqrstuvwxyz") for i in range(string_length))
            
            # get the hash of the string 
            hash = SHA256.new()
            hash.update(s.encode())
            h = hash.hexdigest()
            h = int(h, 16)
            h = bin(h)[:b + 2] # add 2 because of the 0b prefix
            # print(f"String: {s}, hash: {h}")

            
            # truncate
            if h not in hashes:
                hashes[h] = s
            else:
                s2 = hashes[h]
                print("\tCollision found!\n")
                print(f"String 1: {s}, hash: {h}")
                print(f"String 2: {s2}, hash: {h}")
                break
        end = time.time()
        times[b] = end - start
        print(f"Time taken for {b} bits: {end - start} seconds\n")
    print(times)

if __name__ == "__main__":
    task1()
    # x = '0x1111111'
    # print(int(x, 16))
    # print(bin(int(x, 16)))
    # print(bin(int(x, 16)))
