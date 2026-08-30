from game.player import Player
from game.boss import Boss
from game.background import BackgroundManager
from game.ui import UIManager
from game.waves import WaveManager
from game.collisions import CollisionManager

class GameManager:
    def __init__(self):
        self.state = "MENU"
        self.background = BackgroundManager()
        self.waves = WaveManager()
        
        self.player = None
        self.boss = None
        self.bullets = []
        self.enemy_bullets = []
        self.enemies = []
        self.explosions = []
        self.total_enemies_defeated = 0

    def start_game(self):
        # -------------------------------------------------------------
        # A SE INSTANCIA A TU NAVE AL INICIAR LA PARTIDA:
        # Usamos la clase Player() que definieron en game/player.py
        # -------------------------------------------------------------
        self.player = Player()
        self.boss = None
        self.bullets = []
        self.enemy_bullets = []
        self.enemies = []
        self.explosions = []
        self.total_enemies_defeated = 0
        self.state = "PLAYING"

    def update(self, keyboard, keys):
        self.background.update()

        if self.state != "PLAYING":
            return

        self.player.update_cooldown()
        self.player.move(keyboard, keys)

        if self.player.score >= 1000 and self.boss is None:
            self.boss = Boss()
            self.enemies = []

        if self.boss:
            self.boss.move()
            eb = self.boss.update_shoot()
            if eb:
                self.enemy_bullets.append(eb)
        else:
            self.waves.update(self.enemies, self.player.score, False)

        for b in self.bullets[:]:
            b.move()
            if b.is_off_screen(): self.bullets.remove(b)

        for eb in self.enemy_bullets[:]:
            eb.move()
            if eb.is_off_screen(): self.enemy_bullets.remove(eb)

        for e in self.enemies[:]:
            e.move()
            if e.is_off_screen(): self.enemies.remove(e)

        for exp in self.explosions[:]:
            exp.update()
            if exp.finished: self.explosions.remove(exp)

        CollisionManager.check_collisions(
            self.bullets, self.enemy_bullets, self.enemies, self.boss,
            self.player, self.explosions, self
        )

    def on_key_down(self, key, keys):
        if self.state == "MENU":
            if key in [keys.RETURN, keys.SPACE]:
                self.start_game()
        elif self.state == "PLAYING":
            if key == keys.SPACE:
                new_bullet = self.player.shoot()
                if new_bullet:
                    self.bullets.append(new_bullet)
        elif self.state in ["GAME_OVER", "VICTORY"]:
            if key in [keys.R, keys.SPACE, keys.RETURN]:
                self.state = "MENU"

    def draw(self, screen):
        self.background.draw(screen)

        if self.state == "MENU":
            UIManager.draw_menu(screen)
        elif self.state == "PLAYING":
            self.player.draw()
            if self.boss: self.boss.draw()
            for b in self.bullets: b.draw()
            for eb in self.enemy_bullets: eb.draw()
            for e in self.enemies: e.draw()
            for exp in self.explosions: exp.draw()
            UIManager.draw_hud(screen, self.player, self.boss)
        elif self.state == "GAME_OVER":
            UIManager.draw_game_over(screen, self.player)
        elif self.state == "VICTORY":
            UIManager.draw_victory(screen, self.player)
