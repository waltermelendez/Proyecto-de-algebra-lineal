import numpy as np

# ===============================
# Matriz A y vector B (3 nodos)
# ===============================
A = np.array([[-2, 1, 1],
              [1, -2, 1],
              [1, 1, -2]])

B = np.array([[150],
              [200],
              [150]])

# ===============================
# Funciones auxiliares
# ===============================
def es_invertible(A):
    """Verifica si la matriz A es invertible"""
    return np.linalg.det(A) != 0

def unir_matrices(A, B):
    """Une matrices para mostrar la aumentada"""
    return np.concatenate((A, B), axis=1)

def resolver_sistema_reducido(A, B, nodo_fijo=2):
    """
    Resuelve el sistema reducido fijando un nodo como referencia
    nodo_fijo: índice del nodo que se fija a 0 (0, 1 o 2)
    """
    n = A.shape[0]
    
    # Crear matriz reducida eliminando fila y columna del nodo fijo
    indices = [i for i in range(n) if i != nodo_fijo]
    A_reducida = A[np.ix_(indices, indices)]
    B_reducida = B[indices]
    
    # Resolver sistema reducido
    if es_invertible(A_reducida):
        X_reducida = np.linalg.solve(A_reducida, B_reducida)
        
        # Reconstruir vector solucion completo
        X_completo = np.zeros((n, 1))
        idx = 0
        for i in range(n):
            if i == nodo_fijo:
                X_completo[i] = 0
            else:
                X_completo[i] = X_reducida[idx]
                idx += 1
        
        return X_completo
    else:
        print("La matriz reducida tampoco es invertible")
        return None

def calcular_flujos(X):
    """
    Calcula los flujos entre nodos basado en los potenciales
    f_ij = x_i - x_j (conductancia unitaria)
    """
    n = len(X)
    flujos = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                flujos[i, j] = X[i][0] - X[j][0]  # Acceder al elemento [0] porque X es vector columna
    
    return flujos

def verificar_conservacion(A, X, B):
    """Verifica que se cumpla la conservación: A*X = B"""
    resultado = np.dot(A, X)
    error = np.linalg.norm(resultado - B)
    return resultado, error

def mostrar_resultados_texto(X, flujos, B):
    """Muestra los resultados en formato texto"""
    print("\n" + "="*50)
    print("RESULTADOS DE LA SIMULACIÓN")
    print("="*50)
    
    print("\nPOTENCIALES EN LOS NODOS:")
    nodos = ['Nodo 1', 'Nodo 2', 'Nodo 3']
    for i, nodo in enumerate(nodos):
        print(f"  {nodo}: {X[i][0]:.2f}")
    
    print("\nDEMANDAS DE TRÁFICO:")
    for i, nodo in enumerate(nodos):
        print(f"  {nodo}: {B[i][0]}")
    
    print("\nFLUJOS ENTRE NODOS:")
    print("  Dirección  |  Flujo  |  Tipo")
    print("  " + "-"*35)
    
    for i in range(3):
        for j in range(3):
            if i != j and i < j:  # Mostrar cada conexion solo una vez
                flujo = flujos[i, j]
                if flujo > 0:
                    direccion = f"{nodos[i]} → {nodos[j]}"
                    tipo = "Saliente"
                else:
                    direccion = f"{nodos[j]} → {nodos[i]}"
                    tipo = "Entrante"
                    flujo = -flujo
                
                print(f"  {direccion:12} | {flujo:7.2f} | {tipo}")

# ===============================
# MAIN - ANALISIS COMPLETO
# ===============================
print("=" * 60)
print("PROYECTO: OPTIMIZACION DE SISTEMA DE REDES DE COMUNICACIONES")
print("=" * 60)

print("\n1. MATRICES DEL SISTEMA:")
print("Matriz A (conexiones entre nodos):")
print(A)

print("\nVector B (demanda de trafico):")
print(B)

# Verificar si el sistema es consistente (suma de B = 0)
suma_B = np.sum(B)  # Esto devuelve un escalar, no un array
print(f"\nSuma de elementos de B: {suma_B}")  # CORRECCIÓN: usar suma_B directamente, sin [0]
if abs(suma_B) < 1e-10:
    print(" El sistema es CONSISTENTE (suma de B = 0)")
else:
    print(" El sistema es INCONSISTENTE (suma de B ≠ 0)")
    print("  Se ajustara B para hacerlo consistente")
    # Ajustar B para hacerlo consistente
    B[2] = -B[0] - B[1]
    print(f"  Nuevo vector B: {B.flatten()}")

# Determinante y verificación
det = np.linalg.det(A)
print(f"\n2. ANALISIS DE LA MATRIZ A:")
print(f"Determinante de A: {det}")

# Matriz aumentada
AB = unir_matrices(A, B)
print("\nMatriz aumentada [A|B]:")
print(AB)

# Resolver el sistema
print("\n3. RESOLUCION DEL SISTEMA:")
if es_invertible(A):
    print("La matriz A es invertible.")
    A_inv = np.linalg.inv(A)
    print("\nInversa de A:")
    print(A_inv)

    X = np.dot(A_inv, B)
    print("\nSolucion del sistema AX = B usando la inversa:")
    print(X)
else:
    print("La matriz A NO es invertible (matriz singular).")
    print("Se usara el metodo de sistema reducido fijando el Nodo 3 como referencia...")
    
    # Resolver usando sistema reducido
    X = resolver_sistema_reducido(A, B, nodo_fijo=2)
    
    if X is not None:
        print("\nSolucion del sistema (con Nodo 3 fijo a 0):")
        print(X)
        
        # Verificar la solución
        resultado, error = verificar_conservacion(A, X, B)
        print(f"\nVerificacion - A*X deberia ser igual a B:")
        print(f"A*X = {resultado.flatten()}")
        print(f"B   = {B.flatten()}")
        print(f"Error: {error:.10f}")

# ===============================
# CÁLCULO DE FLUJOS
# ===============================
print("\n4. CALCULO DE FLUJOS ENTRE NODOS:")
if 'X' in locals() and X is not None:
    flujos = calcular_flujos(X)
    print("Matriz de flujos (f_ij = x_i - x_j):")
    print(flujos)
    
    print("\nInterpretacion de flujos:")
    nodos = ['Nodo 1', 'Nodo 2', 'Nodo 3']
    for i in range(3):
        for j in range(3):
            if i != j:
                if flujos[i, j] > 0:
                    print(f"  {nodos[i]} → {nodos[j]}: {flujos[i, j]:.2f} (flujo saliente)")
                else:
                    print(f"  {nodos[i]} ← {nodos[j]}: {-flujos[i, j]:.2f} (flujo entrante)")

# ===============================
# SIMULACIÓN DE ESCENARIOS
# ===============================
print("\n5. SIMULACION DE DIFERENTES ESCENARIOS:")

# Escenario 1: Cambio en la demanda
print("\nEscenario 1 - Cambio en la demanda:")
B_esc1 = np.array([[50], [-50], [0]])
print(f"Nueva demanda B: {B_esc1.flatten()}")

if es_invertible(A):
    X_esc1 = np.dot(np.linalg.inv(A), B_esc1)
else:
    X_esc1 = resolver_sistema_reducido(A, B_esc1, nodo_fijo=2)

if X_esc1 is not None:
    print(f"Solucion X: {X_esc1.flatten()}")
    flujos_esc1 = calcular_flujos(X_esc1)
    print(f"Flujo N1→N2: {flujos_esc1[0,1]:.2f}")

# Escenario 2: Matriz modificada (mayor capacidad entre N1 y N2)
print("\nEscenario 2 - Matriz con mayor capacidad entre N1 y N2:")
A_esc2 = np.array([[-3, 2, 1],
                   [2, -3, 1],
                   [1, 1, -2]])

print("Nueva matriz A:")
print(A_esc2)

if es_invertible(A_esc2):
    A_esc2_inv = np.linalg.inv(A_esc2)
    X_esc2 = np.dot(A_esc2_inv, B)
    print(f"Solucion X: {X_esc2.flatten()}")
    
    # Comparar con el escenario original
    if 'X' in locals() and X is not None:
        mejora = np.linalg.norm(X_esc2) - np.linalg.norm(X)
        print(f"Mejora en la norma de X: {mejora:.4f}")

# ===============================
# VISUALIZACIÓN EN TEXTO
# ===============================
print("\n6. VISUALIZACION DE RESULTADOS (TEXTO):")
if 'X' in locals() and X is not None and 'flujos' in locals():
    mostrar_resultados_texto(X, flujos, B)

# ===============================
# ANÁLISIS DE RESULTADOS
# ===============================
print("\n7. ANALISIS Y RECOMENDACIONES:")
if 'X' in locals() and X is not None:
    # Calcular métricas de rendimiento
    norma_X = np.linalg.norm(X)
    
    # Asegurarnos de que los flujos se calculan correctamente
    flujos_abs = np.abs(flujos)
    # Para encontrar el flujo mínimo, excluimos los ceros de la diagonal
    flujos_sin_cero = flujos_abs[flujos_abs > 0]
    
    if len(flujos_sin_cero) > 0:
        max_flujo = np.max(flujos_abs)
        min_flujo = np.min(flujos_sin_cero)
    else:
        max_flujo = 0
        min_flujo = 0
    
    print(f"• Norma del vector solucion: {norma_X:.4f}")
    print(f"• Flujo maximo entre nodos: {max_flujo:.4f}")
    print(f"• Flujo mínimo entre nodos: {min_flujo:.4f}")
    
    # Recomendaciones basadas en los resultados
    print("\nRECOMENDACIONES:")
    if max_flujo > 100:
        print("  ALERTA: Hay congestión en algunos enlaces")
        print("  Considerar aumentar la capacidad de los enlaces")
    else:
        print("  La red esta operando dentro de parametros aceptables")
    
    # Calcular el balance de flujos (solo conexiones únicas)
    flujos_conexiones = [flujos[0,1], flujos[0,2], flujos[1,2]]
    balance = np.std(np.abs(flujos_conexiones))
    
    if balance > 50:
        print(" ALERTA: Distribución de flujos desbalanceada")
        print(" Optimizar rutas y redistribuir trafico")
    else:
        print(" Buena distribución de flujos en la red")
    
    print("\nCONCLUSION FINAL:")
    print("El modelo matricial permite predecir eficientemente los flujos")
    print("en la red y identificar puntos de optimización.")

print("\n" + "=" * 60)
print("ANALISIS COMPLETADO")
print("=" * 60)
