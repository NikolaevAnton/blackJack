#рисование карт в ascii

def draw_open_card(cards, total = "", diller = False):
    suits_symbols = ['♣', '♦', '♥', '♠']

    lines = [[] for i in range(10)]
    i = 0
    for index, card in enumerate(cards):
        if card.rank == '10':
            rank = card.rank
            space = ''
        else:
            rank = card.rank
            space = ' '
        if card.suit == "c":
            suit_symbol = suits_symbols[0]  # Трефы ♣
        elif card.suit == "d":
            suit_symbol = suits_symbols[1]  # Бубны ♦
        elif card.suit == "h":
            suit_symbol = suits_symbols[2]  # Червы ♥
        else:
            suit_symbol = suits_symbols[3]  # Пики ♠

        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit_symbol))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')
        lines[9].append('    {}     '.format(card))

        if not total == "":
            if len(cards) - 1 == i:
                lines[9].append(' Количество очков = {}'.format(total))


        i += 1

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))
    if not diller:
        return '\n'.join(result)
    else:
        return result


def draw_cards_diller(cards):
    lines = [
        ['┌─────────┐'],
        ['│░░░░░░░░░│'],
        ['│░░░░░░░░░│'],
        ['│░░░░░░░░░│'],
        ['│░░░░░░░░░│'],
        ['│░░░░░░░░░│'],
        ['│░░░░░░░░░│'],
        ['│░░░░░░░░░│'],
        ['└─────────┘'],
        ['     XX    ']
    ]

    hidden_card_to_diller = draw_open_card(cards[1:], diller=True)
    for index, line in enumerate(hidden_card_to_diller):
        lines[index].append(line)

    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    return '\n'.join(lines)