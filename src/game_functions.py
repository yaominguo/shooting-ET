# coding=utf-8
import sys
import pygame


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, rocket):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    rocket.blitme()

    pygame.display.flip()
