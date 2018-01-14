# coding=utf-8
import pygame
from pygame.sprite import Group
from setting import Settings
from rocket import Rocket
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shooting ET!")

    # 创建飞船
    rocket = Rocket(ai_settings, screen)
    # 创建用于存储外星人的编组
    aliens = Group()
    # 创建用于存储子弹的编组
    bullets = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, rocket, bullets)
        rocket.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, rocket, aliens, bullets)


run_game()
