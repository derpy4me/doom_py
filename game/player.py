"""Player class for game."""
# Standard Library Imports
import math

# Third Party Imports
import pygame

# Local App Imports
from settings import PLAYER_POSITION, PLAYER_ANGLE, PLAYER_ROTATION_SPEED, PLAYER_SPEED, WIDTH


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x, self.y = PLAYER_POSITION
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        direction_x, direction_y = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            direction_x += speed_cos
            direction_y += speed_sin
        if keys[pygame.K_s]:
            direction_x += -speed_cos
            direction_y += -speed_sin
        if keys[pygame.K_a]:
            direction_x += speed_sin
            direction_y += -speed_cos
        if keys[pygame.K_d]:
            direction_x += -speed_sin
            direction_y += speed_cos

        self.x += direction_x
        self.y += direction_y

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROTATION_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROTATION_SPEED * self.game.delta_time

        self.angle %= math.tau

    def draw(self):
        pygame.draw.line(
            self.game.screen,
            "yellow",
            (self.x * 100, self.y * 100),
            (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)),
            2,
        )
        pygame.draw.circle(self.game.screen, "green", (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
