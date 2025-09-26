distancia_km = int(input("distancia recorrida: "))
velocidad_kmh = int(input("velocidad: "))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")