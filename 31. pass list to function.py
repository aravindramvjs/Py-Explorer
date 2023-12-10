def name_len(*names):
    for i in names:
        if len(names)==5:
            print('it has 5 letters')
        else:
            print('it has more than or less than 5 letters')

names=name_len('aravi')
print(names)
print(len('aravi'))