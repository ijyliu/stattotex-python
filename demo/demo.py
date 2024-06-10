# demo.py
# This file demonstrates how to use the stattotex package
# You should run this file from the root directory of the repository

# First, we import stattotex (pip version)
from stattotex.stattotex import stattotex

# Suppose we had some calculated statistic
# For example, we could compute average monthly sales for a product over the previous quarter
# Suppose that this statistic takes on the value of 2,532.01 units
number = 2532.01
# Let us now save this number to the file "demo/demoNums.tex" with the name "AvgMonthlySales"
# We can use the setting clear_file=True to delete the file before writing to it
stattotex(number=number, number_name="AvgMonthlySales", filename="demo/demoNums.tex", clear_file=True)

# Let's say we wish to format this as 2,532.01
# We can directly format the number as a string, and feed strings to stattotex
f_number = "{:,.2f}".format(number)
# This function call will update the value of the number for LaTeX
stattotex(f_number, "AvgMonthlySales", "demo/demoNums.tex")

# stattotex will accept arbitrary string inputs
# Let's say our sales increased by 100.3% from the previous quarter
pct = 100.3
pct_string = str(pct) + "%"
stattotex(pct_string, "SaleIncPct", "demo/demoNums.tex")
if pct > 0.0:
    word = "increased"
elif pct == 0.0:
    word = "stayed the same"
else:
    word = "decreased"
stattotex(word, "SaleDir", "demo/demoNums.tex")
