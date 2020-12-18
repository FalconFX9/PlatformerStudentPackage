import pygame

"PART 1"
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        width = None
        height = None

        self.image = None
        self.rect = None

        self.speed_x = None
        self.speed_y = None

        self.direction = 0

        self.platforms = None

    def handle_keys(self):
        pass

    def gravity(self):
        pass

    def jump(self):
        pass

    def update(self, *args, **kwargs) -> None:
        pass


"PART 2"
class Platform(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = None

        self.rect = None

        self.rect.x = None
        self.rect.y = None

"PART 5"
class Game:

    def __init__(self):
        pass

    def run(self):
        pass
