"""Дан словарь {‘class’: {‘student’: {‘name’: ‘Mike’, ‘marks’: {‘physics’: 70, ‘history’: 80}}}}.
Выведите на экран имя студента и его оценку по истории."""

dict1 = {'class': {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}}

dict_class = dict1['class']
#print(dict_class)

dict_student = dict_class['student']
#print(dict_student)

dict_marks = dict_student['marks']

#print(dict_marks)

print('Physics mark: ', dict_marks['physics'])
