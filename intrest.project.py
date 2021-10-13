#simple intrest calculator.

#date of present year

year = int(input("Enter present year "))
month = int(input("Enter present month "))
day = int(input("Enter present day "))
print()

#date of amount borrowed year

input_year = int(input("Enter money taken year  "))
input_month = int(input("Enter money taken month "))
input_day = int(input("Enter money taken day  "))

#calculating number of days from money taken year.

n_year = year - input_year
n_month = month - input_month
if n_month < 0:
    n_year = n_year - 1
    n_month = 12 - (input_month - month)
n_day = day - input_day
if n_day < 0:
    n_month = n_month - 1
    n_day = 31 - (input_day - day)

print()

#number of years months days

nyears=n_year
nmonths=n_month
days=n_day

#calculating intrest for the amount

#reading borrowed amount 
amount=int(input('Enter amount= '))

#reading rate of intrest
rate=float(input('Enter rate of intrest= '))
print()

#intrest for one month.

mon_int=(rate/100)*amount
day_int=mon_int/30
tot_di=day_int*days

#total intrest up to date
total_int=((nmonths+(nyears*12))*mon_int)+tot_di
print("Intrest for ",nyears,"Years",nmonths," Months",days,"Days =",total_int)
print()

#total amount till date
total=amount+total_int
print("Total Amount = ",total)



