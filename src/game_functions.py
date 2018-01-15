# coding=utf-8
import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, rocket, bullets):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, rocket, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, rocket, bullets):
    """如果还没有达到极限，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
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


def update_screen(ai_settings, screen, rocket, aliens, bullets):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(ai_settings, screen, rocket, aliens, bullets):
    """更新子弹的位置，并删除已超出屏幕的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, rocket, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, rocket, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了敌人
    # 如果是，就删除相应的子弹和敌人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, rocket, aliens)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def rocket_hit(ai_settings, stats, screen, rocket, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.rocket_left > 0:
        # 将rocket_left减1
        stats.rocket_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人， 并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, rocket, aliens)
        rocket.center_rocket()

        # 暂停一会儿
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, rocket, aliens, bullets):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            rocket_hit(ai_settings, stats, screen, rocket, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, rocket, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(rocket, aliens):
        rocket_hit(ai_settings, stats, screen, rocket, aliens, bullets)
    # 检测外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, rocket, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, rocket_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - rocket_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, rocket, aliens):
    """创建外星人群"""
    # 创建一个外星人， 并计算一行可容纳多少
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, rocket.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):  # 创建一行外星人
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
