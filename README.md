# Caminho Hamiltoniano em Python

## 📌 Descrição do Projeto

Este projeto implementa um algoritmo baseado em backtracking para encontrar um Caminho Hamiltoniano em um grafo não orientado. O algoritmo testa cada vértice como ponto de partida e tenta construir um caminho válido que visite todos os vértices exatamente uma vez.
### Explicação do Algoritmo

#### Função `hamiltoniano`

Esta função é responsável por construir o caminho Hamiltoniano recursivamente.

1. **Entrada**: Recebe o grafo, o caminho atual e o índice do vértice a ser processado.
2. **Saída**: Retorna `True` se um caminho Hamiltoniano for encontrado, caso contrário, `False`.

```python
def hamiltoniano(grafo, caminho, pos):
    # Caso base: se todos os vértices foram incluídos no caminho
    if pos == len(grafo):
        # Verifica se o último vértice está conectado ao primeiro (ciclo)
        return caminho[pos - 1] in grafo[caminho[0]]

    # Tenta adicionar cada vértice ao caminho
    for v in range(len(grafo)):
        if pode_adicionar(v, grafo, caminho, pos):
            caminho[pos] = v  # Adiciona o vértice ao caminho
            if hamiltoniano(grafo, caminho, pos + 1):  # Chamada recursiva
                return True
            caminho[pos] = -1  # Backtrack: remove o vértice do caminho

    return False  # Nenhum caminho válido encontrado
```

#### Função `pode_adicionar`

Esta função verifica se um vértice pode ser adicionado ao caminho atual.

1. **Entrada**: Recebe o vértice, o grafo, o caminho atual e a posição.
2. **Saída**: Retorna `True` se o vértice puder ser adicionado, caso contrário, `False`.

```python
def pode_adicionar(v, grafo, caminho, pos):
    # Verifica se o vértice é adjacente ao último vértice no caminho
    if v not in grafo[caminho[pos - 1]]:
        return False
    # Verifica se o vértice já foi incluído no caminho
    if v in caminho:
        return False
    return True
```

### Ajustes na Lógica do Algoritmo

1. **Melhoria na Verificação de Ciclo**: A verificação do ciclo no final da função `hamiltoniano` foi ajustada para garantir que o último vértice esteja conectado ao primeiro.
2. **Otimização do Backtracking**: A lógica de backtracking foi mantida eficiente, garantindo que o caminho seja limpo ao retroceder.

### Fluxo do Algoritmo

1. Inicialize o caminho com o primeiro vértice.
2. Use a função `hamiltoniano` para tentar construir o caminho recursivamente.
3. Verifique se o caminho encontrado é um ciclo Hamiltoniano.
4. Retorne o caminho se encontrado, ou indique que não há solução.
## ▶️ Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/lucasxae/Caminho-Hamiltoniano-em-Python.git
   cd Caminho-Hamiltoniano-em-Python
   ```

## 📊 Relatório Técnico

### Análise da Complexidade Computacional

#### Classes P, NP, NP-Completo e NP-Difícil

1. O problema do Caminho Hamiltoniano pertence à classe NP-Completo. Ele está em NP porque uma solução pode ser verificada em tempo polinomial. Além disso, é NP-Completo porque problemas conhecidos dessa classe, como o Problema do Caixeiro Viajante (TSP), podem ser reduzidos a ele.
2. A relação com o TSP é que ambos envolvem encontrar caminhos em grafos, mas o TSP adiciona restrições de custo às arestas, enquanto o Caminho Hamiltoniano apenas verifica a existência de um caminho.

### Análise da Complexidade Assintótica de Tempo

1. A complexidade temporal do algoritmo é \(O(N!)\), onde \(N\) é o número de vértices. Isso ocorre porque o algoritmo tenta todas as permutações possíveis de vértices.
2. Essa complexidade foi determinada pela contagem de operações necessárias para verificar cada permutação e construir o caminho.

### Aplicação do Teorema Mestre

O Teorema Mestre não pode ser aplicado diretamente, pois o algoritmo não segue uma recorrência típica de divisão e conquista. Ele utiliza backtracking, que explora todas as combinações possíveis de vértices.

### Análise dos Casos de Complexidade

1. **Pior Caso**: O algoritmo verifica todas as combinações possíveis sem encontrar um caminho válido, resultando em \(O(N!)\).
2. **Caso Médio**: Depende da estrutura do grafo, mas geralmente permanece exponencial.
3. **Melhor Caso**: Um caminho válido é encontrado rapidamente, mas a complexidade ainda é dominada pela verificação inicial, sendo \(O(N!)\).

Essas diferenças afetam o desempenho do algoritmo, tornando-o ineficiente para grafos grandes devido ao crescimento exponencial do tempo de execução.
