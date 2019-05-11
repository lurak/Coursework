from ADT.appropriatePlaces import AppropriatePlaces
from datetime import date
from Const_data.constData import RESORTS


resort_type = input("input cultural resorts, sea resorts or ski resorts: ")
arr_date = input("input arrival date (date-month-year): ").split('-')
dep_date = input("input departure date: ").split('-')
delta = date(int(dep_date[2]), int(dep_date[1][-1]), int(dep_date[0])) - \
        date(int(arr_date[2]), int(arr_date[1][-1]), int(arr_date[0]))

# If delta of days is greater than five delta will be five because of limit weather api
days = delta.days if delta.days <= 5 else 5
appropriatePlaces = AppropriatePlaces(RESORTS[resort_type], days)
while not appropriatePlaces.is_empty():
    city = appropriatePlaces.pop()
    city.wiki_information()
    print(city)
    print(city.extra_data['wiki information'])

