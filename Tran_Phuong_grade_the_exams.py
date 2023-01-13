import statistics as stt
import re
import pandas as pd
while True:
    filename = input("Enter a filename: ")
    try:
        with open(filename+'.txt',"r") as data:
            Data = data.read()
            print(filename+" is opened successfully!")
    except:
        print("File cannot be found")
    else:
        break
print("****REPORT****")
# Task2.1 The total line in data:
Dataline=Data.splitlines()
L=len(Dataline)
print("The total line of Data is:",L)

# Task 2.2. Number of valid line:

#Calculate the number of invalid line and print out:
b=0 # biến đếm số dòng không hợp lệ
c=list() #list các dòng không hợp lệ
MA=re.findall('N[0-9]{8,8}',Data) # List chứa ID hợp lệ

for i in range(len(Dataline)):
    Dataline[i]=Dataline[i].split(',')
    if len(Dataline[i]) != 26 or Dataline[i][0] not in MA: 
    #Nếu dataline[i] bất kì chứa nhiều hơn hoặc ít hơn 26 phần tử hoặc số ID không khớp với kiểu ID hợp lệ
        b+=1 
        c.append(Dataline[i])
for i in range(len(c)):
    print("Invalid line of data: does not contain exactly 26 values:\n",c[i])
print("Total valid line of data: ",L-b)
print("Total invalid lines of data: ",b)
Valid=[s for s in Dataline if s not in c]

#Task 3
#Mark for students: chấm điểm cho thí sinh
answer_key =['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D']
std_grade={}
empty_ans={}
incr_ans={}
# Create function to check the number of empty answers: Tạo hàm để check số câu trả lời trống và tỷ lệ của nó.
def check_emptyans(b,a):
    if b not in a:
        a.setdefault(b,[1,1/(L)])       
    else:
        for key in a.keys():
            if b == key:
                a[key][0]+=1
                a[key][1]=round(a[key][0]/(L),2)     
    return(a)        

# Create function to check the number of incorrects answers: Tạo hàm để check số câu trl sai và tỷ lệ của nó  
def check_incrans(b,a):
    if b not in a:
        a.setdefault(b,[1,1/(L)])
    else:
        for key in a.keys():
            if b == key:
                a[key][0]+=1
                a[key][1]=round(a[key][0]/(L),2)
    return(a)          
for i in range(len(Valid)):
    mark=0
    for j in range(len(answer_key)):
        try:
            if Valid[i][j+1] == '':
                mark=mark
                check_emptyans(j+1,empty_ans)
            elif Valid[i][j+1] == answer_key[j]:
                mark+=4
            else:
                mark-=1
                check_incrans(j+1,incr_ans) 
        except:
            break

    std_grade.setdefault(Valid[i][0],mark) 

Maxx1=0
Maxx2=0
for key in empty_ans.keys():
    if empty_ans[key][1] >= Maxx1:
        Maxx1= empty_ans[key][1]
for key in incr_ans.keys():
    if incr_ans[key][1] >= Maxx2:
        Maxx2= incr_ans[key][1]


s1="Question that most people skip: "
for key in sorted(empty_ans.keys()):
    if empty_ans[key][1] == Maxx1:
        s1+=str(key) + " - "+str(empty_ans[key][0])+" - "+str(empty_ans[key][1])+", "
print(s1[:-2])
s2="Question that most people answer incorrectly: "
for key in sorted(incr_ans.keys()):
    if incr_ans[key][1] == Maxx2:
        s2+=str(key) + " - "+str(incr_ans[key][0])+" - "+str(incr_ans[key][1])+", "
print(s2[:-2])

std_result=list(std_grade.values())
no_highresult=0
avg_scr= stt.mean(std_result)
highest_scr=max(std_result)
lowest_scr=min(std_result)
range_of_scr= highest_scr - lowest_scr
median_csr=stt.median(std_result)
for value in std_result:
    if value > 80:
        no_highresult +=1
print("**** ANALYZING ****")
print("Total student of high scores: ",no_highresult)
print("Mean(average) score: ",avg_scr)
print("Highest score: ", highest_scr)
print("Lowest score: ",lowest_scr)
print("Range of score: ",range_of_scr)
print("Median score: ",median_csr)

#Task 4
Class_grade={'StdID':std_grade.keys(),'Mark':std_grade.values()}
Class_grade1=pd.DataFrame(Class_grade)
with open(filename+'_grade.txt',"w") as resultt:
    resultt.write("This is grade of "+filename+"\n")
    Class_grade1.to_string(resultt)
resultt.close()



    





















