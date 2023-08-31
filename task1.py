#Напишите программу, которая получает целое 
#число и возвращает его шестнадцатеричное 
#строковое представление. Функцию hex 
#используйте для проверки своего результата.

BASE_HEX = 16
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

num = int(input('Введите целое число: '))
entered_number = num
result = ' '
while num:
    result1 = num%BASE_HEX
    result = conversion_table[result1] + result
    num //= BASE_HEX
    
print()  
print (f'{entered_number} в шестнадцатеричной системе счисления : { result}')
print()
print (f'Проверка при помощи функции hex: {hex(entered_number)[2:] }')

#print('\n' + '=' * 20 + '\n')