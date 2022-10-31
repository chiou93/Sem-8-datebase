import pandas as pd

print('----'*30)
print('Табель учащихся 9 Ж класс')

stud_card = {
        'ID': ['01','02','03','04','05'],
        'Имя' : ['Ксения','Радмила','Виргиния','Иван','Стас'],
        'Фамилия': ['Левина','Амирова','Даугелайте','Данилов','Михайлов'],
        'Дата рождения' : ['31.08.1992','01.04.1992','13.07.1992','15.02.1993','06.03.1993'],
        'Успеваемость' : ['Троечник','Троечник','Троечник','Отличник','Ударник']
}
    
sc = pd.DataFrame(data = stud_card)

with open('students.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)