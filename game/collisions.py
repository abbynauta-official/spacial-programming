from game.explosion import Explosion

class CollisionManager:
    @staticmethod
    def check_collisions(bullets, enemy_bullets, enemies, boss, player, explosions, game):
        for b in bullets[:]:
            for e in enemies[:]:
                if b.actor.colliderect(e.actor):
                    bullets.remove(b)
                    enemies.remove(e)
                    player.score += e.points
                    explosions.append(Explosion(e.actor.x, e.actor.y))
                    break

            if boss and b.actor.colliderect(boss.actor):
                if b in bullets: bullets.remove(b)
                explosions.append(Explosion(b.actor.x, b.actor.y))
                if boss.take_damage(1):
                    game.state = "VICTORY"

        for eb in enemy_bullets[:]:
            if eb.actor.colliderect(player.actor):
                enemy_bullets.remove(eb)
                explosions.append(Explosion(player.actor.x, player.actor.y))
                if player.take_damage():
                    game.state = "GAME_OVER"

        for e in enemies[:]:
            if e.actor.colliderect(player.actor):
                enemies.remove(e)
                explosions.append(Explosion(e.actor.x, e.actor.y))
                if player.take_damage():
                    game.state = "GAME_OVER"

        if boss and boss.actor.colliderect(player.actor):
            explosions.append(Explosion(player.actor.x, player.actor.y))
            if player.take_damage():
                game.state = "GAME_OVER"
