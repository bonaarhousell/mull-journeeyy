#breakdown:
#   input nya adalah string
#   outputnya adalah string yang di proses menjadi string terbalik
#   sistem di harapkan dapat membalik isi string
#   sistem diharapkan dapat menyimpan hasil proses ke variable agar dapat di outputkan

#pseudocode:
#   buat function
#   buat variabel output
#   buat edge case
#   loop parameter function dari index -1
#   tambahkan hasil loop ke variabel
#   return output

#code:
def reverse_string(string):
    rev = ""
    if not string:
        return "Cannot reverse empty string"

    for i in range(len(string)-1, -1, -1):
        rev = string[i] + rev

    return rev
print(reverse_string("hello"))


#test result:
#   12 kali percobaan dan tetap tidak tau approach lain selain [::-1]
#   akhir nya saya menggunakan hint, ternyata cukup rev = char + rev
#   approach yang saya gunakan saat ini belum terlalu saya mengerti
#   for i in range(len(string)-1, -1, -1):