# coding=utf-8
import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, rocket, bullets):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, rocket, bullets)
    elif event.key == pygame.k_q:
        sys.exit()


def fire_bullet(ai_settings, screen, rocket, bullets):
    """如果还没有达到极限，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets.allowed:
        new_bullet = Bullet(ai_settings, screen, rocket)
        bullets.add(new_bullet)


def check_keyup_events(event, rocket):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False


def check_events(ai_settings, screen, rocket, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(ai_settings, screen, rocket, alien, bullets):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    alien.blitme()

    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已超出屏幕的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
