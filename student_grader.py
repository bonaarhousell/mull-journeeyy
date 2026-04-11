#breakdown:
#   input nya adalah list of dictionary barisi nama-nama siswa dan nilai-nilai siswa
#   outputnya adalah string dengan format rapi
#   objectiv: dapat memproses list of dictionary= nilai siswa di proses
#   lalu ditentukan sesuai logic atau format yang di tetapkan
#   lalu mencari nilai rata-rata per-siswa
#   mencari nilai tertinggi dari seluruh siswa,
#   mencari nilai rata-rata seluruh siswa,
#   mencari nilai terendah seluruh siswa

#pseudocode:
#   buat function
#   buat edge case
#   buat variabel list untuk menampung: average,max,min
#   buat logic untuk nilai siswa:
#   loop input list of dictionary key: grade
#   proses value tersebut untuk mencari: average,max, dan min
#   simpan hasil proses ke variabel yang telah di siapkan
#   buat grade untuk nilai siswa (pembanding nya menggunakan average)
#   jika average >= 90 = A
#   jika average >= 80 = B
#   jika average >= 70 = C
#   jika average >= 60 = D
#   else : grade = F
#   simpan hasil proses ke variabel grade
#   buat format print menggunakan f string dengan {masing-masing variabel}

#code:
students = [
    {'name': 'Alice', 'grades': [85, 90, 88]},
    {'name': 'Bob', 'grades': [75, 80, 78]},
    {'name': 'Charlie', 'grades': [95, 92, 98]}
]

def student_grader(items):
    if not items:
        return []

    highest = None
    lowest = None
    for item in items:
        for value in item['grades']:
            if highest == None:
                highest = value
            elif value > highest:
                highest =value

            if lowest == None:
                lowest = value
            elif value < lowest:
                lowest = value

    average = []
    for item in items:
        averages = sum(item['grades']) / len(item['grades'])
        average.append(averages)

    grades = []
    for value in average:
        if value >= 90:
            grade = "A"
        elif value >= 80:
            grade = "B"
        elif value >= 70:
            grade = "C"
        elif value >= 60:
            grade = "D"
        else:
            grade = "F"
        grades.append(grade)

    return grades, highest, lowest, average

print(student_grader(students))

#test_result:
#   saya sudah mencoba project ini hingga 150 menit
#   tidak terhitung error yang sudah saya liat
#   saya tidak bisa kepikiran cara menyambungkan data yang sudah saya proses
#   menjadi output yang diinginkan, saya juga seperti nya terlalu fokus
#   ke output class accumulatif, dan tidak kepikiran cara mem proses data per-siswa