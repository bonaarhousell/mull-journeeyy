#breakdown:
#   input nya adalah kalimat string
#   output adalah dictionary yang sudah di proses sistem
#   objectiv : dapat menghitung kalimat yang sudah keluar

#pseudocode:
#   buat function
#   buat edge case
#   buat parameter function hanya lowercase
#   pisahkan kalimat jika ada spasi
#   buat dict kosong
#   loop parameter function yaitu multiple string
#   buat logic proses sistemnya
#   jika string ada di dictionary
#   maka dict[string] + 1
#   jika tidak ada
#   maka dict[string] = 1

#code:
def word_counter(words):
    if not words:
        return {}

    words = words.lower().split()
    counter = {}

    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter

print(word_counter("Are you ready to become rich are"))

#test_result:
#   one try karena logic nya sama dengan count occurrences
#   hanya membuat edge case baru .lower() dan .split()