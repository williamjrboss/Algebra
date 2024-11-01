import numpy as np

# Matriz de transição
T = np.array([[0.6, 0.4],
              [0.3, 0.7]])

# Vetor de estado inicial
x0 = np.array([0, 1])

# Calculando o estado após 3 passos
x3 = np.linalg.matrix_power(T, 3) @ x0

# A probabilidade de vencer o terceiro jogo é o primeiro elemento de x3
probabilidade_de_vencer_terceiro_jogo = x3[0]

print("Probabilidade de vencer o terceiro jogo:", probabilidade_de_vencer_terceiro_jogo)