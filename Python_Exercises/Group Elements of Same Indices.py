def  group_elements(list):
    new_list, max_elements = [], 0
    for i in range(len(list)):
        max_elements = max(max_elements, len(list[i]))
    for i in range(max_elements):
        current_list = []
        for item in list:
            if len(item) > i:
                current_list.append(item[i])
        new_list.append(current_list)
        
    return new_list

list = [[1, 2], [3, 4, 5, 6], [7, 8, 9]]
print(group_elements(list))
