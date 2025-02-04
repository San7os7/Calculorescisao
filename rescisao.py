print('Olá, seja bem-vindo(a) ao nosso calculo de rescisão!')
# entrada de dados
while True:
    nome = input('\nDigite o nome do funcionário: ')
    cargo = input('\nDigite o seu respectivo cargo: ')
    salario = float(input('\nDigite o seu respectivo salário: '))
    tempo_empresa = int(input('\nQuantos anos de empresa? '))
    meses_empresa = (tempo_empresa * 12)
    dias_trabalhados = int(input('\nQuantos dias trabalhados esse mês? '))
    justa_causa = input('\nO funcionário está sendo demitido por justa causa? (sim/não): ').lower()

    # aviso prévio
    dias_base = 30
    dias_adicionais = tempo_empresa * 3
    dias_aviso_previo = min(dias_base + dias_adicionais, 90)
    avisoprevio_valor = (salario / 30) * dias_aviso_previo

    #direitos
    saldo_salario = (salario/30) * dias_trabalhados
    ferias = (salario /12) * meses_empresa * 1.33
    decimoterceiro = (salario / 12) * meses_empresa
    fgts = salario * 0.08
    multafgts = fgts * 0.4
    total_a_receber = avisoprevio_valor + saldo_salario + ferias + fgts + multafgts


    # saida de dados
    if justa_causa == 'sim':
        print(f'\nO funcionário {nome} está sendo demitido por justa causa')
        print(f'\n irá receber - Saldo salário: R${saldo_salario}')
    else:
        print(f'O funcionário {nome} não está sendo demitido por justa causa!')
        print(f'\nTerá direito a receber: ')
        print(f'\nSaldo Salario - R${saldo_salario}')
        print(f'\nFerias Proporcionais - R${ferias}')
        print(f'\nFGTS - R${fgts}')
        print(f'\nMulta FGTS - R${multafgts}')
        print(f'\nDecimo Terceiro - R${decimoterceiro}')
        print(f'\nAviso Prévio - R${avisoprevio_valor}')
        print(f'\nTotal a receber- R${total_a_receber}')
    escolha = input('\nDeseja fazer um outro calculo? (sim/não): ').lower()
    if escolha == 'sim':
        continue
    else:
        break