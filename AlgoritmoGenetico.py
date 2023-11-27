from Individuo import Individuo
import random

class AlgoritmoGenetico ():
    def __init__ (self ,tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.volume_total = 0

    def inicializa_populacao( self, espacos, valores,limite_espacos ):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos,valores,limite_espacos))
            self.melhor_solucao = self.populacao[0]

    def ordena_populacao(self):
        self.populacao = sorted( self.populacao, key = lambda populacao : populacao.nota_avaliacao ,reverse = True)
    
    def melhor_individuo( self, individuo ):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo

    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
    def soma_volume(self):
        soma_volume = 0
        for individuo in self.populacao:
            soma_volume += individuo.espaco_usado
        return soma_volume
    
    def seleciona_pais(self):
        pais = []
        for _ in range(2):
            pai = None
            soma_avaliacao = self.soma_avaliacoes()
            valor_sorteado = random.uniform(0, soma_avaliacao)
            soma = 0
            for individuo in self.populacao:
                soma += individuo.nota_avaliacao
                if soma > valor_sorteado:
                    pai = individuo
                    break
            pais.append(pai)
        return pais
