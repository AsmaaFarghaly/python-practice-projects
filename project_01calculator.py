print("---Age in days calculator---\n")

age = float(input("enter your age in years:  "))

print("you have lived for " + str(age * 365) + " days")

print("\n")

print("---Age in days calculator---\n")
age_years = input("enter your age in years:  ")
age_years = int(age_years)

age_days =age_years*365
print(f"you have lived for {age_days} days.")


#challenge

print("---Age in days calculator---\n")
age_years = input("enter your age in years:  ")
age_years = int(age_years)

age_days =age_years*365
age_months = age_years*12
age_hours = age_days*24

print(f"you have lived for {age_months} months.")
print(f"you have lived for {age_days} days.")
print(f"you have lived for {age_hours} hours.")