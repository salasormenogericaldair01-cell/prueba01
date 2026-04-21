from datetime import datetime

def calcular_contador_semanas(fecha_inicio_str):
    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y")
        fecha_actual = datetime.now()

        diferencia = fecha_actual - fecha_inicio
        
        total_semanas = diferencia.days // 7
        dias_extra = diferencia.days % 7

        print(f"--- Reporte de Tiempo ---")
        print(f"Fecha de inicio: {fecha_inicio.strftime('%d de %B, %Y')}")
        print(f"Fecha actual:   {fecha_actual.strftime('%d de %B, %Y')}")
        print(f"-------------------------")
        print(f"Total: {total_semanas} semanas y {dias_extra} días.")
        
    except ValueError:
        print("Error: El formato de fecha debe ser DD/MM/AAAA")

fecha_proyecto = "01/01/2026" 
calcular_contador_semanas(fecha_proyecto)
# los mejores proyectos se hacen con tiempo, paciencia y dedicación.