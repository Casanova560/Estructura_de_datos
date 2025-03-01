class PlayComparator:
    def compare(self, obj1, obj2):
        # Comparar por fecha
        if obj1.get_fecha() < obj2.get_fecha():
            return -1
        elif obj1.get_fecha() > obj2.get_fecha():
            return 1

        # Comparar por cuarto
        if obj1.get_cuarto() < obj2.get_cuarto():
            return -1
        elif obj1.get_cuarto() > obj2.get_cuarto():
            return 1

        # Comparar por yardas
        if obj1.get_yardas() < obj2.get_yardas():
            return -1
        elif obj1.get_yardas() > obj2.get_yardas():
            return 1

        # Comparar por hora
        if obj1.get_hora() < obj2.get_hora():
            return -1
        elif obj1.get_hora() > obj2.get_hora():
            return 1

        return 0
