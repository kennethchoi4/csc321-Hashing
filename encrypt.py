from Crypto.Hash import SHA256

def task1():
    hash = SHA256.new()
    user_input = input("Enter a string to hash: ")

    # update the hash with the user input converted to bytes
    hash.update(user_input.encode())
    print(hash.hexdigest())


if __name__ == "__main__":
    task1()