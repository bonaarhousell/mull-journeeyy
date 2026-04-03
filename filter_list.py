#breakdown:
#   input nya adalah list integer
#   output nya jika list iteger berhasil melewati logic maka
#   objectiv : dapat memfilter data yang di input

#pseudocode:
#   buat function
#   buat list kosong sesuai filter yang dibutuhkan
#   buat edge case
#   loop input list
#   jika value list di bagi 2 sama dengan 0
#   maka tambahkan data tersebut ke list kosong [0]
#   jika tidak? tambahkan ke list kosong [1]
#   jika value list lebih besar dari 25
#   maka tambahkan ke list kosong [2]
#   jika lebih kecil dari 20
#   tambahkan ke list kosong [3]

#code:

def filter_data(number):
    if not number:
        return []
    even = []
    odd = []
    bigger = []
    lesser = []
    for num in number:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

        if num > 25:
            bigger.append(num)
        elif num < 20:
            lesser.append(num)

    return even, odd, bigger, lesser

print(filter_data([1,2,3,4,5,10,20,30,40,45,9,8,7,320,765,8373]))

#test_result:
#   one try