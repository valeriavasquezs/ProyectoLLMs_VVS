# question-0001-usecase-generator.py
import pandas as pd
import numpy as np
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import mean_absolute_error

def generar_caso_de_uso_ajustar_curva_aprendizaje():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función ajustar_curva_aprendizaje.
    """
    np.random.seed(None)
    
    n_points = np.random.randint(10, 30)
    x = np.arange(n_points)
    y_true = np.log(x + 1) * np.random.uniform(5, 15)
    y = y_true + np.random.normal(0, 0.5, n_points)
    y = np.clip(y, 0, None)
    
    df = pd.DataFrame({'numero_practica': x, 'puntuacion': y})
    df = df.sample(frac=1).reset_index(drop=True)
    
    df_ordenado = df.sort_values('numero_practica').reset_index(drop=True)
    iso_reg = IsotonicRegression(increasing=True)
    y_pred = iso_reg.fit_transform(df_ordenado['numero_practica'].values, df_ordenado['puntuacion'].values)
    mae_esperado = mean_absolute_error(df_ordenado['puntuacion'], y_pred)
    
    input_data = {'df': df}
    output_data = mae_esperado
    
    return input_data, output_data

if __name__ == "__main__":
    entrada, salida = generar_caso_de_uso_ajustar_curva_aprendizaje()
    print("MAE:", salida)