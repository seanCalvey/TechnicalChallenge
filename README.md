## Payslip Technical Challenge

### imports
pandas
openpyxl
pathlib

### Challenge (Create unit tests)
(1) The file is type excel

In this challenge I check the extentsion of the file has `.xlsx`
to fail this test I pass the unit a `.txt` file

(2) The GTN file contains line breaks i.e. empty lines

In this challenge I use the `.dropna()`with the `how` param to find any
empty row and then count the rows before and after if the rows count match
this mean there was no empty rows

(3) The GTN file header structure has changed e.g. there are two header rows instead of one

In this challenge I use the `.dtype` to get the amount of different types if there is just 
type objtect this mean the column contains a string. I use the `header` param to remove each
header row until there more that one dtype

(4) Employees are Present in the Payrun File but missing in the GTN file.

In this challenge I extract the "employee_id" from GNT and the "Employee ID" from Payrun 
as a Series and compare the to Series. I had to change the Payrun Series from float and 
to int32

(5) Employees are Present in the GTN but missing in the Payrun File.

---

(6) Pay Elements in the GTN file do not have a mapping in the Payrun File.

In this challege I compare to dataframes. I used the equals method to check the two frames

(7) Pay Elements in the Payrun file do not have a mapping in the GTN File.

---
(8) For Pay Elements in the GTN file, the values have a numeric type. 

In this challege I extract to pay elements. Then I use the `dtype` to get a 
Series of the type of colums. Then I use a helper method to loop through the
Series an check each type. If the pay contains a object or string I return a false

