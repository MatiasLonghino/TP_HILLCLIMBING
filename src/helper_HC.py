import random 
import math


def validate_inputs(X_mejor, bounds, cant_iterac, max_eps) -> bool:
    """
    Valida input data used in Hill Climbing algorithm.

    Parameters:
        - X_mejor
        - bounds
        - cant_interac
        - max_eps
    """
    if len(X_mejor) == 0:
        print("La solucion inicial debe tener al menos una variable.")
        return False

    if len(bounds) != len(X_mejor) or len(bounds[0]) != 2:
        print("La matriz de Bounds tiene un tamaño incorrecto.")
        return False

    if cant_iterac < 1:
        print("El número máximo de iteraciones debe ser positivo mayor a cero.")
        return False
    if max_eps <= 0:
        print("El tamaño del paso debe ser real y positivo.")
        return False
    return True

def puntoExploracion(X0, max_eps):
    """Calcular un nuevo punto de exploración o solución, a partir de
    una solución previa.

    Parameters
    ----------
    X0: list
        Vector solucion inicial.
    max_eps: float
        Valor del tamaño máximo del paso.

    Returns
    -------
    X : list
        Vector solución generado.
    R : list
        Vector dirección.
    """
    R = [2*(random.random())-1 for x in X0]
    norma = (math.sqrt(sum(ri**2 for ri in R)))
    R = [ri/norma for ri in R]
    #R = ...
    #...
    #X = ...
    epsilon = max_eps*random.random()
    X = [xi + (epsilon*ri) for xi, ri in zip(X0, R)]
    return X, R