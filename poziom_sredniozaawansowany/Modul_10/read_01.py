with open("data_sample.txt") as f:
    datas = f.readlines()

print(f"Full data readed from file: {datas}")
full_data = []

for line in datas:
    line = line.strip().split(" ")
    print(f"Line split by SPACE: {line}")
    line_int = [int(x) for x in line]
    print(f"Data as integer: {line_int}")
    full_data.append(line_int)


print(f"Full data as integers: {full_data}")
