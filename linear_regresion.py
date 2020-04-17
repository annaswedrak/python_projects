#regresja liniowa
#1 zdefiniowanie wzoru na funkcję liniową y = mx + b, zwraca
#wartość y 


def get_y(m, b, x):
  return (m * x) + b

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)



#liczenie błędu, odległość punktu od funkcji, liczenie wartości
#y dla argumentu x punktu
def calculate_error(m,b,point):
    x_point, y_point = point 
    get_y = (m * x_point) + b
    diff = get_y - y_point 
    return abs(diff)

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

#sumaryczny błąd dla zbioru punktów 
def calculate_all_error(m, b, points):
    total = 0
    for point in points: 
        total += calculate_error(m,b,point)
    return total

possible_ms = [i*0.1 for i in range(-100, 101)]
possible_bs = [i*0.1 for i in range(-200, 201)]

#znalezienie optymalnymalnych parametrów funkcji liniowej m i b
#obrazującej najlepiej rozkład zbioru punktów na osi współrzędnych
smallest_error = (float("inf"))
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m, b, datapoints) < smallest_error:
            best_m = m
            best_b = b
            smallest_error = calculate_all_error(m, b, datapoints)
print(best_m, best_b, smallest_error)


