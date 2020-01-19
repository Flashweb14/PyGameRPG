class Camera:
    def __init__(self, game):
        self.game = game
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x = self.dx + int(obj.x)
        obj.rect.y = self.dy + int(obj.y)

    def update(self, target):
        self.dx = -(int(target.x) + target.rect.w // 2 - self.game.width // 2)
        self.dy = -(int(target.y) + target.rect.h // 2 - self.game.height // 2)
