# def single_root_words(root_words, *other_words):
#
#     same_words = []
#
#     for i in other_words:
#         if root_words.lower() in i.lower() or i.lower() in root_words.lower():
#             same_words.append(i)
#
#     return same_words
#
#
# print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
# print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
def sumList(x):
    if x == []:
        return 0
    else:
        return x[0] + sumList(x[1:])


print(sumList([1, 2, 3, 4]))