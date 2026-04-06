#breakdown:
#   input list of number
#   output nilai rata-rata dari list tersebut
#   objectiv: dapat menemukan nilai rata-rata

#pseudocode:
#   buat function
#   buat edge case
#   buat variabel yang menampung penjumlahan list number
#   loop list number
#   variabel += parameter loop
#   variabel % isi list

#code
numbers = [10, 20, 30, 40, 50]
def count_average(number):
    if not number:
        return []
    accumulation = 0
    for num in number:
        accumulation += num
    accumulation /= len(number)
    return accumulation
print(count_average(numbers))

#test result:
#   2 kali, sempat keliru perbedaan / dan %
#   saya mengetest accumulation %= dan hasilnya 0