from modelo import*
SQL_BUSCA = 'SELECT Id, Atividade, Status from Listas'
SQL_DELETA = 'DELETE FROM Listas WHERE Id = %s'
SQL_ATUALIZAR = 'UPDATE Listas SET Atividade = %s, Status = %s WHERE Id = %s'
SQL_POR_ID = 'SELECT Id, Atividade, Status FROM Listas WHERE Id = %s'
SQL_CRIA = 'INSERT INTO Listas (Atividade, Status) VALUES (%s, %s)'

class DAO:
    def __init__(self, db):
        self.__db = db

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA)
        atividade = traduz_atividade(cursor.fetchall())
        return atividade

    def apagar(self,ide):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETA, (ide,))
        self.__db.connection.commit()

    def busca_por_id(self, ide):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_POR_ID, (ide,))
        tupla = cursor.fetchone()
        return Modelagem(tupla[1], tupla[2], ide=tupla[0])

    def salvar(self,lista):
        cursor = self.__db.connection.cursor()
        if lista.ide:
            cursor.execute(SQL_ATUALIZAR, (lista.atividade,lista.status,lista.ide))
        else:
            cursor.execute(SQL_CRIA, (lista.atividade,lista.status))
            print(lista.ide)
            lista.ide = cursor.lastrowid
        self.__db.connection.commit()
        return lista

def traduz_atividade(atividades):
    def cria_atividade_com_tupla(tupla):
        return Modelagem(tupla[1],tupla[2],ide=tupla[0])
        
    return list(map(cria_atividade_com_tupla, atividades))   

