import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# 카드 덱 생성
def create_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# 카드 점수 계산
def calculate_score(cards):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 0, 'jack': 0, 'queen': 0, 'king': 0, 'ace': 1}
    total = sum(rank_values[card['rank']] for card in cards)
    return total % 10

# 카드 이미지 로드
def load_card_images():
    card_images = {}
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    for suit in suits:
        for rank in ranks:
            filename = f"card_images/{rank}_of_{suit}.png"
            image = Image.open(filename)
            image = image.resize((100, 150), Image.ANTIALIAS)  # 카드 크기 조정
            card_images[(rank, suit)] = ImageTk.PhotoImage(image)
    return card_images

# 게임 로직
def play_game():
    global player_images, banker_images, community_images
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    banker_hand = [deck.pop(), deck.pop()]
    community_cards = []

    # 초기 카드 이미지 출력
    player_images = [card_images[(card['rank'], card['suit']] for card in player_hand]
    banker_images = [card_images[(card['rank'], card['suit']] for card in banker_hand]
    update_card_display()

    # 플랍(3장의 커뮤니티 카드)
    for _ in range(3):
        community_cards.append(deck.pop())
    community_images = [card_images[(card['rank'], card['suit'])] for card in community_cards]
    update_card_display()

    # 턴(1장의 커뮤니티 카드)
    community_cards.append(deck.pop())
    community_images.append(card_images[(community_cards[-1]['rank'], community_cards[-1]['suit']])
    update_card_display()

    # 리버(1장의 커뮤니티 카드)
    community_cards.append(deck.pop())
    community_images.append(card_images[(community_cards[-1]['rank'], community_cards[-1]['suit']])
    update_card_display()

    # 점수 계산
    player_score = calculate_score(player_hand + community_cards)
    banker_score = calculate_score(banker_hand + community_cards)

    # 결과 출력
    if player_score > banker_score:
        messagebox.showinfo("Result", "Player wins!")
    elif banker_score > player_score:
        messagebox.showinfo("Result", "Banker wins!")
    else:
        messagebox.showinfo("Result", "It's a tie!")

# 카드 이미지 업데이트
def update_card_display():
    for i, image in enumerate(player_images):
        player_card_labels[i].config(image=image)
    for i, image in enumerate(banker_images):
        banker_card_labels[i].config(image=image)
    for i, image in enumerate(community_images):
        community_card_labels[i].config(image=image)

# GUI 설정
root = tk.Tk()
root.title("Baccarat Game")
root.geometry("800x600")  # 화면 크기 설정

# 카드 이미지 로드
card_images = load_card_images()

# 플레이어 카드 레이블
player_card_labels = [tk.Label(root) for _ in range(2)]
for label in player_card_labels:
    label.pack(side=tk.LEFT, padx=10)

# 뱅커 카드 레이블
banker_card_labels = [tk.Label(root) for _ in range(2)]
for label in banker_card_labels:
    label.pack(side=tk.LEFT, padx=10)

# 커뮤니티 카드 레이블
community_card_labels = [tk.Label(root) for _ in range(5)]
for label in community_card_labels:
    label.pack(side=tk.LEFT, padx=10)

# 버튼 추가
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack(pady=20)

# GUI 실행
root.mainloop()