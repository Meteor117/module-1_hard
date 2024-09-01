grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],[4, 4, 3], [5, 5, 5, 4, 5]]#список оценок по алфавиту
grades_average=((sum(grades[0])/len(grades[0])),(sum(grades[1])/len(grades[1])),(sum(grades[2])/len(grades[2])),(sum(grades[3])/len(grades[3])),(sum(grades[4])/len(grades[4])))
#print(gr1,type(gr1))
students={'Johny', 'Bilbo', 'Steve', 'Khendrick', 'Aaron'}# неупорядоченное множеств всех студентов

#Задача - составить словарь(имя - средняя оценка)

students2=(str(students))
stud2=sorted(students)
#print(stud2)
named=zip(stud2,grades_average)
print (dict(named))







