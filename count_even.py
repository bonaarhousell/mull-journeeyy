#breakdown:
#   input nya adalah kumpulan list nomor
#   hanya menerima angka even/genap
#   jika even maka proses data dengan penjumlahan semua angka even

#pseudocode:
#   loop list angka
#   jika angka dibagi dengan 2 sama dengan 0
#   maka bisa dipastikan angka itu adalah even
#   jumlahkan angka itu yang sudah di filter menggunakan if statment

numbers = [1,2,3,4,5,6,7,8]
def count_even(number):
    total = 0
    if not number:
        return "Angka tidak tersedia"
    for num in number:
        if num % 2 == 0:
            total += num

    return total

result = count_even(numbers)
print(result)

#percobaan:
#   saya mencoba banyak kali, pertama saya tidak menggunakan function
#   dan hasil nya berhasil, tetapi untuk pencegahan jika list nya kosong dan angka nya ganjil semua
#   tidak dapat saya atasi, jadi saya membuat nya menggunakan function mungkin code ini hanya berasal dari ingatan saya.