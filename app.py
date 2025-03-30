# Solicitar ao usuário o nome do herói e a XP
nome = input("Digite o nome do herói: ")  # Entrada para o nome
xp = int(input("Digite a quantidade de XP do herói: "))  # Entrada para XP (convertido para inteiro)

# Calculando a faixa de níveis com base na XP
nivel_ordinal = xp // 1000  # Divisão inteira por 1000 para determinar o intervalo de XP

# Estrutura de decisão utilizando match-case
match nivel_ordinal:
    case 0:
        nivel = "Ferro"
    case 1:
        nivel = "Bronze"
    case 2:
        nivel = "Prata"
    case 3:
        nivel = "Ouro"
    case 4:
        nivel = "Platina"
    case 5:
        nivel = "Ascendente"
    case 6:
        nivel = "Imortal"
    case _:
        nivel = "Radiante"

# Saída do resultado
print(f"O Herói de nome {nome} está no nível de {nivel}")
