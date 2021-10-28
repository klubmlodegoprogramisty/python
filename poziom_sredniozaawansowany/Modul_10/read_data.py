def read_from_file(file_name: str) -> list:

    with open(file_name) as f:
        datas = f.readlines()
    full_data = []

    for line in datas:
        line = line.strip().split(" ")
        line_int = [int(x) for x in line]
        full_data.append(line_int)

    return full_data
