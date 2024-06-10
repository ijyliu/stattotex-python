# Import module from "stattotex/stattotex.py"
# Add to path
import sys
sys.path.append('stattotex')
from stattotex import stattotex

# Suppose we had some calculated statistic
# For example, we could compute the average number of employees in a company from a dataset
# Suppose that formatted, it takes on the value 2,532.01
number = 2532.01
f_number = "{:,.2f}".format(number)
print('Formatted Number:', f_number)

# Let us now save this number to the file "AvgEmps.tex" with the name "AvgEmps"
stattotex(number, "AvgEmps", "AvgEmps.tex")

# Check the .tex file "EmpReport.tex" for a continuation of this example
