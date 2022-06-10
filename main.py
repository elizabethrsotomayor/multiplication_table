def multi_table(number: int) -> str:
    """
    Return multiplication table for number that is always an integer from 1 to 10.
    :param number:
    :return:
    """
    table = ""
    for i in range(1, 11):
        val = i * number
        if i < 10:
            table += str(f"{i} * {number} = {val}\n")
        else:
            table += str(f"{i} * {number} = {val}")

    return table
