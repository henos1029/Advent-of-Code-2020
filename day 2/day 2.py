import os
os.chdir('C:\\Users\\SPI0003\\OneDrive - boxhillhs.vic.edu.au\\Home\\Coding\\advent of code')

with open('day 2.txt') as r:
  r = r.read()

# nr = [items.strip("\n") for items in r]

# listx = []
# count = 0
# for items in nr:
#     count += 1
#     fir = items.split(': ')[0].split(" ")[0].split("-")[0]
#     sec = items.split(': ')[0].split(" ")[0].split("-")[1]
#     letter = items.split(': ')[0].split(" ")[1].strip(" ")[0]
#     string = items.split(': ')[1].split(" ")[0].strip(" ")
#     print(f"{fir},{sec},{letter},{string}")
#     listx.append(f"{fir},{sec},{letter},{string}")

# this was a fail (below)

# count = 0
# finalcount = 0
# for x in listx:
#     listy = x.split(',')
#     print(listy)
#     if listy[2] in listy[3]:
#         for x in listy[3]:
#             if x == listy[2]:
#                 count += 1
#         if count >= int(listy[0]) and count <= int(listy[1]):
#             finalcount += 1
#     count = 0
# print(finalcount)
# count = 0
# finalcount = 0
# for x in listx:
#     listy = x.split(',')
#     print(listy)
#     for x in listy[3]:
#         try:
#             no1 = x[int(listy[0])]
#         except IndexError:
#             continue
#         try:
#             no2 = x[int(listy[1])]
#         except IndexError:
#             continue
#         if no1 == listy[2] or no2 == listy[2]:
#             finalcount += 1
#     count = 0
# print(finalcount)
# print(len(listx))
passwords = r.split('\n')

valid = 0
for p in passwords:
    password = p[p.index(': ') + 2:]
    policy = p[:p.index(':')]
    first = int(policy[:policy.index('-')])
    second = int(policy[policy.index('-') + 1:policy.index(' ')])
    letter_to_check = policy[policy.index(' ')+1:policy.index(' ')+2]
    if password[first-1] == letter_to_check:
        if password[second-1] != letter_to_check:
            valid += 1
    elif password[second-1] == letter_to_check:
        if password[first-1] != letter_to_check:
            valid += 1

print(valid)
