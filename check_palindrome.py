#breakdown approach 1:
#   input nya adalah string berisi huruf atau angka
#   output boolean True or False
#   jika angka atau huruf pertama sama dengan angka terakhir hingga ke tengah
#   maka huruf atau angka tersebut adalah palindrome

#pseudocode:
#   buat function cek_palindrome
#   buat parameter yang dapat menampung input string
#   buat variabel yang menyimpan True or False
#   buat method agar string selalu lowercase
#   buat 2 pointer yang menunjuk string. left and right
#   loop kondisi 2 pointer tersebut
#   jika pointer left dan right sama hingga akhir string
#   return palindrome = True
#   else = return False

#code approach 1:
def check_palindrome(word):
    word = word.lower()
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True
print(check_palindrome('hello world'))

#breakdown approach 2:
#   input adalah list string
#   sistem diharapkan dapat mengecek isi string itu 1 persatu
#   string awal huruf ,akhir huruf hingga ke tengah harus sama

#pseudocode:
#   buat variabel untuk tampil kan boolean True or False
#   buat if statement jika string dari awal dan akhir hingga ke tengah nya sama
#   maka string itu adalah palindrome, tampil kan True
#   jika sebaliknya maka else

#code approach 2:
def cek_palindrome(word):
    palindrome = False
    word = word.lower()
    if word == word[::-1]:
        palindrome = True
        return palindrome
    else:
        return palindrome

print(cek_palindrome('ada'))

#test result:
#one try, kayak nya karena ada rekomendasi dari pycharm.