estudiante = {
    "nombre": "",
    "calificaciones": [],
    "promedio": 0
}

ramos = (
    "Álgebra lineal",
    "Aplicaciones web",
    "Bases de datos",
    "Ingeniería de software",
    "Estructuras de datos"
)

print("******************")
print("*** Bienvenido ***")
print("******************")

while True:
    print("\nIngrese el nombre del estudiante:")
    nombre = input(">>> ")
    if nombre == "":
        print("Error: Debe ingresar un nombre.")
    else:
        estudiante["nombre"] = nombre
        break

print("\nA continuación, debe introducir las calificaciones del estudiante.")

for ramo in ramos:
    while True:
        try:
            cal = float(input(f"\nCalificación de {ramo}: "))
        except ValueError:
            print("Error: Formato de calificación no válido. El formato es: N, donde 1.0 <= N <= 7.0")
        else:
            if cal < 1.0 or cal > 7.0:
                print("Error: Calificación fuera de rango. El rango es 1.0 <= N <= 7.0")
            else:
                estudiante["calificaciones"].append(cal)
                break

estudiante["promedio"] = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])

print("\n\n***** RESUMEN *****")
print(f"Nombre del estudiante: {estudiante["nombre"]}")
print("--- Notas ---")
for k in range(len(estudiante["calificaciones"])):
    print(f"{ramos[k]}:".ljust(max((len(ramo) for ramo in ramos)) + 2) + f"{estudiante["calificaciones"][k]}")
print(f"PROMEDIO: {round(estudiante["promedio"], ndigits=2)}")
