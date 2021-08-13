import mysql.connector

class database:
    nome_database = 'aguadatabase'

    def cria_db(self):
        """Cria um novo schema caso ainda não exista"""
        try:
            aguadb = mysql.connector.connect(
                host = "localhost",
                user = "root2",
                password = "toor")
            cursor = aguadb.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.nome_database}")
            # Seleciona db
            cursor.execute(f"USE {self.nome_database} ;")

            # Cria tabela Água
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.nome_database}.agua ("
                "idagua INT NOT NULL AUTO_INCREMENT,"
                "quantidade INT NOT NULL,"
                " PRIMARY KEY (idagua),"
                "UNIQUE INDEX idagua_UNIQUE (idagua ASC) VISIBLE);")

            # Cria tabela Usuario
            cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.nome_database}.usuario ("
            "idusuario INT NOT NULL AUTO_INCREMENT,"
            "nome VARCHAR(45) NOT NULL,"
            "agua_idagua INT NOT NULL,"
            "PRIMARY KEY (idusuario),"
            "UNIQUE INDEX idusuario_UNIQUE (idusuario ASC) VISIBLE,"
            "UNIQUE INDEX nome_UNIQUE (nome ASC) VISIBLE,"
            "INDEX fk_usuario_agua_idx (agua_idagua ASC) VISIBLE,"
            "CONSTRAINT fk_usuario_agua"
            " FOREIGN KEY (agua_idagua)"
            f" REFERENCES {self.nome_database}.agua (idagua)"
            " ON DELETE NO ACTION"
            " ON UPDATE NO ACTION)")
        finally:
            cursor.close()
            aguadb.close()

