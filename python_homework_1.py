from datetime import datetime
import random
import re


#================================================================ FIRST TASK =======================================================#

def get_days_from_today(date:str):
    try:
        year,month,day=date.split('-')
        today_date=datetime.today()
        datetime_object=datetime(year=int(year),month=int(month),day=int(day))
        return (today_date-datetime_object).days
    
    except ValueError:
        print('Wrong date format! The correct format is "YYYY-MM-DD"')

#================================================================ SECOND TASK =======================================================#

MIN_POSSIBLE_VALUE=1
MAX_POSSIBLE_VALUE=1_000

def get_numbers_ticket(min:int, max:int, quantity:int):
    try:
        max_sample_values=max+1 # include max to sample

        if min<MIN_POSSIBLE_VALUE or max >MAX_POSSIBLE_VALUE or quantity<MIN_POSSIBLE_VALUE or quantity> max_sample_values-min:
           raise ValueError
        
        return sorted(random.sample(range(min,max_sample_values), quantity))
    
    except ValueError: return 'Wrong parameters'

#================================================================ THIRD TASK =======================================================#
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
def normalize_phone(phone_number:str):
    replaced_number= re.sub(r"\D",r'', phone_number)
    if replaced_number.startswith('38'):
        return f"+{replaced_number}"
    elif replaced_number.startswith('0'):
        return f"+38{replaced_number}"
    else : return replaced_number



