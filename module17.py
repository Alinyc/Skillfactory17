per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму предполагаемого вклада: "))
tkb=round(5.6*money/100,(2))
skb=round(5.9*money/100,(2))
vtb=round(4.28*money/100,(2))
sber=round(4.0*money/100,(2))
deposit = [tkb, skb, vtb, sber]
print('Накопленные средства за год вклада в каждом из банков: ', deposit)
deposit_max = max(deposit)
print('Максимальная сумма, которую вы можете заработать —', deposit_max)