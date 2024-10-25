import csv

def analizar_datos():
    with open('research/datos_recoleccion.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Sistema: {row['sistema']}, Estado: {row['estado']}")

if __name__ == '__main__':
    analizar_datos()
