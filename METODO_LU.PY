import numpy as np

def lu_factorization(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.copy(A)

    for k in range(n):
        L[k, k] = 1.0
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]

    return L, U

# Ingresar la cantidad de ecuaciones/incógnitas por consola
n = int(input("Ingrese el número de ecuaciones/incógnitas: "))

# Inicializar la matriz A con ceros
A = np.zeros((n, n))

# Ingresar los coeficientes de la matriz A por consola
print("Ingrese los coeficientes de la matriz A:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Ingrese el coeficiente A[{i+1}][{j+1}]: "))

# Preguntar al usuario si desea ingresar el vector de términos independientes B
include_B = input("¿Desea ingresar el vector de términos independientes B? (y/n): ").lower()

if include_B == 'y':
    # Inicializar el vector de términos independientes B con ceros
    B = np.zeros(n)

    # Ingresar los términos independientes por consola
    print("Ingrese el vector de términos independientes B:")
    for i in range(n):
        B[i] = float(input(f"Ingrese el término independiente B[{i+1}]: "))

    # Realizar la factorización LU con la matriz A y el vector B
    L, U = lu_factorization(np.column_stack((A, B.reshape(-1, 1))))

    # Mostrar la matriz A por consola
    print("\nMatriz A:")
    print(A)

    # Mostrar el vector B por consola
    print("\nVector B:")
    print(B)

    # Mostrar las matrices L y U por consola
    print("\nMatriz triangular inferior (L):")
    print(L)

    print("\nMatriz triangular superior (U):")
    print(U[:, :-1])  # Excluir la última columna correspondiente a B

    # Verificar la respuesta (A = LU)
    print("\nVerificación de la respuesta (A = LU):")
    print(np.dot(L, U[:, :-1]))  # Verificar solo la parte de A

else:
    # Realizar la factorización LU solo con la matriz A
    L, U = lu_factorization(A)

    # Mostrar la matriz A por consola
    print("\nMatriz A:")
    print(A)

    # Mostrar las matrices L y U por consola
    print("\nMatriz triangular inferior (L):")
    print(L)

    print("\nMatriz triangular superior (U):")
    print(U)

    # Verificar la respuesta (A = LU)
    print("\nVerificación de la respuesta (A = LU):")
    print(np.dot(L, U))
