import random
from Parametros import Parametros as config

class Individuo ():
    def __init__ ( self , espacos , valores ,limite_espacos , geracao=0, cromossomos=None):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.geracao = geracao
        self.espaco_usado = 0
        self.cromossomo = cromossomos if cromossomos else self.gerar_novo_cromossomo(len(espacos))
        self.nota_avaliacao = self.avaliacao()
    
    # Função para gerar um novo cromossomo
    def gerar_novo_cromossomo(self, tamanho):
        lista_cromossomos = [] # Cria uma lista vazia para armazenar o cromossomo

        for i in range(0, tamanho): # Itera entre 0 a tamanho
             
             valor_aleatorio = random.choice([0,1]) # Gera 0 ou 1

             lista_cromossomos.append(valor_aleatorio) # Adiciona o número à lista do cromossomo

        return lista_cromossomos # Retorna a lista de cromossomos
    

    # Função para avaliar o cromossomo
    def avaliacao(self):
        # Inicializa variáveis
        nota = 0 
        self.espaco_usado = 0
        for i,item in enumerate(self.cromossomo): # Itera sobre o cromossomo usando enumerate para obter o indice e o valor
            if item == 1:
                # Adicionar o valor e o espaço usado ao total
                nota += self.valores[i] 
                self.espaco_usado += self.espacos[i]
        if self.espaco_usado > self.limite_espacos: # Verifica se ultrapassou o limite de espacos
            return 1 
        else:
            return nota 
    
    
    def crossover( self ,outro_individuo ):
        # Cria um corte aleatório
        corte = round(random.random() * len(self.cromossomo))

        # Cria dois novos indivíduos combinando os cromossomos
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        return (
            Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1, self.mutacao(config.taxa_mutacao,filho1)),
            Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1, self.mutacao(config.taxa_mutacao,filho2)) 
        )

    def mutacao(self, taxa_mutacao, cromossomo):
        for i in range(len(cromossomo)): # Itera sobre cada elemento no cromossomo
            if random.randint(0,100) < taxa_mutacao:
                if cromossomo[i] == 1: # Se o elemento atual for 1, troca para 0
                    cromossomo[i] = 0
                else:
                    cromossomo[i] = 1
        return cromossomo
    

    def __str__(self) -> str:
        # Converte a lista do cromossomo para uma string
        cromossomo_str = str(self.cromossomo)
        return cromossomo_str
    

        
    
   