# project1_script.py
import pandas as pd

print("Versión de pandas:", pd.__version__)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

print("Proyecto 1 - DataFrame de Pandas 1.5:")
print(df)
