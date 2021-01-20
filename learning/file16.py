odd_list=[1,3,5,7]
unordered_set={9,10,11,12,13,14,15,16,17}
print(unordered_set)
for num in unordered_set:
    if (not num%2==0):
        odd_list.append(num)
print(odd_list)