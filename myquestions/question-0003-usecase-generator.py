# question-0003-usecase-generator.py
import pandas as pd
import numpy as np

def generar_caso_de_uso_detectar_quiebres_ventas():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función detectar_quiebres_ventas.
    """
    np.random.seed(None)
    
    n_days = np.random.randint(60, 120)
    start_date = pd.Timestamp('2023-01-01')
    dates = pd.date_range(start=start_date, periods=n_days, freq='D')
    
    # Crear una señal base con estacionalidad semanal y tendencia
    base = np.linspace(50, 80, n_days)
    seasonal = np.sin(np.linspace(0, 4*np.pi, n_days)) * 10
    noise = np.random.normal(0, 2, n_days)
    ventas = base + seasonal + noise
    
    # Introducir algunos quiebres en días aleatorios
    n_quiebres_reales = np.random.randint(3, 8)
    quiebre_indices = np.random.choice(range(7, n_days-1), size=n_quiebres_reales, replace=False)
    for idx in quiebre_indices:
        ventas[idx] = ventas[idx] * np.random.uniform(1.6, 2.5)
    
    df = pd.DataFrame({'fecha': dates, 'ventas': ventas})
    
    # --- Calcular Output Esperado ---
    df_sorted = df.sort_values('fecha').copy()
    media_movil_7 = df_sorted['ventas'].rolling(window=7).mean()
    # Comparar con el valor del día anterior
    condicion = df_sorted['ventas'] > 1.5 * media_movil_7.shift(1)
    # El primer día no puede tener media móvil del día anterior
    condicion.iloc[0] = False
    # También los primeros 7 días no tienen media móvil válida del día anterior
    condicion.iloc[:7] = False
    n_quiebres_esperados = int(condicion.sum())
    
    input_data = {'df': df}
    output_data = n_quiebres_esperados
    
    return input_data, output_data

if __name__ == "__main__":
    entrada, salida = generar_caso_de_uso_detectar_quiebres_ventas()
    print("Número de quiebres:", salida)