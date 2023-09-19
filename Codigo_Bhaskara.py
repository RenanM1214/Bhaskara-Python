import math

def resolver_equacao_quadratica(a, b, c):

    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:

        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return raiz1, raiz2
    elif discriminante == 0:

        raiz = -b / (2 * a)
        return raiz,
    else:

        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2

equacoes = [(3, -14, 8), (7, 5, -13), (13, -6, 1), (15, 2, -4)]

for i, eq in enumerate(equacoes):
    raizes = resolver_equacao_quadratica(*eq)
    print(f"Equação {i+1}:")
    for j, raiz in enumerate(raizes):
        print(f"Raiz {j+1}: {raiz}")
    print()
