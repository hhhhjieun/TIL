# Person 정의
class Person:
    name = 'unkown' 

    # 인스턴스 메서드
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # unkown > 인스턴스는 본인의 인스턴스 name(변수)이 없으면
          # class의 있는지 찾아 올라간다
# p2 인스턴스 변수 설정 전/후

p2 = Person()
p2.talk() # unkown

p2.name = 'Kim'
p2.talk() # Kim

print(Person.name)
print(p1.name)
print(p2.name)

