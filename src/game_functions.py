# coding=utf-8
import sys
import pygame


def check_keydown_events(event, rocket):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True


def check_keyup_events(event, rocket):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False


def check_events(rocket):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(ai_settings, screen, rocket):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    rocket.blitme()

    pygame.display.flip()
