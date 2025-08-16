import pygame, random, sys
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rock paper scissors")
font = pygame.font.SysFont(None,40)
choices = ["rock" "paper" "scissors"]
buttons = [pygame.rect(80+ i*160,280,130,60)for i in range(3)]
player_choice =""
computer_choice = ""
result =""
def get_winner(player,computer):
    if player == computer:
        return "its a tie"
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock",}
    return "you win" if rules [player] == computer else "computer wins"
while True:
    screen.fill((245, 245, 245))
    title = font.render("rock paper scissor"); True (0, 0, 128)
    screen.blit(title,(title,(WIDTH) //2 - title.get_width()//2, 40))