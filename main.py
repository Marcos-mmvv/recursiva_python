#Função fatorial

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)
    
# Programa principal

n = int(input('Informe um número interiro: '))

# Exibe o resultado do fatorial
print(f'Fatorial de {n} é: {calcular_fatorial(n)}.')
