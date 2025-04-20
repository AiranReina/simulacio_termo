import numpy as np
import matplotlib.pyplot as plt


#################################
# ---- PARÀMETRES NECESARIS --- #
#################################


k_b = 1 # Constant de Boltzmann (J/K)
d = 3 # Dimensions (Per canviar a 1D, 2D o 3D, canviar aquest valor per 1, 2 o 3)

N = 1000 # Nombre de partícules
m = 1 # Massa d'una partícula (Normalitzada)
L = 1 # Longitud del sistema (Normalitzada)
T = 1 # Temperatura (Normalitzada)

steps = 10000 # Passos de Monte Carlo
delta = 0.1 # Pas màxim per proposar nous estats


#################################
# ---- CONDICIONS INICIALS ---- #
#################################


x = np.random.uniform(0, L, size=(N, d)) # Posicions inicials aleatòries
v = np.random.normal(0, np.sqrt(k_b * T / m), size=(N, d)) # Velocitats inicials aleatòries
E = [] # Llista per emmagatzemar l'energia total a cada pas


#################################
# ----- ENERGIA A CADA PAS ---- #
#################################


# Creem un bucle per a cada pas del Monte Carlo.

# El bucle proposa un nou estat per a una particula aleatòria i ...
#... l'accepta sempre, d'acord amb la regla de Metropolis.

# Les velocitats es generen aleatòriament per a cada pas (Degut a les collisions ...
#... entre partícules), d'acord amb la distribució de Maxwell-Boltzmann.

# Per asegurar que les partícules no surtin del sistema, s'utilitzaràn condicions ...
#... de contorn periòdiques.


for step in range(steps):
    i = np.random.randint(N)
    new_xi = x[i] + np.random.uniform(-delta, delta, size=d)
    new_xi = new_xi % L

    x[i] = new_xi
    v = np.random.normal(0, np.sqrt(k_b * T / m), size=(N, d))
    energia = (m/2) * np.sum(v ** 2)
    E.append(energia)


#################################
# --------- RESULTATS --------- #
#################################


# Valors per calcular la fluctuació de l'energia
E_squared = [energia ** 2 for energia in E]
Emean_squared = (np.mean(E))**2

# Càlcul de les capacitats calorífiques
cv_montecarlo = (np.mean(E_squared) - Emean_squared) / (k_b * T**2)
cv_t = (d/2) * N * k_b

# Prints dels resultats
print("Energia mitjana:", np.mean(E))
print("Capacitat calorifica per Monte Carlo:", cv_montecarlo)
print("Capacitat calorifica Teorica:", cv_t)
print("Error en la capacitat calorifica:", round(abs(cv_montecarlo - cv_t) / cv_t * 100, 2), "%")