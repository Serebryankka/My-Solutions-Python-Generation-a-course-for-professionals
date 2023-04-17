from datetime import datetime


def is_available_date(booked_dates, date_for_booking):
    for b_d in booked_dates:
        if len(b_d) > 10:
            b_d1, b_d2 = map(lambda x: datetime.strptime(x, '%d.%m.%Y'), b_d.split('-'))
            if len(date_for_booking) > 10:
                d_f_b1, d_f_b2 = map(lambda x: datetime.strptime(x, '%d.%m.%Y'), date_for_booking.split('-'))
                if b_d1 <= d_f_b1 <= b_d2 or b_d1 <= d_f_b2 <= b_d2 or d_f_b1 <= b_d1 <= d_f_b2 or d_f_b1 <= b_d2 <= \
                        d_f_b2:
                    return False
            else:
                if b_d1 <= datetime.strptime(date_for_booking, '%d.%m.%Y') <= b_d2:
                    return False
        else:
            if len(date_for_booking) > 10:
                d_f_b1, d_f_b2 = map(lambda x: datetime.strptime(x, '%d.%m.%Y'), date_for_booking.split('-'))
                if d_f_b1 <= datetime.strptime(b_d, '%d.%m.%Y') <= d_f_b2:
                    return False
            else:
                if datetime.strptime(b_d, '%d.%m.%Y') == datetime.strptime(date_for_booking, '%d.%m.%Y'):
                    return False
    return True
