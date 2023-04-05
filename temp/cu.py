aqui = open('aqui.txt', mode='rt', encoding='utf-8')
foi = open('foi.txt', mode='wt', encoding='utf-8')

for x in aqui:
    lst = x.split('	')
    txt = '('
    for w in lst:
        if w == None:
            f"NULL, "
        if w == lst[-1]:
            w = w.rstrip()
            txt += f"'{w}'),\n"
        else:
            txt += f"'{w}', "
    foi.write(txt)

aqui.close()
foi.close()

# aqui = open('aqui.txt', mode='rt', encoding='utf-8')
# foi = open('foi.txt', mode='wt', encoding='utf-8')
#
# for x in aqui:
#     lst = x.split('	')
#     txt = '('
#     pau = ''
#     for w in lst:
#         if w == lst[-1]:
#             w = w.rstrip()
#             pau = f"'{w}'),\n"
#         else:
#             pau = f"'{w}', "
#
#         if pau == "'', ":
#             pau = "NULL, "
#         txt += pau
#     foi.write(txt)
#
# aqui.close()
# foi.close()

print('dfs')
