card = input("Введите номер карты: ")


def carde(card):
    return print('*' * len(card[:-4]) + card[-4:])


carde(card)
