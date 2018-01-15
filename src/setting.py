# coding=utf-8
class Settings():
    """存储设置选项"""

    def __init__(self):  # 初始化设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.speed_factor = 1.5
        self.rocket_limit = 3
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60  # 子弹颜色
        self.bullets_allowed = 5  # 限制子弹数
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示右移，-1表示左移
        self.fleet_direction = 1
