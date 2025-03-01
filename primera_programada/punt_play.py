class PuntPlay:
    def __init__(self, game_id, equipos, yardas, cuarto, fecha=None, hora=None):
        self.__game_id = game_id
        self.__equipos = equipos
        self.__yardas = int(yardas) if yardas.isdigit() else 0
        self.__cuarto = int(cuarto) if cuarto.isdigit() else 0
        self.__fecha = fecha
        self.__hora = hora

    def __eq__(self, other):
        return self.__yardas == other.__yardas

    def __lt__(self, other):
        return self.__yardas < other.__yardas

    def __gt__(self, other):
        return self.__yardas > other.__yardas

    def __str__(self):
        return f"{self.__game_id},{self.__equipos},{self.__yardas},{self.__cuarto}"

    def get_game_id(self):
        return self.__game_id

    def get_yardas(self):
        return self.__yardas

    def get_cuarto(self):
        return self.__cuarto

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora
