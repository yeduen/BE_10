import random

# 카드 덱 생성
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# 카드 점수 계산
def calculate_score(cards):
    rank_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
    total = sum(rank_values[card['rank']] for card in cards)
    return total % 10  # 바카라 점수는 10으로 나눈 나머지

# 카드 분배
def deal_initial_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    banker_hand = [deck.pop(), deck.pop()]
    return player_hand, banker_hand

# 추가 카드 규칙 적용
def apply_baccarat_rules(player_hand, banker_hand, deck):
    player_score = calculate_score(player_hand)
    banker_score = calculate_score(banker_hand)

    # 플레이어가 세 번째 카드를 받는 경우
    if player_score <= 5:
        player_hand.append(deck.pop())
        player_score = calculate_score(player_hand)

        # 뱅커의 추가 카드 규칙
        if banker_score <= 2:
            banker_hand.append(deck.pop())
        elif banker_score == 3 and player_hand[2]['rank'] != '8':
            banker_hand.append(deck.pop())
        elif banker_score == 4 and player_hand[2]['rank'] not in ['0', '1', '8', '9']:
            banker_hand.append(deck.pop())
        elif banker_score == 5 and player_hand[2]['rank'] in ['4', '5', '6', '7']:
            banker_hand.append(deck.pop())
        elif banker_score == 6 and player_hand[2]['rank'] in ['6', '7']:
            banker_hand.append(deck.pop())
    else:
        # 플레이어가 세 번째 카드를 받지 않으면 뱅커는 5점 이하일 때만 추가 카드를 받음
        if banker_score <= 5:
            banker_hand.append(deck.pop())

    return player_hand, banker_hand

# 게임 실행
def play_baccarat():
    deck = create_deck()
    player_hand, banker_hand = deal_initial_cards(deck)

    print("Initial Cards:")
    print(f"Player's Hand: {[card['rank'] for card in player_hand]}")
    print(f"Banker's Hand: {[card['rank'] for card in banker_hand]}")

    # 추가 카드 규칙 적용
    player_hand, banker_hand = apply_baccarat_rules(player_hand, banker_hand, deck)

    print("\nFinal Cards:")
    print(f"Player's Hand: {[card['rank'] for card in player_hand]} (Score: {calculate_score(player_hand)})")
    print(f"Banker's Hand: {[card['rank'] for card in banker_hand]} (Score: {calculate_score(banker_hand)})")

    # 승패 결정
    player_score = calculate_score(player_hand)
    banker_score = calculate_score(banker_hand)

    if player_score > banker_score:
        print("Player wins!")
    elif banker_score > player_score:
        print("Banker wins!")
    else:
        print("It's a tie!")

# 게임 시작
play_baccarat()