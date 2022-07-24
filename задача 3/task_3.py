file_1 = "1.txt"
file_2 = "2.txt"
file_3 = "3.txt"

def read_file_by_len(file_list):
    dict_1 = {}
    for file in file_list:
        with open(file, 'r', encoding = "UTF-8") as file_obj:
            line_number = len(file_obj.readlines())
            dict_1.setdefault(line_number, [file])
    return dict_1
read_file_by_len([file_1, file_2, file_3])

def write_sorted_file(file_list, new_file):
    dict_1 = read_file_by_len(file_list)
    sorted_list = sorted(dict_1.keys())
    for key in sorted_list:
        list = dict_1[key]
        for file in list:
            with open(file, encoding="utf-8") as f:
                data = (f.read()).strip()

            with open(new_file, "a", encoding="utf-8") as f:
                f.write(f"{file}\n{key}\n{data}\n")

write_sorted_file([file_1, file_2, file_3], "result_3.txt")