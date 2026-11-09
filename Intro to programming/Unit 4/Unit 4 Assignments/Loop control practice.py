for i in range(21):
    if i==15:
        break
    print(i)

print("\n----------\n")

for i in range(31):
    if i % 2 == 0:
        continue
    print(i)

print("\n----------\n")    

for i in range(10):
    if i==2:
        pass # i will print("you lose")
    print(i)

print("\n----------\n")

for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)

print("\n----------\n")    

list=[7,38,45,9,-1,29,56]
sum=0
for i in list:
    if i < 0:
        break
    sum += i
print(sum)