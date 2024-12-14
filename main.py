import pygame

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 游戏标题
pygame.display.set_caption("魂斗罗游戏")

# 游戏时钟
clock = pygame.time.Clock()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height - 50

    def update(self):
        # 获取键盘输入
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5


import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 30)
        self.rect.y = random.randint(0, screen_height - 30)
        self.direction = 1  # 初始方向为向右

    def update(self):
        # 敌人AI逻辑
        self.rect.x += self.direction * 2  # 每次移动2个像素
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction *= -1  # 碰到边界时改变方向


# 创建玩家和敌人组
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
enemies = pygame.sprite.Group()

# 创建10个敌人
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新所有精灵
    all_sprites.update()

    # 绘制屏幕
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # 更新屏幕
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(60)

# 退出游戏
pygame.quit()
