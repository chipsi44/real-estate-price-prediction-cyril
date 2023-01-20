my_list = [1,2,3,4,5]

'''doble_list = []

for elem in my_list :
    doble_list.append(elem*2)'''

double_list = list(map(lambda x:x*2, my_list))

print(double_list)