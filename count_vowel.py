#breakdown:
#   input nya adalah string
#   sistem diharapkan dapat membaca isi string
#   jika string memiliki vowels = a,e,i,o,u
#   maka hitung berapa kali vowels tersebut muncul
#   sistem diharapkan dapat membaca meskipun itu upper case atau lower case

#pseudocode:
#   loop stringnya
#   jika string tidak memiliki value
#   maka tampilkan pesan error
#   jika string tidak memiliki vowels
#   maka tampilkan vowels = 0
#   jika ada? tampilkan vowels

words = "hello world"
vowels = "aeiou"
def count_vowel(word):
    word = word.lower()
    counter= 0
    if not word:
        return 0
    for lett in word:
        if lett in vowels:
            counter += 1

    return counter

print(count_vowel(words))

#test result:
#   1 kali percobaan dan langsung berhasil, entah karena saya sudah sering melihat problem seperti ini
#   tetapi intuisi atau mungkin ingatan saya makanya bayangan kode nya langsung terlihat
