# Proyecto: Programación con LLMs - FASE 1

**Nombre:** Valeria Vásquez Sánchez
**Correo institucional:** valeria.vasquezs@udea.edu.co

## Descripción
Este repositorio contiene las 4 preguntas creadas para la FASE 1 del proyecto "Programación con LLMs".

## Estructura del repositorio
```
proyecto1-llm/
├── README.md
├── myquestions/
│   ├── question-0001.txt
│   ├── question-0001-usecase-generator.py
│   ├── question-0002.txt
│   ├── question-0002-usecase-generator.py
│   ├── question-0003.txt
│   ├── question-0003-usecase-generator.py
│   ├── question-0004.txt
│   └── question-0004-usecase-generator.py
└── myanswers/
    └── (vacío para FASE 2)
```


## Preguntas creadas

| ID | Función | Descripción |
|---|---|---|
| 0001 | `ajustar_curva_aprendizaje` | Regresión isotónica para modelar curvas de aprendizaje con monotonicidad garantizada |
| 0002 | `calcular_importancia_permutacion` | Selección de variables mediante permutación con RandomForestRegressor |
| 0003 | `detectar_quiebres_ventas` | Detección de anomalías en series temporales usando media móvil |
| 0004 | `angulo_primeras_componentes` | Medición de similitud entre espacios PCA mediante ángulo entre componentes |

## Validación de generadores

Cada generador produce casos de uso aleatorios y ha sido probado exitosamente:

- `question-0001-usecase-generator.py` - Produce MAE para curvas de aprendizaje
- `question-0002-usecase-generator.py` - Produce importancias por permutación
- `question-0003-usecase-generator.py` - Produce número de quiebres en series temporales
- `question-0004-usecase-generator.py` - Produce ángulo entre componentes principales

## Nota
La carpeta `myanswers/` permanece vacía para la FASE 2, donde se agregarán las soluciones a las preguntas asignadas por otros compañeros.