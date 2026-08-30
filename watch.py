import os
import sys
import time
import subprocess

def get_max_mtime(directory):
    max_mtime = 0
    for root, _, files in os.walk(directory):
        if ".venv" in root or "__pycache__" in root or ".git" in root or ".vscode" in root:
            continue
        for f in files:
            if f.endswith(".py") and f != "watch.py":
                filepath = os.path.join(root, f)
                try:
                    mtime = os.path.getmtime(filepath)
                    if mtime > max_mtime:
                        max_mtime = mtime
                except OSError:
                    pass
    return max_mtime

def main():
    print("🚀 ¡Auto-reloader de Pygame Zero activado!")
    print("El juego se iniciará y se reiniciará automáticamente al editar cualquier archivo .py.\n")

    # Comando para iniciar el juego usando python3 main.py (o pgzrun)
    cmd = [sys.executable, "main.py"]
    
    last_mtime = get_max_mtime(".")
    process = subprocess.Popen(cmd)

    try:
        while True:
            time.sleep(0.5)
            current_mtime = get_max_mtime(".")
            
            # Si hay un cambio en algún archivo .py
            if last_mtime > 0 and current_mtime > last_mtime:
                print("\n⚡ ¡Cambio detectado en el código! Reiniciando el juego...")
                last_mtime = current_mtime
                if process and process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=1)
                    except subprocess.TimeoutExpired:
                        process.kill()
                process = subprocess.Popen(cmd)
            elif last_mtime == 0:
                last_mtime = current_mtime

    except KeyboardInterrupt:
        print("\n👋 Auto-reloader detenido.")
        if process and process.poll() is None:
            process.terminate()

if __name__ == "__main__":
    main()
