from settings import *
from pytmx.util_pygame import load_pygame

from sprites import Sprite
from entities import Player
from groups import AllSprites


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Legacy of the Forgotten Isle")
        self.clock = pygame.time.Clock()

        # grouping everything
        self.all_sprites = AllSprites()

        self.import_assets()
        self.setup(self.tmx_maps["world"], "house")

    def import_assets(self):
        base_dir = dirname(__file__)

        self.tmx_maps = {
            "world": load_pygame(
                join(base_dir, "..", "texture_tiles", "tiles", "main_map.tmx")
            ),
            "hospital": load_pygame(
                join(base_dir, "..", "texture_tiles", "tiles", "hospital.tmx")
            )
        }

    def setup(self, tmx_map, player_start_pos):
        for layer in ["Terrain", "Top Terrain"]:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites) 

        for obj in tmx_map.get_layer_by_name("Objects"):
            Sprite((obj.x - 11, obj.y - 6), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name("Entities"):
            if obj.name == "Player" and obj.properties["pos"] == player_start_pos:
                self.player = Player(
                    (
                        obj.x,
                        obj.y,
                    ),
                    self.all_sprites,
                )

    def run(self):
        while True:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.all_sprites.update(dt)
            self.display_surface.fill("black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
