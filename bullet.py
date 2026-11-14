
"""
Program Name: Pixel Space Invasion - Track 2
Author: Andrew Hissong
Purpose: Create, display, and move custom retro pixel laser
         projectiles fired by the player's spaceship.
Date Updated: November 14, 2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Represent a custom laser projectile fired by the spaceship."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the laser image, position, and game settings."""

        super().__init__()

        # Access the game screen and configuration
        self.screen = game.screen
        self.settings = game.settings

        # Load the custom laser image using the pathlib asset path
        self.image = pygame.image.load(self.settings.bullet_file)

        # Resize the laser to the configured dimensions
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Position the laser at the top center of the spaceship
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # Store the vertical position for smooth movement
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the laser upward according to the configured speed."""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draw the custom laser image at its current position."""

        self.screen.blit(self.image, self.rect)
