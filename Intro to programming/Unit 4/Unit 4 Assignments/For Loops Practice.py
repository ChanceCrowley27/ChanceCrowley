count_down=[10, 9,8,7,6,5,4,3,2,1]

for numbers in count_down:
    print(numbers)

for numbers in count_down:
    sum_1=(sum(count_down))

print(sum_1)

list_integers=[1,2,3,4,5] 
squares=[]
for numbers in list_integers:
    squares.append(numbers*numbers)
    
print(squares)

vowel_sum=0
word=input("enter a word\n")
for letters in word:
    if letters=="a"or letters=="e"or letters=="i" or letters=="o" or letters=="u":
        vowel_sum += 1

print(vowel_sum)