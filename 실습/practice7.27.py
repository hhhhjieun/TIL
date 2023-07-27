# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f'안녕, {self.name}입니다.') 


# class Professor(Person): # 매개변수로 Person 함수를 받으면 인자로 사용 가능
#     def __init__(self, name, age, department):
#         # self.name = name
#         # self.age = age
#         # Person.__init__(self, name, age)
#         super().__init__(name, age) # self 안써도 됨
#         self.department = department


# class Student(Person):
#     def __init__(self, name, age, gpa):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)
#         self.gpa = gpa

# p1 = Professor('박교수', 49, '컴공')
# s1 = Student('김학생', 20, 3.5)

# p1.talk()
# s1.talk()

class Person:
    def __init__(self, name):
        self.name = name
        

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person): 
    gene = 'XX'

    def __init__(self, name): # 상속받아도 생성자 함수 작성 권장
        super().__init__(name)

    def swin(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def __init__(self, name, age): 
        super().__init__(name)
        self.age = age

    def walk(self):
        return '아빠가 걷기'
    

class FirstChild(Mom, Dad):
    # mom_gene = Mom.gene 
    # 상속 순서 변경 없이엄마의 유전자 정보를 쓰려면 
    # 별도로 클래스 변수 생성

    def __init__(self, name, age): 
        # super().__init__(name)
        Dad.__init__(self, name, age) # super() 보다는 상위클래스 이름 명시 추천
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
    

baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY > Dad가 먼저 상속 / 엄마 먼저 상속 > XX 
print(baby1.mom_gene) # XX

print(FirstChild.mro())
# [<class '__main__.FirstChild'>, <class '__main__.Dad'>, 
#  <class '__main__.Mom'>, <class '__main__.Person'>, 
#  <class 'object'>]