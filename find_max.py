#breakdown:
#   input list of number
#   output: nilai kedua terbesar
#   objectiv: mencari nilai kedua terbesar

#pseudocode:
#   buat function
#   buat edge case tidak boleh list < 2
#   buat 2 variabel pembanding
#   loop list number
#   jika  variabel 1 < parameter loop
#   maka update nilai variabel 2 menjadi variabel 1
#   dan variabel 1 menjadi value parameter loop
#   elif variabel 2 < parameter loop
#   maka update variabel 2 menjadi parameter loop

#code:
numbers = [2,3,5,7,8,9,10]
def second_largest(number):
    if not number:
        return "List cannot empty"
    if len(number) < 2:
        return "List must have at least two elements"
    largest = None
    second_largest = None
    for num in number:
        if largest is None:
            largest = num
        elif largest < num:
            second_largest = largest
            largest = num
        elif second_largest < num:
            second_largest = num

    return second_largest

print(second_largest(numbers))

#test_result:
#   one try xD