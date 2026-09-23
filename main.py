class JugadorFutbol:
    def __init__(self, nombre, equipo, media, ritmo, tiro, pase, fisico):
        self.nombre = nombre
        self.equipo = equipo
        self.media = media
        self.stats = {
            "Ritmo": ritmo,
            "Tiro": tiro,
            "Pase": pase,
            "Fisico": fisico
        }

    def celebrar_gol(self):
        print(f"¡{self.nombre} ha marcado un golazo!")
        print("¡¡¡ GOOOOOOOOOOL !!! ⚽🐐")


# Creando la tarjeta de Lionel Messi con sus datos
messi = JugadorFutbol(
    nombre="Lionel Messi",
    equipo="Inter Miami",
    media=99,
    ritmo=92,
    tiro=99,
    pase=99,
    fisico=85
)
