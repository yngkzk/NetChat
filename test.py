import hashlib

password = "12345"
hash = hashlib.md5(password.encode("utf-8"))
print(hash)

hash_string = hash.hexdigest()
print(hash_string)