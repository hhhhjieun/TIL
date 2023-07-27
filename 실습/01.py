# 클래스 정의
class Person: # 클래스는 파스칼 케이스 사용(대문자)
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self, name): # __ 붙은건 개발자가 직접 호출x, 알아서 호출 
        self.name = name      # > 생성자 메서드 (인스턴스를 만들 때 생성)

    def singing(self):
        return f'{self.name}가 노래합니다.'
    
# 인스턴스를 생성 > 인자 필요(name)
singer1 = Person('iu')
singer2 = Person('BTS')

# 메서드 호출
print(singer1.singing()) # iu가 노래합니다
print(singer2.singing()) # BTS가 노래합니다.

# 속성(변수) 사용
print(singer1.blood_color) # red
print(singer2.blood_color) # red

