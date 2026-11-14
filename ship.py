
"""
Program Name: Pixel Space Invasion - Track 2
Author: Andrew Hissong
Purpose: Manage the custom spaceship, including its image,
         position, movement, laser firing, and collision detection.
Date Updated: November 14, 2026
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """Represent the player's custom retro pixel spaceship."""

    def __init__(
        self, game: 'AlienInvasion', arsenal: 'Arsenal'
    ) -> None:
        """Initialize the ship image, position, and movement controls."""

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load the custom spaceship image from settings.py
        self.image = pygame.image.load(self.settings.ship_file)

        # Resize the spaceship to its configured dimensions
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        # Create the ship rectangle and center it
        self.rect = self.image.get_rect()
        self._center_ship()

        # Track movement using the arrow keys
        self.moving_right = False
        self.moving_left = False

        # Connect the ship to its laser arsenal
        self.arsenal = arsenal

    def _center_ship(self):
        """Position the spaceship at the bottom center of the screen."""

        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Update the spaceship position during each game frame."""

        self._update_ship_movement()

    def _update_ship_movement(self):
        """Move the spaceship horizontally within screen boundaries."""

        # Get the configured movement speed
        temp_speed = self.settings.ship_speed

        # Move right without leaving the screen
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed

        # Move left without leaving the screen
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        # Update the ship rectangle
        self.rect.x = self.x

    def draw(self) -> None:
        """Draw the custom spaceship image on the game screen."""

        self.screen.blit(self.image, self.rect)

    def fire(self) -> None:
        """Fire a custom laser using the Arsenal class."""

        self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        """Detect collisions and reset the ship position if hit.

        This method is reserved for Milestone 2 gameplay.
        """

        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True

        return False
