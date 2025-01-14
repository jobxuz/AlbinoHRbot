import sqlite3


class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self,chat_id: int, first_name: str,username: str ,date: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(chat_id,first_name ,username, date) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(chat_id,first_name,username,date), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def update_user_lang(self, lang, chat_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE users SET lang=? WHERE chat_id=?
        """
        return self.execute(sql, parameters=(lang, chat_id), commit=True)


    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


    def add_bolim(self,name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO bolim(name) VALUES(?)
        """
        self.execute(sql, parameters=(name,), commit=True)

    def select_all_bolim(self):
        sql = """
        SELECT * FROM bolim
        """
        return self.execute(sql, fetchall=True)


    def delete_bolim(self,name):
        sql = f"""
            DELETE FROM bolim WHERE name=?
        """
        return self.execute(sql, parameters=(name,), commit=True)
    

    def add_ofis(self,name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO ofis(name) VALUES(?)
        """
        self.execute(sql, parameters=(name,), commit=True)

    def select_all_ofis(self):
        sql = """
        SELECT * FROM ofis
        """
        return self.execute(sql, fetchall=True)


    def delete_ofis(self,name):
        sql = f"""
            DELETE FROM ofis WHERE name=?
        """
        return self.execute(sql, parameters=(name,), commit=True)
    

    #-------------------------------------------------------------------------------------------#

    def add_ombor(self,name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO ombor(name) VALUES(?)
        """
        self.execute(sql, parameters=(name,), commit=True)

    def select_all_ombor(self):
        sql = """
        SELECT * FROM ombor
        """
        return self.execute(sql, fetchall=True)


    def delete_ombor(self,name):
        sql = f"""
            DELETE FROM ombor WHERE name=?
        """
        return self.execute(sql, parameters=(name,), commit=True)
    

    #-------------------------------------------------------------------------------------------#

    def add_dokon(self,name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO dokon(name) VALUES(?)
        """
        self.execute(sql, parameters=(name,), commit=True)

    def select_all_dokon(self):
        sql = """
        SELECT * FROM dokon
        """
        return self.execute(sql, fetchall=True)


    def delete_dokon(self,name):
        sql = f"""
            DELETE FROM dokon WHERE name=?
        """
        return self.execute(sql, parameters=(name,), commit=True)



    def add_admin(self,name: str, admin_id: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO admins(name, admin_id) VALUES(?, ?)
        """
        self.execute(sql, parameters=(name, admin_id), commit=True)

    
    def select_all_admin(self):
        sql = """
        SELECT * FROM admins
        """
        return self.execute(sql, fetchall=True)
    


    def select_all_admin_ids(self):
        sql = """
        SELECT admin_id FROM admins
        """
        # Ma'lumotlarni olamiz va faqat bitta ustun qiymatlarini qaytaramiz
        rows = self.execute(sql, fetchall=True)
        return [row[0] for row in rows]


    def delete_admin(self,name):
        sql = f"""
            DELETE FROM admins WHERE name=?
        """
        return self.execute(sql, parameters=(name,), commit=True)




def logger(statement):
    pass
#     print(f"""
# _____________________________________________________
# Executing:
# {statement}
# _____________________________________________________
# """)