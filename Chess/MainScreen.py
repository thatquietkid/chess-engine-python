import pygame, sys, ChessMain, PlayerMode
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((762, 512))
pygame.display.set_caption("Chess")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        ChessMain.main()
                

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(20).render("Choose One Player or Two Player", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(380, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_1PLAYER = Button(image=None, pos=(380, 260), 
                                text_input="One Player", font=get_font(30), base_color="Black", hovering_color="Green")
        OPTIONS_2PLAYER = Button(image=None, pos=(380, 360), 
                                text_input="Two Player", font=get_font(30), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=None, pos=(380, 460), 
                                text_input="Back", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_1PLAYER.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_1PLAYER.update(SCREEN)
        OPTIONS_2PLAYER.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_2PLAYER.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_1PLAYER.checkForInput(OPTIONS_MOUSE_POS):
                    PlayerMode.player_one = True
                elif OPTIONS_2PLAYER.checkForInput(OPTIONS_MOUSE_POS):
                    PlayerMode.player_two = True
                elif OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=None, pos=(400, 200), 
                            text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(400, 300), 
                            text_input="OPTIONS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(400, 400), 
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()