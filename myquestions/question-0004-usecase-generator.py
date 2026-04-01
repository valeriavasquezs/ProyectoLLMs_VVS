# question-0004-usecase-generator.py
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def generar_caso_de_uso_angulo_primeras_componentes():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función angulo_primeras_componentes.
    """
    np.random.seed(None)
    
    n_samples = np.random.randint(50, 100)
    n_features = np.random.randint(3, 6)
    
    # Crear un conjunto de datos base
    X_base = np.random.randn(n_samples, n_features)
    
    # Crear df1: un pequeño ruido sobre el base
    df1 = pd.DataFrame(X_base + np.random.randn(n_samples, n_features) * 0.1)
    
    # Crear df2: rotar la base para tener una dirección de varianza diferente
    # Generar una matriz de rotación aleatoria
    Q, _ = np.linalg.qr(np.random.randn(n_features, n_features))
    X_rotated = X_base @ Q.T
    df2 = pd.DataFrame(X_rotated + np.random.randn(n_samples, n_features) * 0.1)
    
    # --- Calcular Output Esperado ---
    pca1 = PCA(n_components=1)
    pca1.fit(df1)
    v1 = pca1.components_[0]
    
    pca2 = PCA(n_components=1)
    pca2.fit(df2)
    v2 = pca2.components_[0]
    
    # Calcular ángulo
    cos_angle = np.abs(np.dot(v1, v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    angulo_esperado = np.arccos(cos_angle)
    
    input_data = {'df1': df1, 'df2': df2}
    output_data = angulo_esperado
    
    return input_data, output_data

if __name__ == "__main__":
    entrada, salida = generar_caso_de_uso_angulo_primeras_componentes()
    print("Ángulo (radianes):", salida)
    print("Ángulo (grados):", np.degrees(salida))