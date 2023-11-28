from Individuo import Individuo
import random

class AlgoritmoGenetico ():
    def __init__ (self ,tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao # Tamanho da população
        self.populacao = [] # Lista com os indivíduos da população
        self.geracao = 0 # Geração atual do algoritmo genético
        self.melhor_solucao = 0 # Melhor solução encontrada pelo algoritmo genético até o momento
        self.volume_total = 0 # Volume total ocupado pelos itens na melhor solução encontrada

    # Inicializa a população
    def inicializa_populacao( self, espacos, valores,limite_espacos ):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos,valores,limite_espacos))
            self.melhor_solucao = self.populacao[0]

    # Ordena a população do algoritmo genético pela nota de avaliação, 
    # em ordem decrescente
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, key=lambda populacao : populacao.nota_avaliacao, reverse=True)
    
    # Atualiza a melhor solução encontrada pelo algoritmo genético, 
    # se o indivíduo passado como argumento tiver nota de avaliação melhor do que a melhor solução atual
    def melhor_individuo( self, individuo ):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo

    # Calcula a soma total das notas de avaliação da população
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
    # Calcula o volume total ocupado pelos itens na população
    def soma_volume(self):
        soma_volume = 0
        for individuo in self.populacao:
            soma_volume += individuo.espaco_usado
        return soma_volume
    
    # Seleciona dois pais para o cruzamento
    def selecionar_pais(self):
        pais = [] # Cria uma lista vazia para armazenar os pais selecionados
        for i in range(2): # Itera duas vezes para selecionar dois pais
            pai = None # Inicializa a variável de pai selecionado
            soma_avaliacao = self.soma_avaliacoes() # Calcula a soma total das avaliações da população
            valor_aleatorio = random.uniform(0, soma_avaliacao) # Gera um valor aleatório dentro da faixa da soma total das avaliações
            soma_total = 0
            for individuo in self.populacao:
                soma_total += individuo.nota_avaliacao
                if soma_total > valor_aleatorio:
                    pai = individuo
                    break
            pais.append(pai)
        return pais
