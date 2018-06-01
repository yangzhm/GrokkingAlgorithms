import hashlib


def passwordmd5(password):
    newpass = password + '_salt'
    md5 = hashlib.md5()
    md5.update(newpass.encode())
    return md5.hexdigest()


print('123456 -> ', passwordmd5("123456"))
print('654321 -> ', passwordmd5("654321"))
print('666666 -> ', passwordmd5("666666"))