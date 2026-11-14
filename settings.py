
"""
Program Name: Pixel Space Invasion - Track 2
Author: Andrew Hissong
Purpose: Store game configuration settings, custom asset paths,
         player movement values, bullet properties, and settings
         for later milestones.
Date Updated: November 14, 2026
"""

from pathlib import Path
import json


class Settings:
    """Store configuration values for Pixel Space Invasion."""

    def __init__(self) -> None:
        """Initialize screen settings, custom assets, and game values."""

        # Game title and screen settings
        self.name: str = 'Pixel Space Invasion - Track 2'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Locate assets using pathlib for cross-platform support
        assets = Path(__file__).resolve().parent / 'Assets'
        images = assets / 'images'
        sounds = assets / 'Sound'

        # Custom retro pixel background and spaceship
        self.bg_file = images / 'space.png'
        self.ship_file = images / 'ship_0000.png'

        # Difficulty settings
        self.difficulty_scale = 1.1

        # Score storage for later milestones
        self.scores_file = assets / 'files' / 'scores.json'

        # Spaceship dimensions
        self.ship_w = 64
        self.ship_h = 64

        # Custom laser image and sound effects
        self.bullet_file = images / 'bullet_01.png'
        self.laser_sound = sounds / 'laserLarge_000.ogg'
        self.impact_sound = sounds / 'explosionCrunch_001.ogg'

        # Alien settings for Milestone 2
        self.alien_file = images / 'enemy_01.png'
        self.alien_w = 64
        self.alien_h = 64
        self.fleet_speed = 2

        # Button settings for Final Submission
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        # Text and HUD settings for Final Submission
        self.text_color = (255, 255, 255)
        self.button_font_size = 32
        self.HUD_font_size = 20

        # Custom retro pixel font
        self.font_file = (
            assets / 'Fonts'
            / 'Silkscreen'
            / 'PressStart2P-Regular.ttf'
        )

    def initialize_dynamic_settings(self) -> None:
        """Initialize player, bullet, and fleet gameplay settings."""

        # Player movement and lives
        self.ship_speed = 5
        self.starting_ship_count = 3

        # Custom laser properties
        self.bullet_w = 25
        self.bullet_h = 60
        self.bullet_speed = 7
        self.bullet_amount = 5

        # Fleet settings for Milestone 2
        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_difficulty(self) -> None:
        """Increase ship and fleet speeds as the game progresses."""

        self.ship_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
