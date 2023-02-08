import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 600, 600

def show_menu():
    menu_font = pygame.font.Font(None, 48)
    mot_jouer = menu_font.render("Jouer", True, (255, 255, 255))
    ajouter_mot = menu_font.render("Ajouter un mot", True, (255, 255, 255))
    quitter = menu_font.render("Quitter", True, (255, 255, 255))

    window.blit(mot_jouer, [WIDTH//2-30, HEIGHT//2])
    window.blit(ajouter_mot, [WIDTH//2-100, HEIGHT//2+50])
    window.blit(quitter, [WIDTH//2-40, HEIGHT//2+100])
    pygame.display.update()

    running_menu = True
    while running_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if WIDTH//2-50 < x < WIDTH//2+30 and HEIGHT//2 < y < HEIGHT//2+50:
                    play_game()
                    running_menu = False
                elif WIDTH//2-100 < x < WIDTH//2+100 and HEIGHT//2+50 < y < HEIGHT//2+100:
                    insert_word()
                    running_menu = False
                elif WIDTH//2-50 < x < WIDTH//2+40 and HEIGHT//2+100 < y < HEIGHT//2+150:
                    pygame.quit()
                    running_menu = False

def play_game():
    global words
    word = random.choice(words)

def insert_word():
    word = input("ajouter un mot: ")
    with open("mots.txt", "a") as f:
        f.write(word + "\n")
        show_menu()

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 32)

with open("mots.txt", "r") as f:
    words = f.readlines()

words = [word.strip() for word in words]
word = random.choice(words)

mauvaise_reponse = 0
bonne_reponse = 0
lettre_trouver = []

show_menu()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
        if event.type == pygame.KEYDOWN:
            letter = chr(event.key)            
            if letter not in lettre_trouver:
                lettre_trouver.append(letter)               
                if letter in word:
                    bonne_reponse += 1
                else:
                    mauvaise_reponse += 1 
                if bonne_reponse == len(word) or mauvaise_reponse == 7:
                    running = False
                    
    display_word = ""
    for char in word:
        if char in lettre_trouver:
            display_word += char + " "
        else:
            display_word += "_ "
    text = font.render(display_word, True, BLACK)
    window.blit(text, [250, 50])
#image du pendu
    if mauvaise_reponse >= 1:
        pendu_image = pygame.image.load("pendu0.png")
        window.blit(pendu_image, (75, HEIGHT-400))
    if mauvaise_reponse >= 2:
        pendu_image = pygame.image.load("pendu1.png")
        window.blit(pendu_image, (75, HEIGHT-400))
    if mauvaise_reponse >= 3:
        pendu_image = pygame.image.load("pendu2.png")
        window.blit(pendu_image, (75, HEIGHT-400))
    if mauvaise_reponse >= 4:
        pendu_image = pygame.image.load("pendu3.png")
        window.blit(pendu_image, (75, HEIGHT-400))
    if mauvaise_reponse >= 5:
        pendu_image = pygame.image.load("pendu4.png")
        window.blit(pendu_image, (75, HEIGHT-400))
    if mauvaise_reponse >= 6:
        pendu_image = pygame.image.load("pendu5.png")
        window.blit(pendu_image, (75, HEIGHT-400))
    if mauvaise_reponse >= 7:
        pendu_image = pygame.image.load("pendu6.png")
        window.blit(pendu_image, (75, HEIGHT-400))
    pygame.display.update()
    
    window.fill(WHITE)
if mauvaise_reponse == 7:
    result_text = "Perdu ! Le mot était " + word
elif bonne_reponse == len(word):
    result_text = "Félicitation le mot était " + word
else:
    result_text = "Merci d'avoir joué !"
result = font.render(result_text, True, BLACK)
window.blit(result, [200, 200])

pygame.display.update()
pygame.time.wait(2000)
pygame.quit()