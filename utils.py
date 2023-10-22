def get_child_index(child_info):
    if len(child_info) > 1:
        for index, child in enumerate(child_info):
            print(f"{index + 1}: {child[1]}")
        selected_child = int(input("Select a child to assign the task: "))
        child_id = child_info[selected_child][0]
    else:
        selected_child = 0
        child_index = child_info
    return selected_child, child_index
