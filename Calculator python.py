import math


def mortgage_calculator(loan_amount, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    total_payments = years * 12
    monthly_payment = (loan_amount * monthly_rate) / (1 - math.pow((1 + monthly_rate), -total_payments))
    return round(monthly_payment, 2)

def investment_return_calculator(initial_investment, annual_rate, years):
    future_value = initial_investment * math.pow((1 + annual_rate / 100), years)
    return round(future_value, 2)

def savings_goal_calculator(goal_amount, years, annual_rate):
    monthly_rate = annual_rate / 100 / 12
    months = years * 12
    monthly_savings = goal_amount * monthly_rate / (math.pow((1 + monthly_rate), months) - 1)
    return round(monthly_savings, 2)

def income_tax_calculator(income, deductions, filing_status):
    taxable_income = income - deductions
    if filing_status == "single":
        if taxable_income <= 9950:
            tax = taxable_income * 0.10
        elif taxable_income <= 40525:
            tax = 995 + (taxable_income - 9950) * 0.12
        elif taxable_income <= 86375:
            tax = 4664 + (taxable_income - 40525) * 0.22
        else:
            tax = 14751 + (taxable_income - 86375) * 0.24
    else:  # married
        if taxable_income <= 19900:
            tax = taxable_income * 0.10
        elif taxable_income <= 81050:
            tax = 1990 + (taxable_income - 19900) * 0.12
        elif taxable_income <= 172750:
            tax = 9328 + (taxable_income - 81050) * 0.22
        else:
            tax = 29502 + (taxable_income - 172750) * 0.24
    return round(tax, 2)

def process_bulk_calculations(file_path, output_file):
    df = pd.read_csv(file_path)
    
    df['Monthly Mortgage Payment'] = df.apply(lambda row: mortgage_calculator(row['Loan Amount'], row['Annual Interest Rate'], row['Loan Term']), axis=1)
    df['Future Investment Value'] = df.apply(lambda row: investment_return_calculator(row['Initial Investment'], row['Expected Return Rate'], row['Investment Years']), axis=1)
    df['Monthly Savings Required'] = df.apply(lambda row: savings_goal_calculator(row['Savings Goal'], row['Time Frame'], row['Expected Return Rate']), axis=1)
    df['Estimated Tax Liability'] = df.apply(lambda row: income_tax_calculator(row['Annual Income'], row['Deductions'], row['Filing Status']), axis=1)
    
    df.to_csv(output_file, index=False)
    print(f"Bulk calculations completed. Results saved to {output_file}")

def main():
    while True:
        print("\nFinancial Planning Toolkit")
        print("1. Mortgage Calculator")
        print("2. Investment Return Calculator")
        print("3. Savings Goal Calculator")
        print("4. Income Tax Calculator")
        print("5. Bulk Calculation (CSV File)")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            loan = float(input("Enter loan amount: "))
            rate = float(input("Enter annual interest rate (in %): "))
            term = int(input("Enter loan term (in years): "))
            print(f"Your monthly mortgage payment is: ${mortgage_calculator(loan, rate, term)}")
        elif choice == '2':
            invest = float(input("Enter initial investment amount: "))
            rate = float(input("Enter expected annual return rate (in %): "))
            years = int(input("Enter investment time horizon (in years): "))
            print(f"The future value of your investment is: ${investment_return_calculator(invest, rate, years)}")
        elif choice == '3':
            goal = float(input("Enter savings goal amount: "))
            years = int(input("Enter time frame (in years): "))
            rate = float(input("Enter expected annual return rate (in %): "))
            print(f"You need to save ${savings_goal_calculator(goal, years, rate)} per month to reach your goal.")
        elif choice == '4':
            income = float(input("Enter your annual income: "))
            deductions = float(input("Enter total deductions: "))
            status = input("Enter filing status (single/married): ").lower()
            print(f"Your estimated tax liability is: ${income_tax_calculator(income, deductions, status)}")
        elif choice == '5':
            file_path = input("Enter input CSV file path: ")
            output_file = input("Enter output CSV file path: ")
            process_bulk_calculations(file_path, output_file)
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
