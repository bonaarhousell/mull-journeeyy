#breakdown:
#   input nya adalah list of number
#   output dictionary yang sudah di proses
#   objectiv: dapat mengelompokkan nilai
#   dan menghitung nilai sesuai dengan logic

#pseudocode
#   buat function
#   jika list kosong return list kosong
#   buat dictionary kosong
#   loop list number
#   jika num > 89 : maka dict[grade] = "A"
#   elif num > 79 and <= 89 : maka dict[grade] = "B"
#   elif num > 69 and <= 79 : maka dict[grade] = "C"
#   elif num > 59 and <= 69 : maka dict[grade] = "D"
#   else : dict[grade] = "F"
#   jika dict[grade] tidak ada di dictionary
#   maka dict[grade] = 1
#   jika ada
#   maka dict[grade] += 1

#code:
numbers = [85, 90, 78, 92, 88]

def grade_cek(number):
    if not number:
        return {}

    grades = {}

    for num in number:
        if num > 89:
            grade = "A"
        elif num > 79 and num <= 89:
            grade = "B"
        elif num > 69 and num <= 79:
            grade = "C"
        elif num > 59 and num <= 69:
            grade = "D"
        else:
            grade = "F"

        if grade in grades:
            grades[grade] += 1
        else:
            grades[grade] = 1

    return grades

print(grade_cek(numbers))

#test result:
#   terlalu banyak saya tidak dapat hitung
#   saya debugging dari 07.20 hingga 08.15
#   saya mengetest grades[num] = "A", lalu grades = "A"
#   tetapi ketika di return, yang muncul malah dict 85 : 1 bukan "A" : 1
#   mungkin penyebab nya di if num in grades, entah lah saya sudah mentok
#   saya bahkan mencoba membuat list kosong dan menambahkan grade ke list tersebut
#   agar di loop untuk ditambahkan di dictonary