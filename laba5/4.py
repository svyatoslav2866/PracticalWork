old_stroka = input("ведите строку: ")
new_stroka = 'www'
else_stroka = 'zzz'

if old_stroka == 'abc':
    result = old_stroka.replace(old_stroka, new_stroka)
    print(result)
else:
    result2 = old_stroka + else_stroka
    print(result2)