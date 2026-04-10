#breakdown:
#   input nya adalah 2 dictionary
#   output nya 1 dictionary
#   objectiv: dapat menggabungkan 2 dictionary tersebut ke 1 output dict

#pseudocode:
#   buat function
#   buat edge case
#   buat dictionary kita
#   loop dict1
#   jika key ada di di dict2
#   maka dict[key] = dict2[key]
#   maka isi dict kita dengan: key dan value dict1
#   buat variabel untuk key dan value dict2
#   loop dict2
#   jika dict[key] ada di dict2[key]
#   maka dict[key] akan menjadi dict[key] with value dict2
#   jika tidak
#   maka dict = dict2

#code:
dicts1 = {'b': 10, 'x': 10}
dicts2 = {'x': 20, 'y': 30}

def merge_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return "input must be dictionary"

    m_dict = {}
    for key1 in dict1:
         m_dict[key1] = dict1[key1]

    for key2 in dict2:
        if key2 in m_dict:
            m_dict[key2] = dict2[key2]
        else:
            m_dict[key2] = dict2[key2]


    return m_dict

print(merge_dicts(dicts1, dicts2))

#test result:
#   saya pertama mencoba menggunakan logic seperti ini:
#if m_dict not in dict1:
    #m_dict = dict1
#for key in dict2:
    #value = dict2[key]
    #if m_dict in key:
        #m_dict = m_dict[value]
    #else:
        #m_dict = dict2
#   ternyata tidak bisa langsung update m_dict ke dict1 tanpa loop
#   lalu saya coba neste loop dan bingung logic nya bagaimana
#   akhir nya berhasil setelah 25-30 menit debuggingg