from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import app.config as config

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


def send_email(to_email, subject, template_id, data) -> bool:
    """
    Send Email using Sendgrid integration

    Return
        - Bool value indicating in operation was success or not
    """

    message = Mail(
        from_email='whatacupset@gmail.com',
        to_emails=to_email,
        subject=subject,
    )
    message.template_id = template_id
    message.dynamic_template_data = {
        'total': data['total_balance'],
        'avg_debit': data['avg_debit'],
        'avg_credit': data['avg_credit'],
        'month_transactions': data['month_transactions'],
    }
    try:
        sg = SendGridAPIClient(config.SENDGRID_API_KEY)
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        return True
    except Exception as e:
        print(e)
        print(e.message)
        return False