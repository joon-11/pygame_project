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
        mask.fill((0, 0, 0, 0))  # Fill the mask with transparent color

        # Clear the circle area
        pygame.draw.circle(mask, (0, 0, 0, 255), self.player_pos, self.radius)

        # Fill the left part of the mask with black
        left_rect = pygame.Rect(0, 0, self.player_pos[0] - self.radius, self.screen.get_height())
        pygame.draw.rect(mask, (0, 0, 0, 255), left_rect)

        self.screen.blit(mask, (0, 0))
