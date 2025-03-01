from punt_play import PuntPlay

class LectorData:
    def __init__(self, carpeta):
        self.carpeta = carpeta

    def leer_jugadas(self, archivo):
        print(f"\n🔹 Procesando el archivo correspondiente al año: {archivo.split('_')[1].split('.')[0]}")

        jugadas = []
        ruta_completa = self.carpeta + "/" + archivo

        try:
            with open(ruta_completa, "r", encoding="utf-8") as f:
                
                encabezado = [col.lower().replace(".", "").replace("_", "") for col in f.readline().strip().split(",")]

                try:
                    
                    idx_game_id = encabezado.index("gameid")
                    idx_qtr = encabezado.index("qtr")
                    idx_desc = encabezado.index("desc")
                    idx_yards = encabezado.index("yardsgained")
                    idx_away = encabezado.index("posteam")
                    idx_home = encabezado.index("defensiveteam")
                    idx_fecha = encabezado.index("date")
                    idx_hora = encabezado.index("time")
                except ValueError:
                    print(f"Columnas incorrectas en {archivo}. Verifique los encabezados.")
                    return []

                
                for linea in f:
                    columnas = linea.strip().split(",")
                    if len(columnas) <= max(idx_game_id, idx_qtr, idx_desc, idx_yards, idx_away, idx_home, idx_fecha, idx_hora):
                        continue

                    descripcion = columnas[idx_desc].lower()
                    if "punt" in descripcion and "fumble" not in descripcion:
                        game_id = columnas[idx_game_id]
                        equipos = f"{columnas[idx_away]} @ {columnas[idx_home]}"
                        yardas = columnas[idx_yards]
                        cuarto = columnas[idx_qtr]
                        fecha = columnas[idx_fecha]
                        hora = columnas[idx_hora]

                        jugadas.append(PuntPlay(game_id, equipos, yardas, cuarto, fecha, hora))

        except FileNotFoundError:
            print(f" Archivo NO encontrado: {archivo}")

        return jugadas

    def procesar_todos_los_archivos(self):
        """
        Procesa los archivos uno por uno
        """
        archivos = [
            "pbp_2009.csv",  # Archivo con datos del 2009
            "pbp_2010.csv",  # Archivo con datos del 2010
            "pbp_2011.csv",  # Archivo con datos del 2011
            "pbp_2012.csv",  # Archivo con datos del 2012
            "pbp_2013.csv",  # Archivo con datos del 2013
            "pbp_2014.csv",  # Archivo con datos del 2014
            "pbp_2015.csv",  # Archivo con datos del 2015
            "pbp_2016.csv",  # Archivo con datos del 2016
            "pbp_2017.csv",  # Archivo con datos del 2017
        ]

        
        for archivo in archivos:
            print(f"\n🔹 Leyendo y procesando las jugadas del año correspondiente al archivo: {archivo.split('_')[1].split('.')[0]}...")
            yield archivo, self.leer_jugadas(archivo)
