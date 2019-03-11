s = b"Hello, world!"

print(s)

md5string = hashlib.md5.update(s)

result = md5string.md5.digest()

print(result)
