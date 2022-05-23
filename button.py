import pygame
pygame.font.init()


class Button:
    RED = (249, 44, 61)
    ORANGE = (248, 144, 73)
    YELLOW = (254, 231, 125)
    BLACK = (0, 0, 0)
    FONT_SIZE = 72

    def __init__(self, size, text):
        font = pygame.font.Font(None, self.FONT_SIZE)
        self._pos = None
        self._size = size
        self._text = font.render(text, True, self.BLACK)

    def draw(self, screen, pos):
        self._pos = (pos[0], pos[1], pos[0] + self._size[0], pos[1] + self._size[1])
        if self.mouseInButton():
            pygame.draw.rect(screen, self.ORANGE, (pos[0], pos[1], self._size[0], self._size[1]))
        else:
            pygame.draw.rect(screen, self.RED, (pos[0], pos[1], self._size[0], self._size[1]))
        pygame.draw.rect(screen, self.YELLOW, (pos[0], pos[1], self._size[0], self._size[1]), 6)
        place = self._text.get_rect(center=(pos[0]+(self._size[0]//2), pos[1]+(self._size[1]//2)))
        screen.blit(self._text, place)

    def mouseInButton(self):
        mousePos = pygame.mouse.get_pos()
        return self._pos[0] < mousePos[0] < self._pos[2] and self._pos[1] < mousePos[1] < self._pos[3]





