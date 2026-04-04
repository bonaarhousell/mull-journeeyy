#breakdown:
#   input nya adalah string
#   output nya dictionary hasil dari proses sistem
#   objectiv : menghitung karakter yang muncul di string lalu tambahkan ke dictionary

#pseudocode:
#   buat dictionary
#   buat function
#   buat edge case
#   buat loop untuk memproses string
#   buat logic statement
#   jika string ada di dictionary
#   maka dict[loop]+1
#   jika tidak ada?
#   tambahkan string ke dictionary

#code:
occurrences = {}
def count_occurrences(words):
    if not words:
        return {}
    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1

    return occurrences

print(count_occurrences("AaBbCc"))

#test_result =
#   1 try, pertama saya sempat berpikir bahwa sulit dan tidak tau mau ngapain
#   setelah saya breakdown dan memikirkan pseudocodenya
#   langsung ada seperti gambaran code nya di kepala saya