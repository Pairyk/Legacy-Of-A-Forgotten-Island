from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        base_dir = dirname(__file__)
        self.image = pygame.image.load(
            join(base_dir, "..", "texture_tiles", "sprites", "test_sprite1.png")
        )

        # just the tip for the transform
        # self.image = pygame.transform.scale(
        #     self.image, (self.image.get_width() * 1, self.image.get_height() * 1))

        self.rect = self.image.get_frect(center=pos)

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector()
        if keys[pygame.K_w]:
            input_vector.y -= 1
        if keys[pygame.K_s]:
            input_vector.y += 1
        if keys[pygame.K_a]:
            input_vector.x -= 1
        if keys[pygame.K_d]:
            input_vector.x += 1
        self.direction = input_vector

    def move(self, dt):
        self.rect.center += self.direction * 50 * dt

    def update(self, dt):
        self.input()
        self.move(dt)
