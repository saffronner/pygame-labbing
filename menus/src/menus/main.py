import pygame

from pygame.event import Event
from pygame.locals import QUIT


def update(gs: GameState):
    widgets.Button.one_clicked = False
    x, y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        pygame.event.post(Event(MOUSE_HELD))

    for event in pygame.event.get():
        for widget in gs.widgets.__dict__.values():
            widget.handle_event(event, gs, x, y)

        if event.type == QUIT:
            gs.playing = False


def draw(screen: pygame.Surface, gs: GameState):
    screen.fill(settings.BOARD_COLOR)

    for widget in gs.widgets.__dict__.values():
        widget.draw(screen, gs)

    pygame.display.update()


def main():
    pygame.init()

    pygame.display.set_caption("menus")
    pygame.display.set_icon(pygame.image.load("assets/favicon.png"))

    # screen = pygame.display.set_mode((600, 400), flags=0, vsync=1)
    screen = pygame.display.set_mode((600, 400), flags=pygame.SCALED, vsync=1)

    gs: GameState = GameState()
    clock = pygame.time.Clock()
    while gs.playing:
        update(gs)
        draw(screen, gs)

        clock.tick(60)


main()
