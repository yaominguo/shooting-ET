# coding=utf-8
import pygame


class Rocket():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船并获取外形矩阵
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.center += self.ai_settings.speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
