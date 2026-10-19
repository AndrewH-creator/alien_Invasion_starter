import pygame
from bullet import Bullet


class Arsenal:
    def __init__(self, game):
        self.game = game
        self.bullets = pygame.sprite.Group()

    def fire_bullet(self):
        if len(self.bullets) < self.game.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()

        # Remove bullets that leave the top of the screen.
        for bullet in list(self.bullets):
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw_bullet()

    def _remove_bullets_offscreen(self) -> None:
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
