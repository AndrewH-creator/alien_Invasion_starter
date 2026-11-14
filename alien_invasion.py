
import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

# Milestone 2 and Final Submission features
# from game_stats import GameStats
# from alien_fleet import AlienFleet
# from time import sleep
# from button import Button
# from hud import HUD

class AlienInvasion:

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_w, self.settings.screen_h)
        )

        # Milestone 1: HUD and scoring disabled
        # self.game_stats = GameStats(self)
        # self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()


        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(
            self.settings.laser_sound
        )
        self.laser_sound.set_volume(1.0)

        # Milestone 2: Explosion sound
        # self.impact_sound = pygame.mixer.Sound(
        #     self.settings.impact_sound
        # )
        # self.impact_sound.set_volume(1.0)

        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)

        # Milestone 2
        # self.alien_fleet = AlienFleet(self)

        # Final Submission
        # self.play_button = Button(self, 'Play')

        # Milestone 1: Game starts immediately
        self.game_active = True
    

    def run_game(self) -> None:
        """Run the Milestone 1 game loop."""
        while self.running:
            self._check_events()

            if self.game_active:
                self.ship.update()

                # Milestone 2 features
                # self.alien_fleet.update_fleet()
                # self._check_collisions()

            self.arsenal.update_bullets()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

        pygame.quit()
        sys.exit()

    def _check_collisions(self) -> None:
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()


        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.bullets)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # update game stats level
            self.game_stats.update_level()
            # update HUD view
            self.HUD.update_level()
        

    def _check_game_status(self) -> None:
        if self.game_stats.ships_left >0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

       


    def _reset_level(self) -> None:
        self.ship.arsenal.bullets.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self) -> None:
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()

        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)
            

    def _update_screen(self) -> None:
        """Draw the custom Milestone 1 game assets."""

        # Custom background
        self.screen.blit(self.bg, (0, 0))

        # Custom lasers
        self.arsenal.draw_bullets()

        # Custom spaceship
        self.ship.draw()

        # Milestone 2
        # self.alien_fleet.draw()

        # Final Submission
        # self.HUD.draw()
        # if not self.game_active:
        #     self.play_button.draw()

        pygame.display.flip()

    def _check_events(self) -> None:
        """Handle keyboard and window events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            # Final Submission: Play button
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

 
    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
                self.ship.fire()
                print("SPACE PRESSED")
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.running = False
            

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
