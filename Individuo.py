import random
from Parametros import Parametros as config

class Individuo ():
    def __init__ ( self , espacos , valores ,limite_espacos , geracao=0, cromossomos=None):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.geracao = geracao
        self.espaco_usado = 0
        self.cromossomo = cromossomos if cromossomos else self.criar_cromossomo(len(espacos))
        self.nota_avaliacao = self.avaliacao()
    
    def criar_cromossomo(self, tamanho):
        lista_cromossomo = [] # Cria uma lista vazia para armazenar o cromossomo

        for i in range(0, tamanho): # Itera entre 0 a tamanho
             
             result = random.choice([0,1]) # Gera 0 ou 1

             lista_cromossomo.append(result) # Adiciona o número à lista do cromossomo

        return lista_cromossomo
    

    def avaliacao(self):
        nota = 0
        self.espaco_usado = 0
        for index,item in enumerate(self.cromossomo):
            if item == 1:
                nota += self.valores[index]
                self.espaco_usado += self.espacos[index]
        if self.espaco_usado > self.limite_espacos:
            return 1
        return nota
    

    def crossover( self ,outro_individuo ):
        corte = round(random.random() * len(self.cromossomo))
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        return (
            Individuo( self.espacos, self.valores ,self.limite_espacos ,self.geracao + 1,self.mutacao(config.taxa_mutacao,filho1)),
            Individuo( self.espacos ,self.valores ,self.limite_espacos ,self.geracao + 1,self.mutacao(config.taxa_mutacao,filho2)) 
        )

    def mutacao( self ,taxa_mutacao, cromossomo):
        for i in range(len(cromossomo)):
            if random.randint(0,100) < taxa_mutacao:
                if cromossomo[i] == 1:
                    cromossomo[i] = 0
                else:
                    cromossomo[i] = 1
        return cromossomo
    # converte objeto para uma str
    def __str__(self) -> str:
        return self.cromossomo.__str__()
    

        
    
   