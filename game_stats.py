from scoreboard import  Scoreboard

class GameStats():
    """ 跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """ 初始化统计信息"""
        self.ai_settings = ai_settings
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 在任何情况下都不应该重置最高得分
        self.high_score = 0
        self.high_score_text = "high_score.txt"
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = self.read_high_score()

    def save_high_score(self):
        with open(self.high_score_text, "w") as f:
            f.write(str(self.high_score))

    def read_high_score(self):
        with open(self.high_score_text, "r") as f:
            try:
                hscore = int(f.read())
            except ValueError:
                self.save_high_score()
                hscore = int(f.read())

            return hscore



