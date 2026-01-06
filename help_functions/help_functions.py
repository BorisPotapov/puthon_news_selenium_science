from datetime import datetime


def data_now():

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("YYYY-MM-DD")
    print("date and time =", dt_string)
    return dt_string


