import pygame

# 상수
FLASHLIGHT_COLOR = (255, 255, 255)
DARK_DURATION = 200  # 어둠이 유지되는 시간 (밀리초 단위)

class Flashlight:
    def __init__(self, max_light=10000, radius=100):
        self.x, self.y = 0, 0
        self.light = max_light
        self.max_light = max_light
        self.light_press = False
        self.radius = radius  # 빛의 반경을 설정합니다.
        self.prev_mouse_pos = (0, 0)  # 이전 마우스 위치를 저장하는 변수입니다.
        self.dark_timer = 100  # 어둠이 유지되는 타이머입니다.

    def shoot_light(self, x, y):
        self.x, self.y = x, y

    def decrease_light(self):
        self.light -= 1  # 빛의 양을 1만큼 감소시킵니다.
        if self.light < 0:
            self.light = 0

    def increase_light(self, amount):
        self.light += amount
        if self.light > self.max_light:
            self.light = self.max_light

    def draw(self, screen):
        pygame.draw.circle(screen, FLASHLIGHT_COLOR, (self.x, self.y), self.light)

    def is_out_of_light(self):
        return self.light <= 0

