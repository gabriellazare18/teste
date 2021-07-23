print('Bora jogar Jokenpo? Digite 1-Pedra / 2-Papel / 3-Tesoura')
pessoa1 = int(input('Pessoa 1: Digite alguma das opções: '))
pessoa2 = int(input('Pessoa 2: Digite alguma das opções: '))

if pessoa1 == 1 and pessoa2 == 3:
    print('Parabéns pessoa 1 ganhou escolheu pedra e pessoa 2 tesoura')
elif pessoa1 == 2 and pessoa2 == 1:
    print('Parabéns pessoa 1 ganhou escolheu papel e pessoa 2 pedra')
elif pessoa1 == 3 and pessoa2 == 2:
    print('Parabéns pessoa 1 ganhou escolheu tesoura e pessoa 2 papel')
elif pessoa1 == 1 and pessoa2 == 1:
    print('Empatou os dois jogaram a mesma!')
elif pessoa1 == 2 and pessoa2 == 2:
    print('Empatou os dois jogaram a mesma!')
elif pessoa1 == 3 and pessoa2 == 3:
    print('Empatou os dois jogaram a mesma!')
elif pessoa2 == 1 and pessoa1 == 3:
    print('Parabéns pessoa 2 ganhou escolheu pedra e pessoa 1 tesoura')
elif pessoa2 == 2 and pessoa1 == 1:
    print('Parabéns pessoa 2 ganhou escolheu papel e pessoa 1 pedra')
elif pessoa2 == 3 and pessoa1 == 2:
    print('Parabéns pessoa 2 ganhou escolheu tesoura e pessoa 1 papel')
else:
    print('Jogada errada tente novamente!')