# int_list = list(range(2, 16))
# print(int_list)

# for i in range(5, 106, 25)[::-1]:
#     print(i)

x = list(range(0, 12))
print(x)
if (len(x) % 2) == 0:
    a = x[-2::-2]
    x[::2] = a
else:
    a = x[::-2]
    x[::2] = a
print(x)