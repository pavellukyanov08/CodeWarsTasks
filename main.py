# Task 1
# def get_count(sentence):
#     chars = ['a','e','i','o','u']
#     count = 0
#     for i in sentence:
#         if i in chars:
#             count += 1
#     return get_count

# sentence = 'abracadabra'
# print(get_count(sentence))


# Task 2
# def xor(a,b):
#     return a != b

# print(xor(True, True))


# Task 3
# def remove_exclamation_marks(s):
#     return s.replace('!', '')
        

# s = 'Hello world!'
# print(remove_exclamation_marks(s))


# Task 4
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
    # return [b for b in birds if b not in geese]
    # for i in birds:
        # if i in geese:
            # print(i)
            # birds.remove(i)
            # print(birds)
    # return birds


# birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# print(goose_filter(birds))


# Task 5
# from collections import Counter
# def is_anagram(test, original):
#     return Counter(test) == Counter(original)

# test = 'foefet'
# original = 'toffee'

# print(is_anagram(test, original))


# Task 6
# def capitals(word):
#     res = []
#     for idx, ch in enumerate(word):
#         if ch.isupper():
#             res.append(idx)
#     return res

# word = 'etqURkAkeKCsgmxZTfbReH'
# print(capitals(word))


# Task 7
# def reverse_list(l):
#     return l[::-1]

# l = [1, 2, 3, 4]
# print(reverse_list(l))


# Task 7
# def dna_to_rna(dna):
#     return dna.replace('T', 'U')

# dna = 'GCAT'
# print(dna_to_rna(dna))


# Task 8
# def name_shuffler(str_):
#     fname = str_.split(' ')[0]
#     result = str_.split(' ')[1] + ' ' + fname
#     return result

# str_ = 'john McClane'
# print(name_shuffler(str_))


# Task 9
# def sort_by_length(arr):
#     sorted_arr = sorted(arr, key=len)
#     return sorted_arr

# arr = ['beg', 'i', 'life', 'to']
# print(sort_by_length(arr))


# Task 10
# def expression_matter(a: int, b: int, c: int) -> int:
#     return max(
#         a + b + c,
#         a * b * c,
#         (a + b) * c,
#         a * (b + c),
#         a + (b * c),
#         (a * b) + c
#     )
#
# a, b, c = 1, 2, 3
# print(expression_matter(a, b, c))


# Task 11
# def likes(names):
#     length = len(names)
#
#     if length == 0:
#         return "no one likes this"
#     elif length == 1:
#         return f"{names[0]} likes this"
#     elif length == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif length == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {length - 2} others like this"
#
# print(likes([]))
# print(likes(["Peter"]))
# print(likes(["Jacob", "Alex"]))
# print(likes(["Max", "John", "Mark"]))
# print(likes(["Alex", "Jacob", "Mark", "Max"]))


# Task 12
# def bouncing_ball(h, bounce, window):
"""
Ребенок играет с мячом на n-м этаже высотного здания. Известна высота этого этажа над уровнем земли h.
Он бросает мяч из окна. Мяч отскакивает (например) на две трети своей высоты (коэффициент отскока 0,66).
Его мать смотрит из окна на высоте 1,5 метра от земли.
Сколько раз мать увидит, как мяч пролетает перед ее окном (включая моменты, когда он падает и подпрыгивает)?
Для проведения корректного эксперимента необходимо соблюдение трех условий:
Параметр с плавающей точкой «h» в метрах должен быть больше 0.
Параметр float «bounce» должен быть больше 0 и меньше 1.
Параметр float «window» должен быть меньше h.
Если выполнены все три условия выше, вернуть положительное целое число, в противном случае вернуть -1.
Примечание:
Мяч можно увидеть только в том случае, если высота отскока мяча строго больше параметра окна.    Примеры:
- h = 3, bounce = 0.66, window = 1.5, result is 3
- h = 3, bounce = 1, window = 1.5, result is -1 
(Condition 2) not fulfilled).
"""
from functools import reduce

#     if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
#         return -1

#     result = 1
#     h *= bounce
#     while h > window:
#         result += 2
#         h *= bounce
#     return result


# print(bouncing_ball(3, 0.66, 1.5))


# Task 13
# def delete_nth(lst, max_e):
#     new_lst = []
#     counts = {}
#     for i in lst:
#         print(counts)
#         if counts.get(i, 0) < max_e:
#             new_lst.append(i)
#             counts[i] =  counts.get(i, 0) + 1
#     return new_lst


# lst = [1, 2, 3, 1, 2, 1, 2, 3, 1]
# print(delete_nth(lst, 2))


# Task 14
# def two_sort(array):
#     return '***'.join(sorted(array)[0])

# array = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
# print(two_sort(array))


# Task 15
# def sum_two_smallest_numbers(numbers):
#     return sorted(numbers)[0] + sorted(numbers)[1]

# numbers = [9, 1, 5, 8, 12, 18, 22]
# print(sum_two_smallest_numbers(numbers))


# Task 16
# def find_short(s):
#     return len(min(s.split(' '), key=len))

# s = "bitcoin take over the world maybe who knows perhaps"
# print(find_short(s))


# Task 17
# def permutations(s):
#     from itertools import permutations

#     return list({''.join(s) for s in permutations(s)})

# s = 'aabb'
# print(permutations(s))


# Task 18
# def zero(func=None): return func(0) if func else 0
# def one(func=None): return func(1) if func else 1
# def two(func=None): return func(2) if func else 2
# def three(func=None): return func(3) if func else 3
# def four(func=None): return func(4) if func else 4
# def five(func=None): return func(5) if func else 5
# def six(func=None): return func(6) if func else 6
# def seven(func=None): return func(7) if func else 7
# def eight(func=None): return func(8) if func else 8
# def nine(func=None): return func(9) if func else 9

# def plus(y): return lambda x: x + y
# def minus(y): return lambda x: x - y
# def times(y): return lambda x: x * y
# def divided_by(y): return lambda x: x // y

# print(one(plus(two())))


# Task 19
# def max_sequence(arr):
#     current_sum = max_sum = 0
#     for i in arr:
#         current_sum = max(i, current_sum + i)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_sequence(arr))


# Task 20
# def domain_name(url):
#     import re

#     domain = re.sub(r'^(https?:\/\/)?(www\.)?', '', url)
#     domain = re.split(r'\/|\\|\?|#', domain)[0]

#     if '.' in domain:
#         domain = domain.split('.', 1)[0]

#     return domain

# urls = [
#     "http://google.com",
#     "https://123.net",
#     "https://hyphen-site.org",
#     "http://codewars.com",
#     "www.xakep.ru",
#     "https://youtube.com",
#     "http://www.codewars.com/kata/",
#     "icann.org"
# ]

# for url in urls:
#     print(domain_name(url))


# Task 21
# def move_zeros(lst):
#     nums = [i for i in lst if i != 0]
#     print(nums)
#     zeros = [0] * (len(lst) - len(nums))
#     print(zeros)
#     return nums + zeros
#
# lst = [1, 0, 1, 2, 0, 1, 3]
# print(move_zeros(lst))


# Task 22
# def solution(s):
#     result = ''
#     for char in s:
#         if char.isupper():
#             result += ' ' + char
#         else:
#             result += char
#     return result
#
# s = 'helloWorld'
# print(solution(s))


# Task 23
# def array_diff(a, b):
#     return [i for i in a if i not in b]
    # result = []
    # for i in a:
    #     if i not in b:
    #         result.append(i)
    # return result

# a, b = [1, 2, 2], [1]
# print(array_diff(a, b))


# Task 24
# def alphabet_position(text):
#     result = []
#     for char in text:
#         if char.isalpha():
#             position = ord(char.lower()) - ord("a") + 1
#             result.append(str(position))
#     return ' '.join(result)
#
# text = "The sunset sets at twelve o' clock."
# print(alphabet_position(text))


# Task 25
# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i
#
# seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]
# print(find_it(seq))


# Task 26. Quick sort int array
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[0]
#     left = [i for i in arr[1:] if i < pivot]
#     print(f'left: {left}, pivot: {pivot}')
#     right = [i for i in arr[1:] if i > pivot]
#     print(f'right: {right}, pivot: {pivot}')
#
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
# arr = [8, 3, 1, 6, 4, 7]
# print(quick_sort(arr))


# Task 27. Quick sort str array
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[0]
#     left = [i for i in arr[1:] if len(i) < len(pivot)]
#     print(f'left: {left}, pivot: {pivot}')
#     right = [i for i in arr[1:] if len(i) >= len(pivot)]
#     print(f'right: {right}, pivot: {pivot}')
#
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
# arr = ["apple", "kiwi", "banana", "fig"]
# print(quick_sort(arr))


# Task 28. Choice sort
# def choice_sort(arr):
#     for i in range(len(arr)):
#         min_item = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_item]:
#                 min_item = j
#         arr[i], arr[min_item] = arr[min_item], arr[i]
#     return arr
#
#
# arr = [29, 10, 14, 37, 13]
# print(choice_sort(arr))


# Task 29. Choice sort
# def choice_sort(arr):
#     for i in range(len(arr)):
#         min_item = i
#         for j in range(i + 1, len(arr)):
#             if arr[j][1] < arr[min_item][1]:
#                 min_item = j
#         arr[i], arr[min_item] = arr[min_item], arr[i]
#     return arr


# arr = [("Alice", 90), ("Bob", 70), ("Charlie", 85)]
# arr = [29, 10, 14, 37, 13]
# print(choice_sort(arr))


# def square(x):
#     return x * x
#
# numbers = [1, 2, 3, 4, 5]
# squares = map(square, numbers)
# print(list(squares))

# lst = [1, 2, 3, 4]
# result = list(map(lambda x: x * x, lst))
# print(result)
#
# lst = [1, 2, 3, 4]
# result = list(filter(lambda x: x % 2 == 0, lst))
# print(result)
#
# lst = [1, 2, 3, 4]
# result = list(map(lambda x: str(x), lst))
# print(result)
#
# lst = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, lst)
# print(result)
#
# lst = ['level', 'world', 'madam', 'python']
# result = list(filter(lambda word: word[::] == word[::-1], lst))
# print(result)
#
# lst = [1, 2, 3, 4, 5]
# result = [
#     list(filter(lambda x: x % 2 != 0, lst)),
#     list(map(lambda x: x * x, lst)),
#     reduce(lambda x, y: x + y, lst)
# ]
# print(result)
#
# lst = ['hi', 'hello', 'world', 'yes']
# result = filter(lambda x: len(x) > 4, lst)
# print(len(list(result)))
#
# lst = ["Python", "is", "awesome"]
# result = reduce(lambda x, y: x + y, lst, "")
# print(result)
#
# lst = ['Python', '', ' ', 'code', '']
# result = list(filter(lambda x: x.strip(' '), lst))
# print(result)


# Task. 30
# def missing_number(nums):
#     n = len(nums)
#     full_set = set(range(n + 1))
#     return list(full_set - set(nums))[0]
#
#
# lst = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# print(missing_number(lst))


# Task. 31
# def reverse_string(s):
#     left, right = 0, len(lst) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#
# lst = ["H","a","n","n","a","h"]
# print(reverse_string(lst))


# Task. 31
# def reverse_string(lst):
#     left , right = 0, len(lst) - 1
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#
#     return lst
#
# lst = ["H", "a", "n", "n", "a", "h"]
# print(reverse_string(lst))


# def clock_angle(hour, minutes):
#     hour_angle = (hour % 12 + minutes / 60) * 30
#     minute_angle = minutes * 6
#     angle = abs(hour_angle - minute_angle)
#     return min(angle, 360 - angle), angle
#
# hour, minute = map(int, input().split())
# print(clock_angle(hour, minute))


# def intersect(lst1, lst2):
#     from collections import defaultdict
#     freq = defaultdict(int)
#     result = []
#
#     for item in lst1:
#         freq[item] += 1
#
#     for item in lst2:
#         if freq[item] > 0:
#             result.append(item)
#             freq[item] -= 1
#
#     return result
#
#
# lst1, lst2 = [1,2,2,1], [2,2]
# print(intersect(lst1, lst2))


# def unique_intersection(nums1, nums2):
#     return list(set(nums1) & set(nums2))
#
# nums1, nums2 = [1,2,2,1], [2,2]
# print(unique_intersection(nums1, nums2))


# def max_power(s):
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             substring = s[i:j + 1]
#     return s
#
# s = 'meet'
# print(max_power(s))


# def delete_extra_nums(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         if i not in new_lst:
#             new_lst.append(lst[i])
#     return f'список: {new_lst}'
#
# lst = [1, 2, 2, 3, 4]
# print(delete_extra_nums(lst))

# def min_value(dct):
#     return max(dct.items(), key=lambda x: x[1])
#
# dct = {"a": 10, "b": 20, "c": 5}
# print(min_value(dct))

# def combine_dict(dct1, dct2):
#     return {**dct1, **dct2}
#
# dct1, dct2 = {"a": 10, "b": 20, "c": 5}, {"d": 15, "e": 25, "f": 35}
# print(combine_dict(dct1, dct2))

