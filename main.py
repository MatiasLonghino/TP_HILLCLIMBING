from src.algoritmo import HillClimbing
from src.grafica import graficarCaminata, graficarEvolucionFitness
from src.funciones import parabola

#Variables iniciales
n_variables = 1
bounds = [(-5,5) for i in range(n_variables)]
x0 = [row[1] for row in bounds] # punto inicial en una de las esquinas
max_eps = 0.5
cant_iterac = 20
resolution_grafico = 0.1

#Llamada a algoritmo HillClimbing
X_mejor, fX_mejor, Trace_R, Trace_X, Trace_X_mejor, Trace_f = HillClimbing(
    parabola, x0, max_eps, bounds, cant_iterac)

print("-----")
print("Solución: {0}".format(X_mejor))
print("Fitness: {0}".format(fX_mejor))
print("Iteraciones: {0}".format(len(Trace_X)-1))


#Graficas
graficarEvolucionFitness(Trace_f)
graficarCaminata(parabola, Trace_X_mejor, bounds, resolution_grafico)
