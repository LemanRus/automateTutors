with open('mad_libs.txt', mode='r', encoding='utf-8') as in_text:
    temp_text = in_text.read()

adj = input("Введите прилагательное:\n")
nom1 = input("Введите существительное:\n")
adv = input("Введите глагол:\n")
nom2 = input("Введите существительное:\n")

temp_text = temp_text.replace('ПРИЛАГАТЕЛЬНОЕ', adj, 1)
temp_text = temp_text.replace('СУЩЕСТВИТЕЛЬНОЕ', nom1, 1)
temp_text = temp_text.replace('ГЛАГОЛ', adv, 1)
temp_text = temp_text.replace('СУЩЕСТВИТЕЛЬНОЕ', nom2, 1)

print(temp_text)
with open('mad_libs_result.txt', mode='w', encoding='utf-8') as out_text:
    out_text.write(temp_text)
