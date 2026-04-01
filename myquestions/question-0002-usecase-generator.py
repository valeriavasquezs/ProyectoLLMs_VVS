# question-0002-usecase-generator.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance

def generar_caso_de_uso_calcular_importancia_permutacion():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función calcular_importancia_permutacion.
    """
    np.random.seed(None)
    
    n_samples = np.random.randint(50, 150)
    n_features = np.random.randint(3, 6)
    
    # Generar características
    X = np.random.randn(n_samples, n_features)
    
    # Crear target con relación lineal a algunas características y ruido
    true_coefs = np.random.choice([0, 1, 2], size=n_features, p=[0.4, 0.3, 0.3])
    y = X @ true_coefs + np.random.randn(n_samples) * 0.5
    
    # Crear nombres de columnas
    feature_names = [f'feature_{chr(97+i)}' for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    target_name = 'target_variable'
    df[target_name] = y
    
    # --- Calcular Output Esperado ---
    X_data = df.drop(columns=[target_name])
    y_data = df[target_name]
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_data, y_data)
    
    result = permutation_importance(model, X_data, y_data, n_repeats=5, random_state=42)
    importancias_esperadas = result.importances_mean
    
    input_data = {'df': df, 'target_col': target_name}
    output_data = importancias_esperadas
    
    return input_data, output_data

if __name__ == "__main__":
    entrada, salida = generar_caso_de_uso_calcular_importancia_permutacion()
    print("Importancias:", salida)