import pygame
from pgzero.loaders import images

from config import WIDTH, HEIGHT

class BackgroundManager:
    def __init__(self, image_name="backgrounds/space", speed=1):
        self.image_name = image_name
        self.speed = speed
        self.bg_x = 0
        self._scaled_surf = None

    def _get_scaled_image(self):
        if self._scaled_surf is None:
            try:
                raw_surf = images.load(self.image_name)
                self._scaled_surf = pygame.transform.scale(raw_surf, (WIDTH, HEIGHT))
            except Exception:
                self._scaled_surf = None
        return self._scaled_surf

    def update(self):
        self.bg_x -= self.speed
        if self.bg_x <= -WIDTH:
            self.bg_x = 0

    def draw(self, screen):
        try:
            screen.fill((8, 10, 24))
        except Exception:
            try:
                screen.surface.fill((8, 10, 24))
            except Exception:
                pass

        surf = self._get_scaled_image()
        if surf:
            try:
                screen.surface.blit(surf, (int(self.bg_x), 0))
                screen.surface.blit(surf, (int(self.bg_x) + WIDTH, 0))
            except Exception:
                try:
                    screen.blit(surf, (int(self.bg_x), 0))
                    screen.blit(surf, (int(self.bg_x) + WIDTH, 0))
                except Exception:
                    pass
        else:
            try:
                screen.blit(self.image_name, (int(self.bg_x), 0))
                screen.blit(self.image_name, (int(self.bg_x) + WIDTH, 0))
            except Exception:
                pass
