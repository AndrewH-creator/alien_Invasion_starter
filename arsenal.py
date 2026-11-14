
"""
Program Name: Pixel Space Invasion - Track 2
Author: Andrew Hissong
Purpose: Manage the player's custom laser projectiles,
         including firing, updating, drawing, and removing
         lasers that leave the screen.
Date Updated: November 14, 2026
"""

import pygame
from bullet import Bullet


class Arsenal:
    """Manage the collection of lasers fired by the spaceship."""

    def __init__(self, game):
        """Initialize the game reference and laser sprite group."""

        self.game = game
        self.bullets = pygame.sprite.Group()

    def fire_bullet(self):
        """Create a laser if the maximum active laser count is not reached."""

        if len(self.bullets) < self.game.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """Update laser positions and remove offscreen projectiles."""

        # Move all active lasers upward
        self.bullets.update()

        # Remove lasers that leave the top of the screen
        self._remove_bullets_offscreen()

    def draw_bullets(self):
        """Draw every active custom laser on the game screen."""

        for bullet in self.bullets:
            bullet.draw_bullet()

    def _remove_bullets_offscreen(self) -> None:
        """Remove lasers that have traveled beyond the screen."""

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
