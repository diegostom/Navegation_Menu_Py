import os
import sys

# Configurar el lector de teclado nativo según el Sistema Operativo
if os.name == 'nt':
    import msvcrt
    def _leer_tecla() -> str:
        """Lee teclas en Windows de forma nativa."""
        ch = msvcrt.getch()
        # En Windows, las flechas y teclas especiales envían un prefijo (0x00 o 0xE0)
        if ch in (b'\x00', b'\xe0'):
            ch = msvcrt.getch() # Leer el segundo byte que identifica la flecha
            if ch == b'H': return 'UP'
            if ch == b'P': return 'DOWN'
            if ch == b'M': return 'RIGHT'
            if ch == b'K': return 'LEFT'
        if ch == b'\r': return 'ENTER'
        try:
            return ch.decode('utf-8', errors='ignore')
        except:
            return ''
else:
    import tty
    import termios
    def _leer_tecla() -> str:
        """Lee teclas en Linux / macOS de forma nativa."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            # En Unix, las flechas envían secuencias de escape que empiezan con \x1b
            if ch == '\x1b':
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch2 == '[':
                    if ch3 == 'A': return 'UP'
                    if ch3 == 'B': return 'DOWN'
                    if ch3 == 'C': return 'RIGHT'
                    if ch3 == 'D': return 'LEFT'
            if ch == '\r' or ch == '\n': return 'ENTER'
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


class MenuConsola:
    def __init__(self, titulo: str = "MENÚ PRINCIPAL", indicador: str = "→"):
        """Inicializa el menú interactivo sin dependencias externas.
        
        :param titulo: El título superior del menú.
        :param indicador: El ícono o emoji que marcará la opción seleccionada.
        """
        self.titulo = titulo
        self.indicador = indicador
        self.opciones = []
        self._posicion_actual = 0 

    def agregar_opcion(self, texto: str, funcion_accion):
        """Añade una opción al menú asociada a una función."""
        self.opciones.append({"texto": texto, "accion": funcion_accion})

    def _limpiar_pantalla(self):
        """Limpia la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _imprimir_menu(self):
        """Dibuja el menú entero destacando la opción actual."""
        self._limpiar_pantalla()
        
        ancho = max(len(self.titulo), 30)
        print("=" * (ancho + 4))
        print(f"  {self.titulo.upper()}  ")
        print("=" * (ancho + 4))
        
        todas_las_opciones = [op["texto"] for op in self.opciones] + ["Salir"]
        
        for indice, texto_opcion in enumerate(todas_las_opciones):
            if indice == self._posicion_actual:
                print(f" {self.indicador} {texto_opcion}")
            else:
                espacio_vacio = " " * len(self.indicador)
                print(f" {espacio_vacio} {texto_opcion}")
                
        print("-" * (ancho + 4))
        print("Usa las flechas (↑ / ↓) y presiona ENTER para seleccionar.")

    def mostrar(self):
        """Inicia el bucle interactivo controlado por teclado nativo."""
        if not self.opciones:
            print("Error: No has agregado opciones al menú.")
            return

        total_opciones = len(self.opciones) + 1 

        while True:
            self._imprimir_menu()
            
            # Capturar la tecla de nuestro lector multiplataforma
            tecla = _leer_tecla()
            
            if tecla == 'UP':
                self._posicion_actual = (self._posicion_actual - 1) % total_opciones
                
            elif tecla == 'DOWN':
                self._posicion_actual = (self._posicion_actual + 1) % total_opciones
                
            elif tecla == 'ENTER':
                if self._posicion_actual == len(self.opciones):
                    print("\n¡Hasta luego!")
                    break
                
                print("\n" + "-" * 30)
                self.opciones[self._posicion_actual]["accion"]()
                print("-" * 30)
                input("\nPresiona ENTER para regresar al menú...")
