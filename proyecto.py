import pandas as pd
from workalendar.america.chile import Chile
from calendar import monthrange

cal = Chile()
results = []

# Definir los años 
years = [2024, 2025, 2026, 2027]

# Iterar sobre los años y meses
for year in years:
    for month in range(1, 13):  # Meses del 1 al 12
        # Obtener el último día del mes
        last_day = monthrange(year, month)[1]
        dates = pd.date_range(start=f"{year}-{month:02d}-01", end=f"{year}-{month:02d}-{last_day}")
        
        # Contadores de días
        feriados = 0
        dias_trabajados = 0
        
        for date in dates:
            # Un día es feriado si es domingo o está en el calendario de feriados
            if (cal.is_holiday(date) and not (date.month == 12 and date.day == 31)) or date.weekday() == 6:
                feriados += 1
            elif date.weekday() in [0, 1, 2, 3, 4]:  # De lunes a viernes
                dias_trabajados += 1
        
        # Agregar el resultado a la lista
        results.append({
            "Año": year,
            "Mes": month,
            "Días Trabajados": dias_trabajados,
            "Feriados": feriados
        })

# Crear el DataFrame con el resumen
df_resumen = pd.DataFrame(results)
# Crear la columna 'Periodo' utilizando solo las columnas Año y Mes
df_resumen["Periodo"] = pd.to_datetime(
    df_resumen[["Año", "Mes"]].rename(columns={"Año": "year", "Mes": "month"}).assign(day=1)
)

# Reorganizar las columnas
df_resumen = df_resumen[["Periodo", "Días Trabajados", "Feriados"]]

print(df_resumen)