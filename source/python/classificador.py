def classificar_heroi(nome: str, xp: int) -> str:
    if xp < 1000:
        nivel = 'Ferro'
    elif xp <= 2000:
        nivel = 'Bronze'
    elif xp <= 5000:
        nivel = 'Prata'
    elif xp <= 7000:
        nivel = 'Ouro'
    elif xp <= 8000:
        nivel = 'Platina'
    elif xp <= 9000:
        nivel = 'Ascendente'
    elif xp <= 10000:
        nivel = 'Imortal'
    else:
        nivel = 'Radiante'
    return f"O Herói de nome {nome} está no nível de {nivel}"

if __name__ == '__main__':
    nome = input('Digite o nome do herói: ')
    xp = int(input('Digite a quantidade de XP: '))
    print(classificar_heroi(nome, xp))
