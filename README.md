# Red Neuronal Simple para Clasificación Par/Impar

Este script implementa una red neuronal básica usando TensorFlow/Keras para clasificar números como pares o impares.

## Descripción

El script red.py implementa una red neuronal simple que:

1. Utiliza un conjunto de datos de entrenamiento de 10 números (1-10)
2. Clasifica los números como par (1) o impar (0)
3. Usa una única neurona para realizar la clasificación
4. Predice si un número nuevo (12) es par o impar

## Requisitos

- Python 3.x
- NumPy
- TensorFlow

## Estructura del Modelo

- Capa de entrada: 1 neurona (input_shape=[1])
- Optimizador: Adam
- Función de pérdida: Error cuadrático medio (mean_squared_error)
- Épocas de entrenamiento: 1000

## Uso

```python
# Ejecutar el script
python red.py

# La salida mostrará la probabilidad de que el número 12 sea par
```

## Ejemplo de Salida

```
¿12 es par? Probabilidad: ~1.0
```

Nota: Este es un ejemplo educativo simple. Para casos reales de clasificación par/impar, una simple operación matemática (n % 2 == 0) sería más apropiada.