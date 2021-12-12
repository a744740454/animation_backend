import hashlib


def hash_password(password):
    hl = hashlib.md5()

    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(password.encode(encoding='utf-8'))
    return hl.hexdigest()
