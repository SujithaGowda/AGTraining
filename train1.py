import math

def checkpal(paltext):
    listpal = []
    for p in paltext:
        listpal.append(p)
    if listpal.reverse() == paltext:
        print("String {} is palindrome".format(paltext))
    else:
        print("String {} is not palindrome".format(paltext))    

def main():
    paltext = input("Enter String: ")
    checkpal(str(paltext))

def checkdiv7():
    for i in range(2000,3200,1):
        if i%7==0 and i%5!=0:
            print(i)

def revname():
    Name = raw_input("Enter name (first last):")
    fname,lname = str(Name).split(' ')
    print("{} {}".format(lname,fname))
    

def findvol():
    D = raw_input("Enter the diameter:")
    V = ( 4/3 * math.pi ) * (int(D)/2)**3
    print V

def strfunc():
    text = raw_input("Enter a string:")
    print("First 3 characters:{}".format(text[0:3]))
    print("Last 2 characters:{}".format(text[-2:]))
    print("Skip characters:{}".format(text[::2]))
    print("Reverse string:{}".format(text[::-1]))
    
if __name__ == '__main__':
    # checkdiv7()
    # revname()
    # findvol()
    strfunc()