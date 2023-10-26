def get_child_index(child_data, allow_selection=False):
    if len(child_data) > 1 and allow_selection:
        for index, child in enumerate(child_data):
            print(f"{index + 1}: {child[1]}")
        child_index = int(input("Select a child to assign the task: ")) - 1
        child_id = child_data[child_index][0]
    else:
        child_index = 0
        print(child_data)
        child_id = child_data[0][0]
    return child_index, child_id