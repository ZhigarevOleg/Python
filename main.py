per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите желаемую сумму:"))
deposit=list(per_cent.values())
for i in range(len(deposit)):
    deposit[i]=int((deposit[i]*money)/100)
print(f"{deposit}- Накопленные средства за год вклада")
deposit_max=max(deposit)
print("Максимальная сумма, которую вы можете заработать —",deposit_max)
