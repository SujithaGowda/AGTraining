def printstar(oddno):
    len = int(oddno) / 2
    count = 0
    # print(len)
    for i in range(int(oddno)):
        if i <= len:
            x = '*' * (count + 1)
            count = count + 1
            print(x)
        else:
            x = '*' * (count - 1)     
            count = count - 1
            print(x)

def sortdict():
    student_data = {'id1':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
    },
    'id2':
    {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
    },
    'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
    },
    'id4':
    {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
    },
    }

    z = {}
    print(student_data)
    print('****')
    print(sorted(student_data))
    print('****')
   
    for key, value in student_data.items(): 
        if value not in z.values():
            z[key] = value

    print(z)

    # y = set()
    # x = sorted(student_data.values())
    # z = student_data.values()
    # print(list(z))
        
#fibonacci        
def fibo(n):
    x = 1
    y = 1
    for no in range(n):
        x,y = y,x+y
        yield x
        
def maptest():
    list1 = [4,5,6,7]
    list2 = [1,2,3,9]
    
    d1 = {'t1':2,'t2':3,'t3':4}
    # res1 = map(mul,d1)
    res1 = map(mul,list1)
    
    print(res1)

def mul(x):
    return x * 2

def redfunc():

    list1 = [1,2,3,4]
    z = reduce(lambda x,y: x % y,list1)
    print(z)

def filfunc():
    list1 = [15,100,35,50,14]
    z = reduce(lambda z1,z2 : z1+z2,filter(lambda x: x < 55,list1) )
    print(z)

if __name__ == '__main__':
    # oddno = raw_input("Enter an odd no.:")
    # printstar(oddno)      
    # sortdict()      
    # squareno(4)

# fibonacci    
    # n = raw_input("Enter no.:")
    # for num in fibo(int(n)):
    #     print(num)
    # maptest()
   
    # redfunc()
    filfunc()
 


    