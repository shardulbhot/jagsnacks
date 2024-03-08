from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():

    def bcryptpwd(pwd:str):
        return pwd_cxt.hash(pwd)

    def verify(hash_pwd:str,plain_pwd:str):
        return pwd_cxt.verify(plain_pwd,hash_pwd)

