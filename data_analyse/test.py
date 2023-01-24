def my_test(list_elem) :
    dic_opperation = {
        '+' : lambda x,y : x + y ,
        '-' : lambda x,y : x-y,
        '*' : lambda x,y : x * y ,
        '/' : lambda x,y : x/y,

    }
    operator = list_elem.pop()
    operator = operator.split('')
    results = dic_opperation[operator[0]](list_elem[0],list_elem[1])
    for i in range(2,len(list_elem)):
        results += dic_opperation[operator[i-1]](results,list_elem[i])
    return results

