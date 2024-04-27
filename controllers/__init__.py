from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.hash import sha1_crypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")