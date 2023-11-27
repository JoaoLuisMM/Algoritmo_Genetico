from AlgoritmoGenetico import AlgoritmoGenetico
from Parametros import Parametros as config
from Produto import Produto
from matplotlib import pyplot as plt

# Lista de produtos
produtosLista  = [
     {'nome': "Item 1"  , 'volume': 1.11 , 'valor' : 4.75 },
     {'nome': "Item 2"  , 'volume': 1.25 , 'valor' : 8.00 },
     {'nome': "Item 3"  , 'volume': 1.67 , 'valor' : 5.50 },
     {'nome': "Item 4"  , 'volume': 1.67 , 'valor' : 3.50 },
     {'nome': "Item 5"  , 'volume': 1.25 , 'valor' : 1.50},
     {'nome': "Item 6"  , 'volume': 1.46 , 'valor' : 4.50},
     {'nome': "Item 7"  , 'volume': 0.9  , 'valor' : 4.50 },
     {'nome': "Item 8"  , 'volume': 1.00 , 'valor' : 3.75 },
     {'nome': "Item 9"  , 'volume': 1.54 , 'valor' : 11.50 },
     {'nome': "Item 10" , 'volume': 1.75 , 'valor' : 10.00 },
     {'nome': "Item 11" , 'volume': 1.33 , 'valor' : 7.50 },
     {'nome': "Item 12" , 'volume': 0.33 , 'valor' : 6.00 },
     {'nome': "Item 13" , 'volume': 2.22 , 'valor' : 3.00 },
     {'nome': "Item 14" , 'volume': 3.24 , 'valor' : 4.50 },
     {'nome': "Item 15" , 'volume': 1.00 , 'valor' : 23.00},
     {'nome': "Item 16" , 'volume': 2.50 , 'valor' : 1.30},
     {'nome': "Item 17" , 'volume': 1.50 , 'valor' : 3.14},
     {'nome': "Item 18" , 'volume': 5.77 , 'valor' : 1.41},
     {'nome': "Item 19" , 'volume': 1.23 , 'valor' : 5.22},
     {'nome': "Item 20" , 'volume': 4.50 , 'valor' : 8.10},
     {'nome': "Item 21" , 'volume': 6.70 , 'valor' : 1.40},
     {'nome': "Item 22" , 'volume': 1.20 , 'valor' : 2.25},
     {'nome': "Item 23" , 'volume': 0.44 , 'valor' : 0.50},
     {'nome': "Item 24" , 'volume': 1.33 , 'valor' : 2.33},
     {'nome': "Item 25" , 'volume': 1.40 , 'valor' : 1.75},
     {'nome': "Item 26" , 'volume': 4.63 , 'valor' : 9.50},
     {'nome': "Item 27" , 'volume': 6.22 , 'valor' : 3.10},
     {'nome': "Item 28" , 'volume': 0.45 , 'valor' : 2.25},
     
]

# Cria uma lista de objetos Produto
produtos = [Produto(item['nome'], item['valor'], item['volume']) for item in produtosLista]

# Cria uma lista de espaços (volume)
espacos = [item['volume'] for item in produtosLista]

# Cria uma lista de valores(preços)
valores = [item['valor'] for item in produtosLista]

# Instancia um objeto AlgoritmoGenetico
algoritmo_generico = AlgoritmoGenetico(config.numero_individuos_populacao)

# Inicializa a população
algoritmo_generico.inicializa_populacao(espacos,valores,config.limite_espaco_mochila)

populacaoInicial = algoritmo_generico.populacao

melhores = []


for _ in range(config.numero_geracao):
    algoritmo_generico.ordena_populacao()

    melhor_da_geracao = algoritmo_generico.populacao[0]
    melhores.append(melhor_da_geracao)

    algoritmo_generico.melhor_individuo(melhor_da_geracao)

    soma_avaliacao = algoritmo_generico.soma_avaliacoes()

    nova_populacao = []

    for _ in range(0, algoritmo_generico.tamanho_populacao, 2):
        pais = algoritmo_generico.seleciona_pais()
        filhos = pais[0].crossover(pais[1])
        
        for filho in filhos:
            nova_populacao.append(filho)

    algoritmo_generico.populacao = nova_populacao
    algoritmo_generico.geracao += 1
    
melhores.append(melhor_da_geracao)

def calcular_volume_mochila(solucao):
    volume_total = sum(solucao.espacos)
    print("Volume total da mochila:", volume_total)

print("Melhor solução:")
print("Cromossomo:", algoritmo_generico.melhor_solucao.cromossomo)
print("Espaços usados:", algoritmo_generico.melhor_solucao.espacos)
print(f"Volume total da mochila: {round(algoritmo_generico.melhor_solucao.espaco_usado, 2)}")
print("Valores obtidos:", algoritmo_generico.melhor_solucao.valores)
print("Preço total da mochila", algoritmo_generico.melhor_solucao.nota_avaliacao)

def plotar_grafico(resultados):
    geracoes = list(range(1, len(resultados) + 1))
    valores_totais = [individuo.nota_avaliacao for individuo in resultados]

    plt.plot(geracoes, valores_totais, linestyle='-')
    plt.title('Preço da Mochila por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Valor Total da Mochila')
    plt.grid(True)
    plt.show()





plotar_grafico(melhores)