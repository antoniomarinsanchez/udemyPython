from pathlib import Path
# Ejercicio 1
ruta_base = Path.home()

# Ejercicio 2
from pathlib import Path
ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)

# Ejercicio 3
from pathlib import Path
ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py")
print(ruta)
