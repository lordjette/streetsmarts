#TODO: eto ang gagamitin mo :fire: 🔥 🔥:fire::fire::fire::fire:
import hmac
import hashlib
import base64
from passlib.context import CryptContext

text_type = str
salt = "thisissalt"
SECRET_KEY = 'e3be6b00b6e7f53754498e54813ea190'

def get_pw_context ():
  pw_hash = 'pbkdf2_sha512'
  schemes = ['bcrypt', 'des_crypt', 'pbkdf2_sha256', 'pbkdf2_sha512', \
      'sha256_crypt', 'sha512_crypt', "md5_crypt", 'plaintext']
  deprecated = ['auto']
  return CryptContext (schemes=schemes, default= pw_hash, deprecated=deprecated)

def encode_string(string):
  if isinstance(string, text_type):
    string = string.encode('utf-8')
  return string

def get_hmac (password):
  h = hmac.new(encode_string(salt),  encode_string(password), hashlib.sha512)
  return base64.b64encode(h.digest())

def verify_password (password, hash):
  return get_pw_context().verify(get_hmac(password), hash)

# Finally
gh= get_hmac('123456')
print('This is gh:', gh)
print('The length of gh is: ', len(gh))
vp = verify_password ("123456", gh)
print (vp)

gwc = get_pw_context()
print (gwc.default_scheme())
print (gwc.hash("123456"))


#need to install bycrypt to use bcrypt --> pip isntall bcrypt