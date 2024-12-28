def calculate_interest(principal,rate,time):
  
simple_interest=(principal*rate*time)/100
compound_interest=principal*((1+rate/100)**time)-principal
return simple_interest,compound_interest

principle=float(input("Enter the principle amount (in INR): "))
rate=float(input("Enter the rate of interest (in %): "))
time=float(input("Enter the time period (in years): "))

simple_interest,compound_interest=calculate_interest(principle,rate,time)

print(f"\nSimple Interest: Rs.{simple_interest:.2f}")
print(f"\nCompound Interest: Rs.{compound_interest:.2f}")
