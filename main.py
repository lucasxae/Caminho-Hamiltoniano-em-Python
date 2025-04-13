# Objetivo:
# § Desenvolver um programa em Python que implemente o algoritmo para
# encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado.
# O projeto deverá ser entregue por meio de um link para o repositório do GitHub
# no CANVAS.
# Sobre o algoritmo:
# § Um Caminho Hamiltoniano em um grafo é um caminho que visita cada vértice
# exatamente uma vez. Encontrar esse caminho é um problema clássico em teoria
# dos grafos e está associado a problemas de alta complexidade computacional,
# como o Problema do Caixeiro Viajante. Este projeto tem como objetivo
# implementar uma abordagem para determinar se um Caminho Hamiltoniano
# existe em um grafo e, em caso afirmativo, encontrá-lo.

def hamiltoniano(grafo, caminho, pos):
    if pos == len(grafo):
        return True

    for vertice in range(len(grafo)):
        if pode_adicionar(vertice, grafo, caminho, pos):
            caminho[pos] = vertice 

            if hamiltoniano(grafo, caminho, pos + 1):
                return True

            caminho[pos] = -1

    return False 


def pode_adicionar(vertice, grafo, caminho, pos):
    if grafo[caminho[pos - 1]][vertice] == 0:
        return False

    if vertice in caminho:
        return False

    return True

def main():
    grafo = [[0, 1, 1, 0],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [0, 1, 1, 0]]

    caminho = [-1] * len(grafo)
    caminho[0] = 0 

    if hamiltoniano(grafo, caminho, 1):
        print("Caminho Hamiltoniano encontrado:")
        print(caminho)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")

if __name__ == "__main__":
    main()
# Caminho Hamiltoniano encontrado: