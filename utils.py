def get_child_index(child_data, allow_selection=False):
    """
    Get child index and ID based on user input.

    Args:
        child_data (list): List of child data.
        allow_selection (bool, optional): Allow user selection if there are multiple children.

    Returns:
        tuple: Index and ID of the selected child.
    """
    if len(child_data) > 1 and allow_selection:
        for index, child in enumerate(child_data):
            print(f"{index + 1}: {child[1]}")
        child_index = int(input("Select a child to assign the task: ")) - 1
        child_id = child_data[child_index][0]
    else:
        child_index = 0
        child_id = child_data[0][0]
    return child_index, child_id