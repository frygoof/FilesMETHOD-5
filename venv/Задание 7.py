import json
profit_dict = {}
total_profit = 0
with open("прибыль.txt", "r") as file:
    for line in file:
        name, ownership, revenue, expenses = line.strip().split()
        revenue, expenses = int(revenue), int(expenses)
        profit = revenue - expenses
        profit_dict[name] = profit
        total_profit += max(profit, 0)
num_profitable_firms = len([firm for firm, profit in profit_dict.items() if profit > 0])
average_profit = total_profit / num_profitable_firms if num_profitable_firms > 0 else 0

result_list = [profit_dict, {"average_profit": average_profit}]
with open("прибыль.json", "w") as json_file:
    json.dump(result_list, json_file)
print("Результаты сохранены")
