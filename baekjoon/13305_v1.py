n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_cost = 0

while(road):
    min_price_index = price.index(min(price))
    min_cost += sum(road[min_price_index:])*price[min_price_index]
    road = road[:min_price_index]
    price = price[:min_price_index]

print(min_cost)
