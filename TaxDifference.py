if __name__ == "__main__": 

    income = input("Please enter your taxable income: ")
    income = int(income)

    old_rates = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
    old_cuts =[18650, 75900, 153100, 233350, 416700, 470700, 1000000]

    new_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    new_cuts = [19050, 77400, 165000, 315000, 400000, 600000, 1000000]

    old_ranges = []
    new_ranges = []
    old_ranges.append(18650)
    new_ranges.append(19050)
    for i in range(1, len(old_cuts)):
        old_ranges.append(old_cuts[i] - old_cuts[i-1])
        new_ranges.append(new_cuts[i] - new_cuts[i-1])

    income_copy = income

    old_tax = 0
    new_tax = 0

    for i in range(len(old_ranges)):
        if income > old_ranges[i]:
            old_tax += old_rates[i] * old_ranges[i]
            income -= old_ranges[i]
        elif income > 0:
            old_tax += income * old_rates[i]
            income = 0

    income = income_copy
    for i in range(len(new_ranges)):
        if income > new_ranges[i]:
            new_tax += new_rates[i] * new_ranges[i]
            income -= new_ranges[i]
        elif income > 0:
            new_tax += income * new_rates[i]
            income = 0
        
    print("The tax for old rates for taxable income $%d is $%d."%(income_copy, old_tax))
    print("The tax for new rates for taxable income $%d is $%d."%(income_copy, new_tax))
