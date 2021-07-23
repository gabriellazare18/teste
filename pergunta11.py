continuar = True
soma = 0
count J

while continuar:
    try:
        numero = int(input('Digite um número: '))
        decisao = str(input('Voce Dejesa continuar digitando números? s - SIM / n - NÃO: '))
        soma += numero
        count += 1
    except ValueError:
        print('Apenas digite números inteiros!')
    else:
        if count == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

        if decisao == 'n' or decisao == 'N':
            continuar = False

print(f'O Menor número digitado foi {menor}.')
print(f'O Maior número digitado foi {maior}.')
print(f'A media da soma dos números foi: {soma / count}')