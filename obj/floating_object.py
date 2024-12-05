import pygame

from sound import Sound

class FloatingObject:
    def __init__(self, size: int, x: int, y: int, vx: float, vy: float, color: tuple[int, int, int]
                 , screen_width: int, screen_height: int):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.size)

    def updates(self, paddle=None):
        self.x += self.vx
        self.y += self.vy

        self.on_hit_screen_edge()
        if paddle is not None:
            self.on_hit_paddle(paddle)

    def on_hit_screen_edge(self):
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
        if self.y - self.size < 0 or self.y + self.size > self.screen_height:
            self.vy = -self.vy

    def on_hit_paddle(self, paddle):
        if self.x - self.size < 0 or self.x + self.size > paddle.width:
            self.vx = -self.vx
        if self.y - self.size < 0 or self.y + self.size > paddle.height:
            self.vy = -self.vy

class Ball(FloatingObject):
    def __init__(self, size: int = 20, x: int = 0, y: int = 0, vx: float = 0, vy: float = 0
                 , color: tuple[int, int, int] = (0, 0, 0), screen_width: int = 800, screen_height: int = 600):
        super().__init__(size, x, y, vx, vy, color, screen_width, screen_height)

    def on_hit_screen_edge(self):
        sound = Sound()
        if self.x - self.size < 0 or self.x + self.size > self.screen_width:
            self.vx = -self.vx
            sound.run_sound('wall')
        if self.y - self.size < 0 or self.y + self.size > self.screen_height:
            self.vy = -self.vy
            sound.run_sound('wall')

    def on_hit_paddle(self, paddle):
        sound = Sound()
        if self.x - self.size < 0 or self.x + self.size > paddle.width:
            self.vx = -self.vx
            sound.run_sound('paddle')
        if self.y - self.size < 0 or self.y + self.size > paddle.height:
            self.vy = -self.vy
            sound.run_sound('paddle')