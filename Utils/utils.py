# encoding:utf-8
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex

AesKey = 'abcabcabc2020123'
AesVi = '9847473127393676'


# @base_exceptions()
def encrypt(password):
    """
    密码加密 AES
    """
    password = password or ''  # 防止传入的是None
    aes = AES.new(AesKey.encode('utf8'), AES.MODE_CBC, AesVi.encode('utf8'))
    context_encode = password.encode('utf-8')
    num = AES.block_size - (len(context_encode) % AES.block_size)
    ciphertext = aes.encrypt(context_encode + bytes([0]) * num)
    return base64.b64encode(b2a_hex(ciphertext)).decode('utf8')


# @base_exceptions()
def decrypt(password):
    """
    密码解密
    """
    password = password or ''  # 防止传入的是None
    missing_padding = 4 - len(password) % 4
    if missing_padding:
        password += '=' * missing_padding
    cryptor = AES.new(AesKey.encode('utf8'), AES.MODE_CBC, AesVi.encode('utf8'))
    aesStr = cryptor.decrypt(a2b_hex(base64.b64decode(password.encode('utf8'))))
    return bytes.decode(aesStr).rstrip('\0')
