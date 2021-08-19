from mysqldb import database


class Usuario:

    db = database

    def get_usuario_if_exists(self):
        try:
            database.open_connection(self.db)
            
        finally:
            database.close_connection(self.db)
