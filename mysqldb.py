import mysql.connector

class database:
    nome_database = 'aguadatabase'
    nome_user = 'root'
    password = 'toor'

    def cria_db(self):
        """Cria um novo schema no mysql caso ainda não exista"""
        try:
            db = mysql.connector.connect(
                host = "localhost",
                user = self.nome_user,
                password = self.password)
            cursor = db.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.nome_database}")
            # Seleciona db
            cursor.execute(f"USE {self.nome_database} ;")

            # Cria tabela Usuario
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.nome_database}.usuario ("
                "idusuario INT NOT NULL AUTO_INCREMENT,"
                "nome VARCHAR(45) NOT NULL,"
                "PRIMARY KEY (idusuario),"
                "UNIQUE INDEX idusuario_UNIQUE (idusuario ASC) VISIBLE,"
                "UNIQUE INDEX nome_UNIQUE (nome ASC) VISIBLE)")

            # Cria tabela Água
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.nome_database}.agua ("
                "idagua INT NOT NULL AUTO_INCREMENT,"
                "quantidade INT NOT NULL,"
                "usuario_idusuario INT NOT NULL,"
                "PRIMARY KEY (idagua, usuario_idusuario),"
                "UNIQUE INDEX idagua_UNIQUE (idagua ASC) VISIBLE,"
                "INDEX fk_agua_usuario_idx (usuario_idusuario ASC) VISIBLE,"
                "CONSTRAINT fk_agua_usuario"
                " FOREIGN KEY (usuario_idusuario)"
                f" REFERENCES {self.nome_database}.usuario (idusuario)"
                " ON DELETE NO ACTION"
                " ON UPDATE NO ACTION)")
        except mysql.connector.errors.ProgrammingError:
            print('Usuario ou senha incorretos para login no db')
        finally:
            cursor.close()
            db.close()

    def open_connection(self):
        """Abre conexão para db criado"""
        self.db = mysql.connector.connect(
            host = "localhost",
            user = self.nome_user,
            password = self.password)
        self.cursor = self.db.cursor(dictionary=True)
        # Seleciona db
        self.cursor.execute(f"USE {self.nome_database} ;")

    def close_connection(self):
        """Fecha conexão com o db criado"""
        self.cursor.close()
        self.db.close()

    def get_idusuario(self, nome: str) -> int:
        """Obtem o id do usuário atravez do nome. (Já deve ter uma conexão com o db estabelecida"""
        self.cursor.execute(f"SELECT idusuario FROM usuario WHERE nome='{nome}'")
        idusuario = self.cursor.fetchall()
        return idusuario[0]['idusuario']

    def existente(self, nome_usuario='', id_usuario=0) -> bool:
        """Retorna valor booleano para a existência do usuario ou id especificado"""
        try:
            if nome_usuario:
                database.open_connection(self)
                self.cursor.execute(f"SELECT nome FROM usuario WHERE nome='{nome_usuario}';")
                result = self.cursor.fetchall()
            elif id_usuario:
                database.open_connection(self)
                self.cursor.execute(f"SELECT nome FROM usuario WHERE idusuario='{id_usuario}';")
                result = self.cursor.fetchall()
            if result:
                return True
            else:
                return False
        finally:
            database.close_connection(self)

    def get_SELECT(self, id_usuario=0, all_usuarios=True):
        """Disponibiliza dois tipos de SELECTs, usados para gerar o conteúdo do método GET"""
        if id_usuario > 0:
            all_usuarios=False
        try:
            database.open_connection(self)
            if all_usuarios:
                self.cursor.execute(f"SELECT * FROM {self.nome_database}.usuario")
            else:
                self.cursor.execute(f"SELECT quantidade FROM agua WHERE usuario_idusuario={id_usuario};")
            result = self.cursor.fetchall()
            return result
        finally:
            database.close_connection(self)

    def post_INSERT(self, nome: str, quantidade_agua: int):
        """Recebe o usuario e a quantidade de água e cria uma nova entrada no db"""
        try:
            database.open_connection(self)
            self.cursor.execute(f"INSERT INTO usuario(nome) VALUES('{nome}');")
            idusuario = database.get_idusuario(self, nome)
            self.cursor.execute(f"INSERT INTO agua(quantidade, usuario_idusuario) VALUES ({quantidade_agua}, {idusuario});")
            self.db.commit()
        finally:
            database.close_connection(self)

    def put_UPDATE(self, nome: str, quantidade_agua: int):
        """Recebe o usuário e a quantidade de água e atualiza uma entrada no db"""
        try:
            database.open_connection(self)
            idusuario = database.get_idusuario(self, nome)
            self.cursor.execute(f"INSERT INTO agua(quantidade, usuario_idusuario) VALUES ({quantidade_agua}, {idusuario})")
            self.db.commit()
        finally:
            database.close_connection(self)

    def delete_DELETE(self, id: int):
        """Deleta uma entrada no db de acordo com o id especificado"""
        try:
            database.open_connection(self)
            self.cursor.execute(f"DELETE FROM agua WHERE usuario_idusuario=({id});")
            self.cursor.execute(f"DELETE FROM usuario WHERE idusuario={id}")
            self.db.commit()
        finally:
            database.close_connection(self)
