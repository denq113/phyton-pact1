import math

print("Введите длину маятника")
l = float(input())
g = 9.81
t = 2*math.pi*math.sqrt(l/g)
print("Период колебания маятника равен = ",t)