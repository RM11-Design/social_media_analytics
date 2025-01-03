import matplotlib.pyplot as plt
import csv

# x = [] 
# y = [] 

# with open('UCC Bangladesh Society 🇧🇩.csv','r',encoding="utf-8") as csvfile: 
#     plots = csv.reader(csvfile, delimiter = ',')
#     next(plots) 
                
#     for row in plots: 
#         x.append(row[0])
#         y.append(int(row[1]))

# plt.bar(x, y, color = 'g', width = 0.72, label = "Views") 
# plt.xlabel('Video Number') 
# plt.ylabel('Views') 
# plt.title('Views for each video comparsion') 
# plt.legend() 
# plt.show() 

with open('Ron’s gadget Review.csv','r',encoding="utf-8") as csvfile: 
     read_part = csv.reader(csvfile) 
     next(read_part, None)   

     values = []

     for row in read_part:
         value = float(row[2])
         values.append(value)
         avg = sum(values) / len(values)
     print(f"Average views: {avg:.0f}")