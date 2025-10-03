respuesta ="S"
while respuesta == "S":
    distancia_km = 225000000
    velocidad_kmh = int(input("velocidad: "))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    respuesta= input("quieres hacer otra simulación? (s/n):").lower()