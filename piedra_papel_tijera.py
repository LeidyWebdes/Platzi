import random # escoger aleatoriamente

options = ('piedra', 'papel', 'tijera') # elementos para que computer elija aleatoriamente

computer_wins = 0
user_wins = 0

total = int(input('¿Con cuántas partidas habrá un ganador? ')) # Cuántos rounds debe ganar un jugador para terminar el juego

rounds = 1

while True:
    
    print('*' * 10)
    print (f'ROUND: {rounds}')
    print(f'Puntos de User: {user_wins}')
    print(f'Puntos de Computer: {computer_wins}')
    print('*' * 10)

    user_option = input('¿piedra, papael o tijera? ').lower()
    rounds += 1
    
    if not user_option in options:
        print('Opción inválida')
        continue

    computer_option = random.choice(options)

    print('User option:', user_option)
    print('Computer option: ', computer_option)

    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User ganó!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Computer ganó')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a tijera')
            print('User ganó!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('Computer ganó')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('User ganó')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Computer ganó')
            computer_wins += 1
    if computer_wins == total:
        print('COMPUTER GANÓ EL JUEGO')
        break
    if user_wins == total:
        print('USER GANÓ EL JUEGO')
        break
    
    

    