import hashlib
import secrets

def toHash(string, salt):
    hash = hashlib.sha3_256()
    hash.update(string)
    hash.update(salt)

    hash_string = hash.hexdigest()
    return hash_string 

def createSalt(length):
    salt = secrets.token_bytes(length)
    salt_hex = salt.hex()
    return salt_hex



with open("data_storage/user.db", 'r', encoding='UTF-8') as database_file:
    user_data = database_file.read()
salt = createSalt(16)
print(toHash(user_data, salt))



