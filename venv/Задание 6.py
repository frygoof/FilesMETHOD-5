import re
subject_dict = {}
with open('subjects.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(':')
        subject_name = parts[0].strip()
        data = re.findall(r'\d+\(\w+\)', parts[1])
        total_hours = sum(int(re.search(r'\d+', item).group()) for item in data)
        subject_dict[subject_name] = total_hours
print(subject_dict)
