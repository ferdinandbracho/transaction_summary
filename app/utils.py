from datetime import date

def list_sum(list: list)-> float:
    """
    Return float sum of items in a list
    """
    total = 0
    for num in list:
        total  += num
    return total

def list_avg(list: list)-> float:
    """
    Return float avg of items in a list
    """
    return list_sum(list) / len(list)

def month_counter(dates: list)-> dict:
    """
    Return dict with number of transactions for each month present
    """
    result = {}
    for d in dates:
        d_list = d.split('/')
        py_date = date(1, int(d_list[0]), int(d_list[1]))
        month = py_date.strftime('%B')
        if month in result:
            result[month] += 1
        else:
            result.update({month: 1})

    return result