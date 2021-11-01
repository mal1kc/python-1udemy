# import string
# import time
# import re
#
# #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# #print(time.localtime())
#
# aranılacak_metin ='''
# abcdefghijklmnopqrstuvwxyz
#
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
# 1234567890
#
# Ha HaHA
#
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? +{ } [ ] \ | ( )
#
# coreyms.com
#
# 321-555-4321
# 123.555.1234
#
# Mr .Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
# '''
#
# cumle = 'Start a sentence and then bring it to an end'
#
# desen = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#
# eslesmeler = desen.finditer(aranılacak_metin)
#
# for eslesme in eslesmeler:
#     print(eslesme)
#
# print()
# importing libraries
dictt = dict(dict())
for i in range(100):
    dictt[i]["a"] = i
    dictt[i]["b"] = i
