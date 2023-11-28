from AlgoritmoGenetico import AlgoritmoGenetico
from Parametros import Parametros as params
from matplotlib import pyplot as plt
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Mochila")

class Item():
    def __init__ (self,nome,preco,volume):
        self.nome = nome
        self.preco = preco
        self.volume = volume

Lista_Itens  = [
     {'nome': "Item 1"  , 'volume': 1.11 , 'valor' : 4.75 },
     {'nome': "Item 2"  , 'volume': 1.25 , 'valor' : 8.00 },
     {'nome': "Item 3"  , 'volume': 1.67 , 'valor' : 5.50 },
     {'nome': "Item 4"  , 'volume': 1.67 , 'valor' : 3.50 },
     {'nome': "Item 5"  , 'volume': 1.25 , 'valor' : 1.50 },
     {'nome': "Item 6"  , 'volume': 1.46 , 'valor' : 4.50 },
     {'nome': "Item 7"  , 'volume': 0.90 , 'valor' : 4.50 },
     {'nome': "Item 8"  , 'volume': 1.00 , 'valor' : 3.75 },
     {'nome': "Item 9"  , 'volume': 1.54 , 'valor' : 11.50},
     {'nome': "Item 10" , 'volume': 1.75 , 'valor' : 10.00},
     {'nome': "Item 11" , 'volume': 1.33 , 'valor' : 7.50 },
     {'nome': "Item 12" , 'volume': 0.33 , 'valor' : 6.00 },
     {'nome': "Item 13" , 'volume': 2.22 , 'valor' : 3.00 },
     {'nome': "Item 14" , 'volume': 3.24 , 'valor' : 4.50 },
     {'nome': "Item 15" , 'volume': 1.00 , 'valor' : 23.00},
     {'nome': "Item 16" , 'volume': 2.50 , 'valor' : 1.30 },
     {'nome': "Item 17" , 'volume': 1.50 , 'valor' : 3.14 },
     {'nome': "Item 18" , 'volume': 5.77 , 'valor' : 1.41 },
     {'nome': "Item 19" , 'volume': 1.23 , 'valor' : 5.22 },
     {'nome': "Item 20" , 'volume': 4.50 , 'valor' : 8.10 },
     {'nome': "Item 21" , 'volume': 6.70 , 'valor' : 1.40 },
     {'nome': "Item 22" , 'volume': 1.20 , 'valor' : 2.25 },
     {'nome': "Item 23" , 'volume': 0.44 , 'valor' : 0.50 },
     {'nome': "Item 24" , 'volume': 1.33 , 'valor' : 2.33 },
     {'nome': "Item 25" , 'volume': 1.40 , 'valor' : 1.75 },
     {'nome': "Item 26" , 'volume': 4.63 , 'valor' : 9.50 },
     {'nome': "Item 27" , 'volume': 6.22 , 'valor' : 3.10 },
     {'nome': "Item 28" , 'volume': 0.45 , 'valor' : 2.25 },
]

itens = [Item(item['nome'], item['valor'], item['volume']) for item in Lista_Itens]
espacos = [item['volume'] for item in Lista_Itens]
valores = [item['valor'] for item in Lista_Itens]


algoritmo_generico = AlgoritmoGenetico(params.numero_individuos_populacao)


algoritmo_generico.inicializa_populacao(espacos,valores,params.limite_espaco_mochila)


melhores_resultados = []


# Utilizado para pegar o melhor indivíduo da última geração e 
# adicioná-lo à lista de melhores resultados
for i in range(params.numero_geracao):

    # Ordena a população com base nas pontuações de avaliação
    algoritmo_generico.ordena_populacao()

    # Obtém o melhor indivíduo da geração e adiciona a lista de melhores resultados
    melhor_geracao = algoritmo_generico.populacao[0]
    melhores_resultados.append(melhor_geracao)

    # Atualiza a melhor solução encontrada até o momento 
    # se o indivíduo atual tiver uma pontuação de avaliação mais alta
    algoritmo_generico.melhor_individuo(melhor_geracao)

    # Calcula a soma de todas as pontuações de avaliação na população
    soma_avaliacao = algoritmo_generico.soma_avaliacoes()

    # Cria uma nova população vazia para a próxima geração
    nova_populacao = []

    # Cria novos indivíduos para a próxima geração selecionando pais e realizando crossover
    for i in range(0, algoritmo_generico.tamanho_populacao, 2):

        pais = algoritmo_generico.selecionar_pais()
        filhos = pais[0].crossover(pais[1])
        
        # Adiciona os filhos à nova população
        for filho in filhos:
            nova_populacao.append(filho)

    # Substitui a população atual pela nova população
    algoritmo_generico.populacao = nova_populacao
    # Incrementa o contador de geração
    algoritmo_generico.geracao += 1

# Adiciona o melhor indivíduo da última geração à lista de melhores resultados
melhores_resultados.append(melhor_geracao)

console.print("[red]\n\nMelhor solução encontrada: \n[/red]", style="underline")
table.add_column("Nome", style="cyan")
table.add_column("Volume", style="magenta", justify="center")
table.add_column("Preço", style="green", justify="right")

volumes_1 = []
valores_1 = []
contador = 0

for item_index, valor in enumerate(algoritmo_generico.melhor_solucao.cromossomo):
    if valor == 1:  # Verifica se o item foi selecionado
        item = itens[item_index]
        table.add_row(item.nome, str(item.volume), f"R$ {item.preco:.2f}")

        volumes_1.append(item.volume)
        valores_1.append(item.preco)
        contador += 1


console.print(f"[green]Cromossomo:[/] {algoritmo_generico.melhor_solucao.cromossomo}")
console.print(f"\n[cyan]Espaços usados:[/] {volumes_1}")
console.print(f"\n[purple]Volume total da mochila[/]: {round(algoritmo_generico.melhor_solucao.espaco_usado, 2)}\n")
console.print(f"[blue]Valores obtidos:[/] {valores_1}")
console.print(f"\n[red]Preço total da mochila:[/] {algoritmo_generico.melhor_solucao.nota_avaliacao:.2f} \n")

table.add_section()
table.add_row(f"Itens={contador}", f"{algoritmo_generico.melhor_solucao.espaco_usado:.2f}l", f"R$ {algoritmo_generico.melhor_solucao.nota_avaliacao:.2f}")

console.print(table)

def plotar_grafico(resultados):
    geracoes = list(range(1, len(resultados) + 1))
    valores_totais = [individuo.nota_avaliacao for individuo in resultados]

    plt.plot(geracoes, valores_totais, linestyle='-')
    plt.title('Preço da Mochila por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Valor Total da Mochila')
    plt.grid(True)
    plt.show()


plotar_grafico(melhores_resultados)