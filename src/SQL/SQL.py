

class SQL_statements:

    def SQL_get_random_user(self):
        return f"SELECT * FROM users WHERE `group`='APG777' order by id desc limit 100;"

    def SQL_get_user_by_email(self, email):
        if not email:
            raise Exception(f"email must be provided")
        else:
            return f"SELECT * FROM users WHERE `email`='{email}';"



