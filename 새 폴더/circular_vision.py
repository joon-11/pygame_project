# circular_vision.py

import pygame
from pygame.math import Vector2

class CircularVision:
    def __init__(self, screen, player_pos, radius):
        self.screen = screen
        self.player_pos = player_pos
        self.radius = radius

    def draw_mask(self):
        mask = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        mask.fill((0, 0, 0, 255))  # Fill the mask with black
        pygame.draw.circle(mask, (0, 0, 0, 0), self.player_pos, self.radius)  # Clear the circle area
        self.screen.blit(mask, (0, 0))

    def set_radius(self, radius):
        self.radius = radius
