# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
#  При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
# операцией, даже ошибочной
# Любое действие выводит сумму денег


                                # Пополнение
MULTIPLICITY = 50 
balans = 0
count = 3
add_sum = int(input("Введите сумму для пополнения счета : "))
if add_sum >= MULTIPLICITY and add_sum% MULTIPLICITY == 0:
    balans=+add_sum
    print(f"Ваш баланс: {balans}")
else:
    print("Сумма пополнения должна быть кратна 50")
    print(f"Ваш баланс : {balans}")

                                 # Снятие 
take_sum = int(input("Введите сумму для снятия со счета : "))
if take_sum > balans:
    print(f"На вашем счете недостаточно средств!")
    print(f"Ваш баланс : {balans}")
elif take_sum >= MULTIPLICITY and take_sum% MULTIPLICITY == 0:
    balans =-take_sum
    print(f"Ваш баланс: {balans}")
else:
    print("Сумма пополнения должна быть кратна 50")
    print(f"Ваш баланс : {balans}")