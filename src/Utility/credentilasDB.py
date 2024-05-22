

import os

def credDB():
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']
    db_name = os.environ['DB_NAME']
    db_port = os.environ['DB_PORT']
    db_host = os.environ['DB_HOST']

    if not db_user and not db_pass:
        raise Exception(f"Need to set up db_user and db_pass")
    else:
        cred_info = {
            "DB_USER": db_user,
            "DB_PASS": db_pass,
            "DB_NAME": db_name,
            "DB_PORT": db_port,
            "DB_HOST": db_host
        }
        return cred_info
