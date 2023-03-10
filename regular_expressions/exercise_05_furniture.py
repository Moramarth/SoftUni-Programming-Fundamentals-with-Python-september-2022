import re

pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

bought_furniture = list()
total_cost = 0

command = input()

while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for item in bought_furniture:
    print(item)

print(f"Total money spend: {total_cost:.2f}")
