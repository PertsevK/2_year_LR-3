import numpy as np


def Ispower5(K):
    """K is integer number. Returns K if it is a power of 5"""
    i = 5
    while i < 3000:
        if K == i: return True
        else: i *= 5
    else: return False


def Ispower_K_for_list(list_of_K):
    """A function to process a list of input data according to a function Proc26"""
    out_data = []
    for K in list_of_K:  # Для кожного елемента вхідного списку
        if Ispower5(K): out_data.append(K)
    return out_data


def task_Proc26():
    """Entering input data, calling a function, outputting results"""
    in_data = []
    try:
        in_num = int(input("Enter the number of incoming items: "))
        for i in range(in_num):
            temp = int(input(f"{i+1} element: "))
            in_data.append(temp)
    except ValueError:
        print("Input error!")
    else:
        print("Numbers that are a power of 5: ", Ispower_K_for_list(in_data))

def matrix5(filename):
    """Зчитування матриці з файлу, підрахунок параметрів та виконання операції над матрицею"""
    M = N = K = 0
    with open(filename, 'r') as f:
        param_line = f.readline().split(" ")
        try:
            M = int(param_line[0])
            N = int(param_line[1])
        except ValueError:
            print("Wrong file data")
        else:
            matrix = np.loadtxt(filename, skiprows=1, max_rows=M)
            print(matrix)
            # Підрахунок параметрів задачі
            means = []
            min_elements = []
            for i in range(0, M, 2):
                row = matrix[i]
                mean = np.mean(row)
                min_element = np.min(row)
                means.append(mean)
                min_elements.append(min_element)

            # Генерація матриці того ж розміру з випадковими числами
            random_matrix = np.random.rand(M, N)
            print("Random matrix\n",random_matrix)
            # Обчислення скалярного добутку
            scalar_product = np.sum(matrix * random_matrix)

            return means, min_elements, scalar_product
    
    return 0, 0, np.zeros((M, N))


def task2_Matrix5():
    """Entering the name of the input file, calling the function for reading and processing the matrix, outputting the results"""
    try:
        filename = input("Enter filename (.txt): ")
        result = matrix5(filename)
        if result is not None:
            means, min_elements, scalar_product = result
            for i, (mean, min_element) in enumerate(zip(means, min_elements), start=1):
                print(f"Row {2*i-1}: Arithmetic mean = {mean}, Minimum element = {min_element}")
            print("Scalar product with a random matrix:", scalar_product)
    except:
        print("Wrong filename")
