import pygame
import random


class Enemy:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.y = y  # 添加 y 属性


# 初始化 Pygame
pygame.init()

# 游戏窗口的宽度和高度
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("飞机大战")

# 加载玩家飞机图像
try:
    player_image = pygame.image.load("sources/smallfighter0001.png")
    player_rect = player_image.get_rect()
    player_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
except pygame.error as e:
    print("无法加载图像:", e)
    pygame.quit()
    exit()

# 加载敌人飞机图像
try:
    enemy_image = pygame.image.load("sources/smallfighter0002.png")
    enemy_rect = enemy_image.get_rect()
except pygame.error as e:
    print("无法加载图像:", e)
    pygame.quit()
    exit()

# 创建敌人飞机列表
enemies = []

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动玩家飞机
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # 移动敌人飞机
    for enemy in enemies:
        # 使用 rect.y 来访问 y 坐标
        enemy.rect.y += enemy.speed
        if enemy.rect.y > WINDOW_HEIGHT:
            enemy.rect.x = random.randint(0, WINDOW_WIDTH)
            enemy.rect.y = 0

    # 绘制背景
    window.fill(BLACK)

    # 绘制玩家飞机
    window.blit(player_image, player_rect)

    # 绘制敌人飞机
    for enemy in enemies:
        window.blit(enemy_image, enemy.rect)

    pygame.display.update()
    # 减慢敌人飞机的下落速度
    if len(enemies) < 5:
        new_enemy = Enemy(enemy_image, random.randint(0, WINDOW_WIDTH), 0, 1)
        enemies.append(new_enemy)
    # 增加一个事件循环，用于监听用户按键事件
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # 当用户按下上键时，减慢敌人的速度
                for enemy in enemies:
                    enemy.speed -= 1
            elif event.key == pygame.K_DOWN:
                # 当用户按下下键时，加快敌人的速度
                for enemy in enemies:
                    enemy.speed += 1

    # 在屏幕左上角显示敌人的移动速度
    # bug修复：添加了enemy变量的定义
    # bug修复：添加了font变量的定义
    font = pygame.font.Font(None, 36)
    for enemy in enemies:
        text = font.render(f"Enemy Speed: {enemy.speed}", True, WHITE)
        window.blit(text, (10, 10))

    # 随机生成敌人
    # bug修复：添加了敌人数量上限的控制
    if len(enemies) < 5:
        if random.randint(0, 100) < 5:
            new_enemy = Enemy(enemy_image, random.randint(0, WINDOW_WIDTH), 0, 1)
            enemies.append(new_enemy)
