#breakdown:
#   input adalah list of number dan command user
#   output adalah list hasil manipulasi
#   objectiv: dapat memproses list input sesuai dengan command yang diberikan

#pseudocode:
#   buat function
#   buat edge case
#   buat trigger kondisi command:
    #   jika "reverse"
    #   buat list baru
    #   loop list input dengan cara terbalik
    #   lalu tambahkan hasil proses ke list baru
#   logic seperti ini akan dilakukan sesuai dengan fungsi command
#   "double", "sort", dan "sum"

#code:
list_number = [10, 5, 8, 3]
def list_manipulation(numbers, command):
    if not numbers:
        return []

    if not command:
        return "u have to use a command!\nlist of command:\nReverse\nDouble\nSort\nSum"

    command = command.lower()

    if command == "reverse":
        rev_result = []
        for i in range(len(numbers)-1, -1, -1):
            rev_result.append(numbers[i])
        return rev_result

    if command == "double":
        double_result = []
        for num in numbers:
            num *= 2
            double_result.append(num)
        return double_result

    if command == "sort":
        numbers.sort()
        return numbers

    if command == "sum":
        sum_result = 0
        for num in numbers:
            sum_result += num
        return sum_result

print(list_manipulation(list_number, "sort"))

#test_result:
#   saya kesultan di logic sort, saya mencoba menggunakan cara manual
#   saya kepikiran logic find_max tetapi membaliknya sehingga find_min
#   tetapi outputnya malah [10,5,5,3]