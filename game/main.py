"""Main file of the game where game loop is started."""
# Standard Library Imports
import sys

# Third Party Imports
import pygame

# Local App Imports
from map import Map
from player import Player
from raycasting import RayCasting
from settings import FPS, RESOLUTION


class Game:
    def __init__(self) -> None:
        pygame.init()  # pylint: disable=maybe-no-member
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (  # pylint: disable=maybe-no-member
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE  # pylint: disable=maybe-no-member
            ):
                pygame.quit()  # pylint: disable=maybe-no-member
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
