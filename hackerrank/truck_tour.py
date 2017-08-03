# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
pump = 0
tank = 0
for i in range(n):
    petrol, distance = map(int, raw_input().split())
    tank += petrol - distance
    if tank < 0:
        tank = 0
        pump = i + 1
print pump
