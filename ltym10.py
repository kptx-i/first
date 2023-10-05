

def approximation_function(args):
    
    # Важно чтобы передавались именно координаты в виде кортежа,
    # а т.к. у нас двухмерный график, то нам нужно именно 2 аргумента
    if type(args[0]) != tuple and len(args[0]) != 2:
        print("Аргументы функции должны быть представлены в виде (x, y)")
    
    # Создаём список и переменную кол-ва точек
    a = []
    args_num = len(args)
    
    # Создаётся матрица вида n x n+1, где элементами первых n столбцов
    # являются x^(n-1), а последнего столбца - y
    for i in range(args_num):
        a.append([])
        for g in range(args_num):
            a[i].append(args[i][0]**(args_num - g - 1))
        a[i].append(args[i][1])
    
    q = []
    for i in range(len(a)):
        
        # Если число главной диагонали равно нулю, то мы не можем поделить на него
        # поэтому надо поменять строку на следующую
        if a[i][i] == 0:
            w = 0
            for j in range(len(a)):
                
                # Проверка строки на число г.д.
                if j >= len(a) - 1 - i:
                    pass
                
                # Если оно не равно нулю, то мы можем поменять строку по индексу
                else:
                    
                    if w >= 1:
                        pass
                    elif a[j+i][i] != 0:
                        a[j+i], a[i] = a[i], a[j+i]
                        w += 1
            if w == 0:
                print("Функцию нельзя аппкросимировать по этим точкам")
                return
                        
        if a[i][i] == 0 and a[i] == a[-1]:
            print("Функцию нельзя аппкросимировать по этим точкам")
            return
        
        for j in range(len(a[0])):
            
            # делим всю строку на число этой строки по главной диагонали
            dm = a[i][j]/a[i][i]
            
            # Проходим по каждой строке
            for h in range(len(a)):
                
                # скипаем строки до г.д. включительно
                if h >= len(a) - 1 - i:
                    pass
                
                else:
                    if j == 0:
                        q.append(a[i+h+1][i])
                    a[i+h+1][j] -= dm*q[h]
        q = []
        
        # делаем всё тоже самое, только треугольник из нулей сверху
    for i in range(len(a)-1, 0-1, -1):
        
        for j in range(len(a[0])-1, 0-1, -1):
            
            # делим всю строку на число этой строки по главной диагонали
            dm = a[i][j]/a[i][i]
            
            # Проходим по каждой строке
            for h in range(len(a)-1, 0-1, -1):
                
                # скипаем строки после г.д. включительно
                if h >= i:
                    pass
                else:
                    a[h][j] -= dm*a[h][i]
    
    # создаём список с коэффициентами полинома
    factors = []
    for i in range(len(a)):
        factors.append(a[i][-1]/a[i][i])
    
    
    polynom = ''
    for i in range(len(factors)):
        
        # добавляем плюс положительным коэффам для правильного сложения строки
        if factors[i] >= 0:
            factors[i] = f'+{factors[i]}'
            
        # степень x
        level = len(factors)-i-1
        polynom += f'{factors[i]}x^{level}'
        
    # делаем срез, чтобы избавиться от x^0
    return polynom[:-3]

def main():
    e = 2.71828182845904523536
    
    print(approximation_function([(-2, 1), (-1, 0), (0, -3)]))


if __name__ == "__main__":
    main()
