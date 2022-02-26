Table_Value = int(float(input("Table of: ")))
Table_Length = int(float(input("How many Tables: ")))
for i in range(Table_Length + 1):
    print("{} X {} =".format(i, Table_Value), i * Table_Value)
print("Done!")
