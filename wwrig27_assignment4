import csv 

student_name = "William Wright"

in_file = open("/kaggle/input/vehcile-mpg/mpg.csv", "r")

mpg_reader = csv.reader(in_file)
next(mpg_reader) 

num_auto = 0
sum_city = 0
num_hwy = 0
sum_hwy = 0
sum_ford = 0
num_ford = 0
sum_suv = 0
num_suv = 0

for row in mpg_reader:
    sum_city = sum_city + int(row[8])
    num_auto = num_auto + 1

    sum_hwy = sum_hwy + int(row[9])
    num_hwy = num_hwy + 1
    
    if row [1] == 'ford':
        num_ford = num_ford + 1
        sum_ford = sum_ford + int(row[9])
        
    if row [11] == 'suv':
        num_suv = num_suv + 1 
        sum_suv = sum_suv + int(row[8])
      

avg_city = sum_city/num_auto    
print(sum_city/ num_auto)
avg_hwy = sum_hwy / num_hwy
print (sum_hwy / num_hwy)
ford_hwy = sum_ford / num_ford
print(sum_ford / num_ford)
suv_city = sum_suv / num_suv
print(sum_suv / num_suv)

out_file = open('wwrig27.assignment4.txt','w')
out_file.write('the avg city mpg is ' + str(avg_city) + '\n')
out_file.write('the avg hwy mpg is ' + str(avg_hwy) + '\n')
out_file.write('the avg hwy mpg for ford is ' + str(ford_hwy) + '\n')
out_file.write('the avg city mpg for suv is ' + str(suv_city))


in_file.close()
out_file.close()