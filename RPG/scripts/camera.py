class Camera:
    def __init__(self, game):
        self.game = game
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
        print(self.dx)
        print(self.dy)

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.game.width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.game.height // 2)
