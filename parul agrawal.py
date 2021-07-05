import hashlib
text = input("Enter a string data")
md= hashlib.md5(text.encode())
print(md.digest())