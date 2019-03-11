import hashlib


s = b"Hello, world!"

print(s)


hash_func = hashlib.md5()
hash_func.update(s)
print(hash_func.digest())
