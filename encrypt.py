from Crypto.Hash import SHA256

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


if __name__ == "__main__":
    task1()