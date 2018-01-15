# coding=utf-8
import pygame
from pygame.sprite import Group

import game_functions as gf
from rocket import Rocket
from setting import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shooting ET!")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建飞船
    rocket = Rocket(ai_settings, screen)
    # 创建用于存储外星人的编组
    aliens = Group()
    # 创建用于存储子弹的编组
    bullets = Group()
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, rocket, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, rocket, aliens, bullets)
        if stats.game_active:
            rocket.update()
            gf.update_bullets(ai_settings, screen, stats, sb, rocket, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, rocket, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, rocket, aliens, bullets, play_button)


run_game()
