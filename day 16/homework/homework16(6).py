
list = [1,2,3,4,5,6,7,8,9]

odd_sum = 0
even_sum = 0

for sub in list:
    for ele in str(sub):
        if int(ele) % 2 == 0:
            even_sum += int(ele)
        else:
            odd_sum += int(ele)

print("odd digit sum: " + str(odd_sum))
print("even digit sum: " + str(even_sum))




