import pygame
from pgzero.actor import Actor
from pgzero.loaders import images
from config import WIDTH, HEIGHT

class Player:
    def __init__(self):
        # -------------------------------------------------------------
        # SEMANA 1: ATRIBUTOS DE LA NAVE
        # -------------------------------------------------------------
        # ACTIVIDAD 1: Define aca tus propios atributos usando 'self.'
        # Pista: Revisar WEEK1.md cuando termines de escribir los atributos notaras que tu nave aparecera en pantalla, pero aun no se podra mover
        # Es posible que te salgan errores en la terminal como "AttributeError: 'Player' object has no attribute 'width'" esto es una pista de lo que te falta, solo pon self. seguido del atributo que te falta :)

        # -------------------------------------------------------------
        # Descarga tu propia imagen de nave y guárdala en la carpeta 'images/player/'.
        # Luego, reemplaza "player/spaceship" por el nombre de tu archivo (sin .png o .jpg, o la extension que tenga).
        # -------------------------------------------------------------
        imagen_name = "player/spaceship"

        surf = images.load(imagen_name)
        surf = pygame.transform.scale(surf, (self.width, self.height))
        
        self.actor = Actor(imagen_name, (self.position_player_x, self.position_player_y))
        self.actor._surf = surf
        self.actor._orig_surf = surf
        self.actor._update_pos()

    def move(self, keyboard, keys):
        # -------------------------------------------------------------
        # PROGRAMAR MOVIMIENTO
        # Recuerda la lógica del eje de coordenadas en la pantalla:
        # - Para subir: restamos en Y
        # - Para bajar: sumamos en Y
        # - Para la izquierda: restamos en X
        # - Para la derecha: sumamos en X
        # -------------------------------------------------------------

        # Ejemplo: Mover hacia arriba al presionar la tecla UP
        if keyboard[keys.UP]:
            self.actor.y -= self.speed

        # Completa el movimiento para las demás direcciones:
        # - Mover hacia abajo

        # - Mover hacia la izquierda

        # - Mover hacia la derecha


        # -------------------------------------------------------------
        # LÍMITES DE LA PANTALLA (Semana 1)
        # -------------------------------------------------------------
        half_width = self.width // 2
        half_height = self.height // 2

        if self.actor.x < half_width:
            self.actor.x = half_width
        if self.actor.x > WIDTH - half_width:
            self.actor.x = WIDTH - half_width
        if self.actor.y < half_height:
            self.actor.y = half_height
        if self.actor.y > HEIGHT - half_height:
            self.actor.y = HEIGHT - half_height

    def draw(self):
        self.actor.draw()

    # -----------------------------------------------------------------
    # SEMANA 2: DISPAROS Y RECARGA
    # -----------------------------------------------------------------
    def update_cooldown(self):
        pass

    def shoot(self):
        pass

    # -----------------------------------------------------------------
    # RECIBIR DAÑO Y DAÑO A ENEMIGOS
    # -----------------------------------------------------------------
    def take_damage(self):
        self.lives -= 1
        return self.lives <= 0


