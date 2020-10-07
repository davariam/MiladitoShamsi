import os
from jalaali import Jalaali

#cmd = "date +%Y%m%d"
#currnetdate = os.popen(cmd).readlines()
bc_year = 2020
bc_month = 10
bc_day = 20
jalali_day = ""
jalali_month = ""
jalali_year = ""

jalaali_day_hash = (bc_year * 365) + (bc_month * 30) + bc_day - 226746
jalali_day = str(jalaali_day_hash % 365 % 30)
if len(jalali_day) == 1:
    jalali_day = "0" + str(jalali_day)

jalali_month = str((jalaali_day_hash % 365 // 30))
if len(jalali_month) == 1:
    jalali_month = "0" + str(jalali_month)

jalali_year = str(jalaali_day_hash // 365)

currnetdate_shamsi = jalali_year + jalali_month + jalali_day

cmd = "find ./ -name " + '"'+'*'+currnetdate_shamsi+'*.unl'+'"' + " | wc -l "
os.popen(cmd)
print(cmd)

print(Jalaali.to_jalaali(2020, 9, 30))
