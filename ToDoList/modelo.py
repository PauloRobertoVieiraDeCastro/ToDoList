class Modelagem:
    def __init__(self,atividade,status,ide=None):
        #self.datas = datas
        self.ide = ide
        self.atividade = atividade
        self.status = status

'''
def cria_atividade_com_tupla(tupla):
    return Modelagem(tupla[0],tupla[1])
        

a = [('comer cu','nao feito'),('bater bronha','nao feito')] 
print(list(map(cria_atividade_com_tupla, a))[1].status)    

'''
