from pathlib import Path
import json





class Settings:

    def __init__(self) -> None:
        self.name: str = 'Pixel Space Invasion - Track 2'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Find the Assets folder beside settings.py
        assets = Path(__file__).resolve().parent / 'Assets'
        images = assets / 'images'
        sounds = assets / 'Sound'

        self.bg_file = images / 'space.png'
        self.ship_file = images / 'ship_0000.png'
        self.difficulty_scale = 1.1

        self.scores_file = assets / 'files' / 'scores.json'

        self.ship_w = 64
        self.ship_h = 64

        self.bullet_file = images / 'bullet_01.png'
        self.laser_sound = sounds / 'laserLarge_000.ogg'
        self.impact_sound = sounds / 'explosionCrunch_001.ogg'

        self.alien_file = images / 'enemy_01.png'
        self.alien_w = 64
        self.alien_h = 64
        self.fleet_speed = 2

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 32
        self.HUD_font_size = 20

        self.font_file = (
            assets / 'Fonts'
            / 'Silkscreen'
            / 'PressStart2P-Regular.ttf'
        )


    def initialize_dynamic_settings(self) -> None:
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 60
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.fleet_direction = 1
        self.alien_points = 50


    def increase_difficulty(self) -> None:
        self.ship_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale