import hashlib

def create_rainbow_table():
    with open('wordlist.txt') as f:
        passwords = [x.strip('\n') for x in f.readlines()]

    passwords_hashes = {hashlib.md5(x.encode()).hexdigest(): x for x in passwords}

    return passwords_hashes

def decrypt_md5_hash(md5_hash):
    rainbow_table = create_rainbow_table()
    if md5_hash in rainbow_table:
        return rainbow_table[md5_hash]
    else:
        return "Password not found in the dictionary"

md5_hash = "ae2b8987e92cfa61159724dcc336540c"
password = decrypt_md5_hash(md5_hash)
print("The password is:", password)
