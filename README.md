# SPACIAL PROGRAMMING - GUÍA DE INSTALACIÓN Y TALLER DE POO

Guía de instalación y ejecución del proyecto.

---

## 1. CÓMO INSTALAR EL PROYECTO

Clona o descarga la carpeta del proyecto y abre tu terminal en ella:
```bash
cd spacial-programming
```

### Paso 1: Crear el Entorno Virtual (`.venv`) con Python 3.12
- **En macOS / Linux**:
  ```bash
  python3.12 -m venv .venv
  ```
- **En Windows (CMD / PowerShell)**:
  ```cmd
  py -3.12 -m venv .venv
  ```

### Paso 2: Activar el Entorno Virtual
- **En macOS / Linux**:
  ```bash
  source .venv/bin/activate
  ```
- **En Windows (CMD / PowerShell)**:
  ```cmd
  .venv\Scripts\activate
  ```

### Paso 3: Instalar las Dependencias (`pgzero` y `pygame`)
Con el entorno virtual activado, instala las dependencias del proyecto:
```bash
pip install -r requirements.txt
```

---

## 2. CÓMO EJECUTAR EL JUEGO

Con el entorno virtual activado (`.venv`), ejecuta el juego con cualquiera de estos dos comandos:

### Opción A (Recomendada con Auto-reinicio al guardar con Ctrl + S):
```bash
python watch.py
```

### Opción B (Ejecución directa):
```bash
pgzrun main.py
```

---

## 3. USO DE FUENTES TIPOGRAFICAS (.TTF / .OTF)

Para cambiar la fuente de texto de todo el juego (Menu, Puntaje, Marcador, Vidas, Pantalla de Victoria y Game Over):

1. Descarga cualquier archivo de fuente con extension `.ttf` o `.otf` (por ejemplo `arcade.ttf`).
2. Guardalo dentro de la carpeta:
   `fonts/`
3. El juego detectara automaticamente tu archivo `.ttf` o `.otf` y aplicara esa tipografia a todo el juego.

---

## 4. ESTRUCTURA DEL PROYECTO

```
spacial-programming/
│
├── main.py                   # Punto de entrada principal (Pygame Zero)
├── README.md                 # Guia de instalacion y didactica
├── requirements.txt          # Dependencia (pgzero)
│
├── fonts/                    # Carpeta para colocar archivos .ttf o .otf
│
├── images/                   # Carpeta para colocar tus imagenes PNG
│   ├── player/               # Imagenes de la nave del jugador (spaceship.png)
│   ├── enemies/              # Imagenes de enemigos y boss (alien.png, boss.png)
│   ├── bullets/              # Imagenes de proyectiles
│   ├── backgrounds/          # Imagenes de fondo de pantalla
│   └── effects/              # Imagenes de explosiones
│
└── game/
    ├── player.py             # ARCHIVO DE TRABAJO DE LOS ESTUDIANTES (Clase Player)
    ├── enemy.py              # Clase Enemy
    ├── boss.py               # Clase Boss (Jefe final tipo Metal Slug)
    ├── bullet.py             # Clases Bullet y EnemyBullet (Herencia)
    ├── explosion.py          # Clase Explosion
    ├── background.py         # Modulo de fondo continuo
    ├── ui.py                 # Renderizado de la interfaz
    ├── waves.py              # Administrador de enemigos
    ├── collisions.py         # Administrador de colisiones
    └── game_manager.py       # Controlador principal del juego
```

---

## 5. GUÍAS SEMANALES Y PLAN DE CLASE DE POO

Para seguir el taller paso a paso divido en semanas o clases, consulta los documentos oficiales:

1. **[SEMANA 1: La Nave del Jugador y Movimiento](WEEK1.md)**
   - Creación de atributos con `self`, carga de imágenes personalizadas, programación del movimiento (UP, DOWN, LEFT, RIGHT) y límites de pantalla con `half_width`/`half_height`.
2. **SEMANA 2: Disparos, Balas y Colisiones** *(🔒 Se desbloquea el siguiente jueves)*
   - Cadencia de disparos (`cooldown`), generación de proyectiles (`Bullet`), movimiento de balas y sistema de colisiones con `colliderect`.
3. **SEMANA 3: Proyecto Final y Rúbrica de 50 Puntos** *(🔒 Se desbloquea el siguiente jueves)*
   - Rúbrica oficial de evaluación por 50 puntos y lista de verificación final para el estudiante.

