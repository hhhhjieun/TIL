# # 혈액형 인원수 세기
# # 결과 => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# # []
# new_dict = {}
# # blood_types을 순회하면서
# for blood_type in blood_types:
#     # 기존의 키가 이미 존대한다면,
#     if blood_type in new_dict:
#         # 기존 키의 값을 +1 증가
#         new_dict[blood_type] += 1
#     # 키가 존재하지 않는다면(처음 설정되는 키)
#     else:
#         new_dict[blood_type] = 1
# # print(new_dict)

# # .get() => if/else 대체
# new_dict = {}
# # blood_types을 순회하면서
# for blood_type in blood_types:

#     new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
   
# #print(new_dict)


# # .setdefault()
# new_dict = {}
# for blood_type in blood_types:
#     new_dict.setdefault(blood_type, 0) 
#     new_dict[blood_type] += 1
   
# print(new_dict)




# 얕은 복사의 한계 : 작은 리스트의 요소가 같은 곳을 바라봄...
a = [1, 2, [1, 2]]

b = a[:]
b [2][0] = 999
print(a, b) # [1, 2, [999, 2]] [1, 2, [999, 2]]

a = [1, 2, [1, 2]]
c = a.copy()
c[2][0] = 999
print(a, c) # [1, 2, [999, 2]] [1, 2, [999, 2]]

# 깊은 복사
import copy

original_list = [1, 2, [1, 2]]

deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999

print(original_list, deep_copied_list) # [1, 2, [1, 2]] [1, 2, [999, 2]]