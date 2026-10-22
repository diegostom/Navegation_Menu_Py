### Navegation Menu PY 🚀

Una librería de Python liviana, multiplataforma y nativa para construir menús interactivos en la consola controlados mediante las flechas del teclado (↑ / ↓), sin necesidad de presionar ENTER para desplazarse. 

### Características ✨

* **Control Nativo:** Navegación fluida por teclado usando librerías nativas del sistema (msvcrt en Windows y termios en Linux/macOS). ¡Cero dependencias externas!
* **Altamente Personalizable:** El programador puede definir el título del menú y el ícono indicador de selección (flechas, emojis, caracteres especiales).
* **Control de Flujo Autónomo:** Integra tus propias funciones o minijuegos y el menú manejará el regreso de manera automática.

### Requisitos Previos 🛠️

Este proyecto utiliza **Poetry** para la gestión de entornos virtuales y dependencias. Para poder ejecutar el script de prueba de manera correcta y con interactividad, es necesario tener instalado Poetry en tu sistema. 

Si no lo tienes instalado, abre tu terminal ejecútalo mediante pip: 

bash

pip install poetry

Usa el código con precaución.

### Instalación y Uso Local 💻

Si deseas clonar este repositorio para probar el menú o jugar al minijuego integrado, sigue estos pasos desde tu terminal real (PowerShell, CMD o Terminal de Linux/macOS): 

1. **Clona el repositorio:** 

bash

git clone https://github.com/diegostom_DEV/navegation_menu_py.git
cd navegation_menu_py

Usa el código con precaución.
2. **Instala el entorno virtual del proyecto:** 

bash

poetry install

Usa el código con precaución.
3. **Ejecuta el menú interactivo:**
Para que las flechas del teclado y la limpieza de pantalla funcionen correctamente, debes inicializar el script de prueba (t.py) a través del entorno seguro de Poetry ejecutando: 

bash

poetry run python t.py

Usa el código con precaución.

### Ejemplo de Código 📝

Así de sencillo es implementar este menú en tus propios scripts: 

python

from navegation_menu_py import MenuConsola

# 1. Define las funciones que ejecutará tu menú
def mi_funcion():
    print("¡Hola desde la librería interactiva!")

# 2. Instancia el menú con tu indicador favorito (flechas, emojis, etc.)
menu = MenuConsola(titulo="Mi Panel de Control", indicador="👉")

# 3. Agrega las opciones asociando el texto con la función
menu.agregar_opcion("Ejecutar Acción", mi_funcion)

# 4. Lanza el menú interactivo
menu.mostrar()

Usa el código con precaución.

### Licencia 📄

Este proyecto está bajo la Licencia MIT. ¡Siéntete libre de usarlo, modificarlo y mejorarlo!
