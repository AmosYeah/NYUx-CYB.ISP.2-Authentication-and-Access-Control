import os, hashlib

def salted_password(pw, salt = os.urandom(32).hex()):
    return hashlib.sha256(pw.encode()+salt.encode()).hexdigest()

#salted_password = salted_password(input("Enter your password: "))
#print(salted_password)