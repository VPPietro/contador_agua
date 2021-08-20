import mysql.connector

class database:
    nome_database = 'aguadatabase'
    nome_user = 'root'
    password = 'toor'

    def open_connection(self, criadb=False, dictionary=True):
        """Abre conexão para db criado"""
        self.db = mysql.connector.connect(
            host = "localhost",
            user = self.nome_user,
            password = self.password)
        self.cursor = self.db.cursor(dictionary=dictionary)
        if criadb:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.nome_database}")
        # Seleciona db
        self.cursor.execute(f"USE {self.nome_database} ;")

    def close_connection(self):
        """Finaliza conexão com o db criado"""
        self.cursor.close()
        self.db.close()

    def cria_db(self):
        """Cria um novo schema no mysql caso ainda não exista"""
        try:
            # Abre conexão com criação de schema
            database.open_connection(self, criadb=True)

            # Cria tabela Usuario
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.nome_database}.usuario ("
                "idusuario INT NOT NULL AUTO_INCREMENT,"
                "nome VARCHAR(45) NOT NULL,"
                "login VARCHAR(32) NOT NULL,"
                "PRIMARY KEY (idusuario),"
                "UNIQUE INDEX idusuario_UNIQUE (idusuario ASC) VISIBLE,"
                "UNIQUE INDEX nome_UNIQUE (nome ASC) VISIBLE,"
                "UNIQUE INDEX login_UNIQUE (login ASC) VISIBLE)")

            # Cria tabela Água
            self.cursor.execute(
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
            print('Erro de conexão com a db ou sintaxe do comando')
        finally:
            database.close_connection(self)

    def get_usuario_if_exists(self, hash='') -> str:
        """Obtem o hash do login e retorna caso exista se não só retorna None. (Já deve ter uma conexão com o db estabelecida)"""
        result = self.cursor.execute(f"SELECT idusuario, nome FROM usuario WHERE login='{hash}'")
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return False

    def get_SELECT(self, id_usuario: int):
        """Disponibiliza todos os inputs do usuario informado (deve estar conectado na db"""
        self.cursor.execute(f"SELECT quantidade FROM {self.nome_database}.agua WHERE usuario_idusuario={id_usuario};")
        return self.cursor.fetchall()

    def post_INSERT(self, id_usuario: int, quantidade_agua: int):
        """Recebe o usuario e a quantidade de água e cria uma nova entrada no db"""
        self.cursor.execute(f"INSERT INTO agua(quantidade, usuario_idusuario) VALUES ({quantidade_agua}, {id_usuario});")
        self.db.commit()

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
