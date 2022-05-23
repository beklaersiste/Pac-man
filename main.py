import pygame
from button import Button
WIDTH = 1280
HEIGHT = 640
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-man")
clock = pygame.time.Clock()


def menu():
    background = pygame.image.load('frame/background.png').convert_alpha()

    running = True

    while running:
        screen.blit(background, (0, 0))
        buttonPlay = Button((240, 80), "PLAY")
        buttonPlay.draw(screen, (520, 270))
        buttonScoreTable = Button((240, 80), "SCORE")
        buttonScoreTable.draw(screen, (520, 380))
        buttonExit = Button((240, 80), "EXIT")
        buttonExit.draw(screen, (520, 490))
        buttonAbout = Button((80, 80), "?")
        buttonAbout.draw(screen, (320, 490))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if buttonPlay.mouseInButton():
                        play()
                    elif buttonScoreTable.mouseInButton():
                        scoreTable()
                    elif buttonExit.mouseInButton():
                        running = False
                    elif buttonAbout.mouseInButton():
                        about()
        clock.tick(FPS)


def scoreTable():
    pass


def about():
    pass


def play():
    pass


if __name__ == "__main__":
    menu()
