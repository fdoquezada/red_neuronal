import numpy as np
from tensorflow import keras

# 1. Datos de ejemplo (entrada: números, salida: 0=impar, 1=par)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])  # 0=impar, 1=par

# 2. Crear un modelo SUPER simple (1 neurona)
model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

# 3. Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# 4. Entrenar (ajustar pesos)
model.fit(X, y, epochs=1000, verbose=0)

# 5. Predecir: ¿El número 12 es par o impar?
prediccion = model.predict([12])
print("¿12 es par? Probabilidad:", prediccion[0][0])  # Debería ser ~1 (par)
