import random, time

DECK = []
MY_CARDS = []
PC_CARDS = []

for i in range(1, 21):
    DECK.append(i)


def dealer(player_deck):
    while len(player_deck) < 4:
        selected_card = random.choices(DECK)[0]
        player_deck.append(selected_card)
        DECK.remove(selected_card)


def pc_logics(player_select):
    POSSIBLE_CHOICES = []
    for i in sorted(PC_CARDS):
        if i > player_select:
            POSSIBLE_CHOICES.append(i)
    if POSSIBLE_CHOICES:
        return random.choices(POSSIBLE_CHOICES)[0]
    else:
        return min(PC_CARDS)


def gameplay():
    MY_POINTS = 0
    PC_POINTS = 0

    while True:
        if MY_CARDS:
            print('\033[1m' + f"Your cards: {MY_CARDS}" + '\033[0m')
            try:
                CHOICE = int(input('\033[1m' + "Pick a card: " + '\033[0m'))
                if CHOICE in MY_CARDS:
                    print(f"You've picked {CHOICE}")
                    MY_CARDS.remove(int(CHOICE))
                    print("Your enemy is picking a card...")
                    time.sleep(2)
                    PC_CHOICE = pc_logics(CHOICE)
                    PC_CARDS.remove(PC_CHOICE)
                    print(f"Enemy have picked {PC_CHOICE}")
                    if MY_CARDS:
                        print("Next round...")
                        print("")
                    if PC_CHOICE < CHOICE:
                        MY_POINTS += 1
                    else:
                        PC_POINTS += 1
                else:
                    print("There's no such card in your hand.")
            except ValueError:
                print("Stick to numbers please...")
        else:
            print("")
            if MY_POINTS > PC_POINTS:
                print('\033[1m' + '\033[92m' + "You won!" + '\033[0m')
                break
            elif MY_POINTS == PC_POINTS:
                print('\033[1m' + '\033[93m' + "Draw!" + '\033[0m')
                break
            else:
                print('\033[1m' + '\033[91m' + "You lost!" + '\033[0m')
                break


dealer(MY_CARDS)
dealer(PC_CARDS)
gameplay()
