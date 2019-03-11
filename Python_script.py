import hashlib
s=b'hello world'
md5_string=hashlib.md5(s)

res = md5_string.digest()
print(res)