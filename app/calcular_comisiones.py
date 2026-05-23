import pandas as pd
import os

data = {
    "vendedor": ["Ana", "Luis", "Carlos", "María"],
    "ventas": [5000, 8000, 3000, 10000]
}

df = pd.DataFrame(data)
df["comision"] = df["ventas"] * 0.10

os.makedirs("/app/output", exist_ok=True)
df.to_excel("/app/output/comisiones.xlsx", index=False)

print("Archivo Excel de comisiones generado correctamente.")
