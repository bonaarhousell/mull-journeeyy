#breakdown:
#   input nya adalah list of items
#   output nya adalah boolean
#   sistem harus dapat mengakses isi list
#   jika isi list ada yang sama baik itu string,integer atau lainnya
#   maka return True

#pseudocode:
#   buat function
#   buat variabel output
#   buat edge case
#   buat loop untuk mengakses isi list
#   buat loop untuk mengakses isi item
#   buat logic nya jika duplicated = True, else = False

#code:
words = ["a", "b", "f", "d", "e", "f"]
def cek_duplicate(word):
    dup = False
    value = []
    if not word:
        return dup
    for i in word:
        value.append(i)
        for x in value:
            if i in value[:-1] and x != value[-1]:
                dup = True

    return dup

print(cek_duplicate(words))

#test_result:
#   12 kali dan saya tidak tau mengapa code nya sekarang bisa sesuai dengan test