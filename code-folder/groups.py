from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()
        self.zoom_scale = ZOOM_SCALE

    def draw(self, player_center):
        self.offset.x = -(player_center[0] * self.zoom_scale - WINDOW_WIDTH / 2)
        self.offset.y = -(player_center[1] * self.zoom_scale - WINDOW_HEIGHT / 2)

        for sprite in self:
            zoomed_pos = (
                sprite.rect.left * self.zoom_scale + self.offset.x,
                sprite.rect.top * self.zoom_scale + self.offset.y,
            )
            scaled_image = pygame.transform.scale(
                sprite.image,
                (
                    int(sprite.rect.width * self.zoom_scale),
                    int(sprite.rect.height * self.zoom_scale),
                ),
            )
            self.display_surface.blit(scaled_image, zoomed_pos)
