def find_change(coins, amount):
    coins.sort(reverse=True)
    change=[]
    for coin in coins:
        while amount >= coin:
            change.append(coin)
            amount -= coin
        return change

products = {
    "молоко": 20,
    "хлеб": 30,
    "доширак": 15,
    "вареники": 50,
    "кирики": 90,
    "макароны": 80,
    "лит энергия": 45,
    "чипсы лаус": 10,
}
print("Список доступных продкутов: ")
for product in products:
    print(product)

product = input("\nВыберите товар: ").lower()
if product in products:
    price = products[product]
    payment = int(input("Введите сумму: "))
    
    if payment >= price:
        change_due = payment - price
        coins = [1,5, 7, 10, 15]
        change_coins = find_change(coins, change_due)
        
        print(f"Сдача: {change_due}p")
        print("Минимальное количество монет для сдачи:")
        for coin in change_coins:
            print(coin, end="р ")
        if payment == price:
            print("Без сдачи")
    else:
        print("Недостаточно средств")
else:
    print("Продукта нету")
