import json
import jwt
import time
    
def encrypt_jwt(user_id, expire_time):
    now = int(time.time())
    exp = now + int(expire_time)
    data_to_encode = {'user_id': user_id, 'iat': now, 'exp': exp}
    algorithm = "HS256"
    encryption_secret = "A-Live"
    encode = jwt.encode(data_to_encode, encryption_secret, algorithm=algorithm)
    return encode
    
def decrypt_jwt(data):
    algorithm = "HS256"
    encryption_secret = "A-Live"
    decode = jwt.decode(data, encryption_secret, algorithms=[algorithm])
    return decode

def check_expired(expired_time):
    current_time = int(time.time())
    isExpire = True
    if current_time > expired_time:
        isExpire = False
    else:
        isExpire = True
    return isExpire