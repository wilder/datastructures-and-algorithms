'''
A Movile possui um app interno onde seus funcionários podem acompanhar notícias da empresa e ganhar pontos por participar de ações internas da Movile.

Como existem muitas pessoas na Movile, esses pontos são adicionados em "lotes"; Os Movilianos avisam que participaram de ações, e em um dia específico da semana esses Movilianos recebem, de uma vez só, seus pontos requisitados durante a semana.

Por exemplo, considere que existam 5 Movilianos e todos eles comecem 0 pontos (0 0 0 0 0). Após processar o lote Adicionar 10 pontos para os Movilianos 1 até 3, a nova lista de pontuação seria 10 10 10 0 0.

Input Format

A primeira linha possui 2 números n e k, indicando o número de Movilianos e o número de lotes, respectivamente.

As k linhas seguintes representam lotes, que consistem em 3 números:

O primeiro e segundo número a e b indicam um grupo (inclusivo) de Movilianos para quais uma certa pontuação deve ser adicionada.
O terceiro número indica a pontuação que deve adicionada para todos os Movilianos do grupo indicado.
'''

'''
Solution

create a list (players) with size N filled with 0.
For each range (i, j), players[i] += point, players[j] -= score
if j < N.

for each player starting from the second,
the score of the current is equal the curent score + last player's score.

get the biggest score from the list.

Time Complexity: O(N + K)

'''

n, k = map(int, input().split())
players = [0] * n

for r in range(k):
    i, j, p = map(int, input().split())
    players[i-1] += p
    if j < n:
        players[j] -= p
    #print(players)

i = 1
while i < n:
    players[i] += players[i-1]
    i += 1

print(max(players))
