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

