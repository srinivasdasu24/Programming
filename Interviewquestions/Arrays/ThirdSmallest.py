def ThirdSmallest(array):
    first,second,third=10000000
    for i in range(0,len(array)):
        if array[i] < first:
            third=second
            second=first
            first=array[i]
        elif array[i] < second:
            third=second
            second=array[i]
        elif array[i] < third:
            third = array[i]
    return third
