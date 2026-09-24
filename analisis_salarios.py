"""Análisis de salarios de los empleados (datos ya limpios de la Subsección 1 del taller)."""
import pandas as pd

# Parámetros del análisis
PORCENTAJE_BONO = 0.12
UMBRAL_SALARIO_ALTO = 5.5

datos = {
    "Nombre": ["Mariana", "Esteban", "Camilo", "Juliana", "Nicolas", "Paula",
               "Sebastian", "Laura", "Andres", "Catalina", "Manuela"],
    "Genero": ["Mujer", "Hombre", "Hombre", "Mujer", "Hombre", "Mujer",
               "Hombre", "Mujer", "Hombre", "Mujer", "Mujer"],
    "Departamento": ["Marketing", "Ventas", "IT", "Marketing", "Ventas", "Marketing",
                     "IT", "Marketing", "Finanzas", "Marketing", "Finanzas"],
    "Salario": [3.8, 4.2, 6.0, 3.2, 4.0, 3.9, 6.3, 3.7, 4.5, 5.5, 3.6],
    "AñosExperiencia": [2, 5, 10, 3, 7, 4, 15, 3, 9, 6, 8],
}
df = pd.DataFrame(datos)

# Nuevas variables
df["Bono"] = df["Salario"] * PORCENTAJE_BONO
df["SalarioAlto"] = df["Salario"] > UMBRAL_SALARIO_ALTO

# Resumen por departamento
resumen = df.groupby("Departamento")["Salario"].agg(["mean", "max"])

print(df[["Nombre", "Departamento", "Salario", "Bono", "SalarioAlto"]])
print("\nResumen por departamento:")
print(resumen)
