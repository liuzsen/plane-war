import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 设置标题
pygame.display.set_caption("飞机大战")

# 设置背景颜色
BLACK = (0, 0, 0)


# 创建玩家飞机类
class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (x, y)
        self.bullets = []  # 玩家的炮弹列表
        self.score = 0  # 玩家的分数


# 创建敌人飞机类
class Enemy:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed


# 创建炮弹类
class Bullet:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (x, y)


# 加载玩家飞机图片
player_image = pygame.image.load("sources/player.png")
player = Player(player_image, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)

# 加载敌人飞机图片
enemies = []

# 加载炮弹图片
bullet_image = pygame.image.load("sources/bullet.png")

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 玩家按空格键发射炮弹
                bullet = Bullet(bullet_image, player.rect.centerx, player.rect.top)
                player.bullets.append(bullet)

    # 移动玩家飞机
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    # 随机生成敌人
    if random.random() < 0.01:  # 1% 的概率生成敌人
        enemy_image = pygame.image.load("sources/smallfighter0002.png")
        enemy_x = random.randint(0, WINDOW_WIDTH - enemy_image.get_width())
        enemy_y = 0
        enemy_speed = 2  # 固定速度
        enemy = Enemy(enemy_image, enemy_x, enemy_y, enemy_speed)
        enemies.append(enemy)

    # 移动敌人飞机
    for enemy in enemies:
        enemy.rect.y += enemy.speed
        if enemy.rect.y > WINDOW_HEIGHT:
            enemies.remove(enemy)
        elif player.rect.colliderect(enemy.rect):  # 玩家与敌人碰撞
            running = False
            player.score -= 100  # 扣除 100 分

    # 移动炮弹
    for bullet in player.bullets:
        bullet.rect.y -= 5
        if bullet.rect.y < 0:
            player.bullets.remove(bullet)

    # 碰撞检测：炮弹与敌人
    for bullet in player.bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                enemies.remove(enemy)
                player.bullets.remove(bullet)
                player.score += 100  # 增加 100 分

    # 绘制分数
    score_text = pygame.font.SysFont("Arial", 24).render(
        "Score: " + str(player.score), True, (255, 255, 255)
    )
    window.blit(score_text, (10, 10))

    # 清除屏幕
    window.fill(BLACK)

    # 绘制玩家飞机
    window.blit(player.image, player.rect)

    # 绘制敌人飞机
    for enemy in enemies:
        window.blit(enemy.image, enemy.rect)

    # 绘制炮弹
    for bullet in player.bullets:
        window.blit(bullet.image, bullet.rect)

    # 绘制分数
    score_text = pygame.font.SysFont("Arial", 24).render(
        "Score: " + str(player.score), True, (255, 255, 255)
    )
    window.blit(score_text, (10, 10))

    # 更新游戏窗口
    pygame.display.flip()
    pygame.time.Clock().tick(60)


# 游戏结束
print("Game Over!")

# 退出 Pygame
pygame.quit()
