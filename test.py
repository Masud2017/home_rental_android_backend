from utils.util import get_role_object_by_role_name,save_file_to_disk
from fastapi import UploadFile,File

if __name__ == "__main__":
    file = open("testsTestAuthServices.py")
    up = File(file)
    aa = UploadFile(up)
    file_name = save_file_to_disk(aa,"msmasud578@gmail.com")

    print(file_name)