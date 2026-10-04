Name = input("Enter the Customer Name:")
DOB = int(input("Enter the Date:"))
LoanAmount = float(input("Enter the Loan Amount:"))

if DOB <= 2008:
    print("You're eligible for loan.")

    if LoanAmount >= 50000:
        print("Congratulations! Your Loan has been Disbursed Successfully.")
    else:
       print("Loan Amount should be 50000 or more.")

else:
    print("You're ineligible for Loan.")
    

                    
