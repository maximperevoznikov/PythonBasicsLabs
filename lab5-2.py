"""
Реализуйте класс Student со следующими методами:
get_python_skill() - получить численную оценку уровня знания Python
learn_python() - увеличить численную оценку уровня знания Python на 1
Изначально значение численной оценки уровня знания Python - 0.
Пример использования: s = Student() s.get_python_skill()
"""

class Student:
    def __init__(self):
        self.python_skill = 0
    
    def get_python_skill(self):
        return self.python_skill
    
    def learn_python(self):
        self.python_skill+=1

s = Student()
print("Уровень знания раньше:")
print(s.get_python_skill())
print("Делаем лабы...")
s.learn_python()
print("Уровень знания теперь:")
print(s.get_python_skill())