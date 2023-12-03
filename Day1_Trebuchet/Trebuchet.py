import re

def part_one():
    with open('Day1_Trebuchet\input.txt','r') as f: 
        data = f.read()
    data = data.split('\n')

    number = []

    for i in data: 
        number.append(re.sub("[a-z]","",i))

    sum = 0 

    for i in number:
        num = int(str(list(i)[0]) + str(list(i)[len(i) - 1]))
        sum = sum + num
    return(sum)

def part_two():
    with open(r'Day1_Trebuchet\input.txt','r') as f: 
        data = f.read()
    data = data.split('\n')
    
    num = ''
    sum = 0
    j = 0 
    numbers = []
    for i in data: 
        while j < len(i):
            if(i[j].isdigit()):
                num+=i[j]
                j+=1
            elif(i[j:j+3] == 'one'):
                num+='1'
                j+=2
            elif(i[j:j+3] == 'two'):
                num+='2'
                j+=2 
            elif(i[j:j+3] == 'six'):
                num+='6'
                j+=2
            elif (i[j:j+4] == 'four'):
                num+='4'
                j+=3
            elif(i[j:j+4] == 'five'):
                num+='5'
                j+=3
            elif(i[j:j+4] == 'nine'):
                num+='9'
                j+=3
            elif(i[j:j+5] == 'three'):
                num+='3'
                j+=4
            elif(i[j:j+5] == 'seven'):
                num+='7'
                j+=4
            elif(i[j:j+5] == 'eight'):
                num+='8'
                j+=4
            else:
                j +=1
        sum = sum + int(num[0] + num[len(num)-1])
        #numbers.append(int(num[0] + num[len(num)-1]))
        num = ''
        j = 0
    
    print (sum)

    
part_two()