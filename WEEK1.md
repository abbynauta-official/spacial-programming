# GUÍA SEMANA 1: LA NAVE DEL JUGADOR Y MOVIMIENTO

Esta guía contiene todos los pasos detallados para completar la **Semana 1** del proyecto. El estudiante trabajará principalmente en el archivo `game/player.py`.

---

## 📋 OBJETIVOS DE LA SEMANA 1
1. Comprender la estructura de una Clase en Python (`Player`).
2. Definir atributos con `self` (`speed`, `lives`, etc.).
3. Personalizar la imagen de la nave espacial.
4. Programar el movimiento en las 4 direcciones (Arriba, Abajo, Izquierda, Derecha).
5. Aplicar límites de pantalla dinámicos usando la mitad del ancho y alto de la nave.
6. Entender cómo el motor del juego (`game/game_manager.py`) instancializa y mueve la nave.

---

## 🛠️ PASO A PASO DE LA SEMANA 1

### PASO 1: Definir Atributos (`__init__`)
Abre `game/player.py`. Dentro del método `__init__(self)` definimos las variables de la nave usando `self.`:

```python
# game/player.py
class Player:
    def __init__(self):
        # 1. ATRIBUTOS DEL JUGADOR
        self.width = 60
        self.height = 40
        self.position_player_x = 100
        self.position_player_y = 300
        self.score = 0
        self.lives = 5      # Vidas de tu nave
        self.speed = 7      # Velocidad de movimiento
```

---

### PASO 2: Cargar tu propia Imagen de Nave
1. Descarga una imagen de nave espacial en formato PNG sin fondo transparente.
2. Guarda el archivo dentro de la carpeta:
   `images/player/mi_nave.png`
3. En `game/player.py`, reemplaza la ruta por el nombre de tu archivo (sin la extensión `.png`):

```python
imagen_name = "player/mi_nave" # Nombre de tu imagen en images/player/
```

---

### PASO 3: Programar el Movimiento (`move`)
En la pantalla de Pygame, la esquina superior izquierda es la coordenada `(0, 0)`:
- **Subir**: Restamos en Y (`self.actor.y -= self.speed`).
- **Bajar**: Sumamos en Y (`self.actor.y += self.speed`).
- **Ir a la Izquierda**: Restamos en X (`self.actor.x -= self.speed`).
- **Ir a la Derecha**: Sumamos en X (`self.actor.x += self.speed`).

Completa la función `move` en `game/player.py`:

```python
def move(self, keyboard, keys):
    # Arriba (Flecha Arriba)
    if keyboard[keys.UP]:
        self.actor.y -= self.speed

    # Abajo (Flecha Abajo)
    if keyboard[keys.DOWN]:
        self.actor.y += self.speed

    # Izquierda (Flecha Izquierda)
    if keyboard[keys.LEFT]:
        self.actor.x -= self.speed

    # Derecha (Flecha Derecha)
    if keyboard[keys.RIGHT]:
        self.actor.x += self.speed
```

---

### PASO 4: Límites de Pantalla Dinámicos
Para evitar que la nave se salga del borde de la pantalla de `WIDTH` x `HEIGHT`, calculamos la mitad del ancho y del alto de la nave:

```python
    # Límites de Pantalla
    half_width = self.width // 2
    half_height = self.height // 2

    # Límite Izquierdo
    if self.actor.x < half_width:
        self.actor.x = half_width

    # Límite Derecho
    if self.actor.x > WIDTH - half_width:
        self.actor.x = WIDTH - half_width

    # Límite Superior
    if self.actor.y < half_height:
        self.actor.y = half_height

    # Límite Inferior
    if self.actor.y > HEIGHT - half_height:
        self.actor.y = HEIGHT - half_height
```

---

### PASO 5: ¿Cómo se conecta con `game_manager.py`?
Es muy importante comprender cómo el motor principal del juego hace funcionar tu código de `player.py`:

1. **Instanciación:** En `game/game_manager.py`, cuando inicia la partida (`start_game`), se crea la nave diciendo:
   ```python
   self.player = Player()
   ```
2. **Ciclo de Actualización (*Update Loop*):** En cada cuadro del juego, `game_manager.py` llama al método que acabas de programar:
   ```python
   self.player.move(keyboard, keys)
   ```
3. **Renderizado (*Draw Loop*):** Para mostrar tu nave en la pantalla, `game_manager.py` llama a:
   ```python
   self.player.draw()
   ```

---

### 🚀 PRUEBA TU CÓDIGO
Ejecuta el auto-reloader en tu terminal:
```bash
python3 watch.py
```
Guarda tus cambios con **`Ctrl + S`** y verás tu nave moverse por la pantalla.
