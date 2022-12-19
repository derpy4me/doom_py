"""Raycasting class and functionality."""
# Standard Library Imports
import math

# Third Party Imports
import pygame

# Local App Imports
from settings import HALF_FOV, NUM_RAYS, DELTA_ANGLE, MAX_DEPTH


class RayCasting:
    def __init__(self, game) -> None:
        self.game = game

    def ray_cast(self):
        player_x, player_y = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle = HALF_FOV + 0.0001
        for _ in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.sin(ray_angle)

            # Horizontals
            y_hor, direction_y = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - player_y) / sin_a
            x_hor = player_x + depth_hor * cos_a

            delta_depth = direction_y / sin_a
            direction_x = delta_depth * cos_a

            for _ in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += direction_x
                y_hor += direction_y
                depth_hor += delta_depth

            # Verticals
            x_vert, direction_x = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - player_x) / cos_a
            y_vert = player_y + depth_vert * sin_a

            delta_depth = direction_x / cos_a
            direction_y = delta_depth * sin_a

            for _ in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += direction_x
                y_vert += direction_y
                depth_vert += delta_depth

            # Depth
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # Draw for debugging
            pygame.draw.line(
                self.game.screen,
                "yellow",
                (100 * player_x, 100 * player_y),
                (100 * player_x + 100 * depth * cos_a, 100 * player_y + 100 * depth * sin_a),
                2,
            )

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
