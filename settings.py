
from pathlib import Path


class Settings:

    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Find the Assets folder beside this settings.py file
        assets = Path(__file__).resolve().parent / 'Assets'
        images = assets / 'images'
        sounds = assets / 'Sound'

        self.bg_file = images / 'Starbasesnow.png'
        self.ship_file = images / 'ship2(no bg).png'

        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_file = images / 'laserBlast.png'
        self.laser_sound = sounds / 'laser.mp3'
        self.impact_sound = sounds / 'impactSound.mp3'

        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 10

        self.alien_file = images / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 40
