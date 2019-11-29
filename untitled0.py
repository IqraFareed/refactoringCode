

import re




def identifier(user):
    rgx='^[A-Za-z_]+[A-Za-z0-9]*$'
    flg=re.match(rgx, user)
    return flg

def digit(user):
    rgx=r"^[0-9]+$"
    flg=re.match(rgx, user)
    return flg

def statement(user):
    rgx='^(^(int|double|float|String|boolean|char)$)(^[A-Za-z_]+[A-Za-z0-9]*$)\s*[0-9]+;$'
    flg=re.match(rgx, user)
    return flg

def operator(user):
    rgx=r"(&&|\|\|+|-|*)"
    flg=re.match(rgx, user)
    return flg

def dataType(user):
    rgx=r"^(int|double|float|String|boolean|char)$"
    flg=re.match(rgx, user)
    return flg

def forLoop(user):
    rgx=r"^for\s*\(\s*int\s*[a-zA-Z]+\s*=[0-9]+;\s*[a-zA-Z]+(<=|>=|<|>)[0-9]+;\s*[a-zA-Z++--]+\)$"
    flg=re.match(rgx, user)
    return flg

def foreachLoop(user):
    rgx=r"^for\s*\((int|char|string)\s*[a-zA-Z]+\s*(:)\s*[a-zA-Z]+\)$"
    flg=re.match(rgx, user)
    return flg

def whileLoop(user):
    rgx=r"^while\s*\([a-zA-Z]+(<=|>=|==|<|>|!=)\s[a-zA-Z0-9]\)\{\s\}$"
    flg=re.match(rgx, user)
    return flg

def doWhileLoop(user):
    rgx=r"^do\{\s*\}\s*while\s*\([a-zA-Z]+(<=|>=|==|<|>|!=)\s[a-zA-Z0-9]*\)$"
    flg=re.match(rgx, user)
    return flg

def ifStatement(user):
    rgx=r"^if\s*\([a-zA-Z]+(==|=|<=|>=|<|>)[a-zA-Z0-9]\s*(&&|\|\|)\s[a-zA-Z](==|=|<=|>=|<|>)[a-zA-Z0-9]\s\)*$"
    flg=re.match(rgx, user)
    return flg

def result(user):
    
    if(identifier(user)!=None):
        print("It is an identifier")
    
    elif(digit(user)!=None):
        print("It is a digit")
        
    elif(statement(user)!=None):
        print("It is a statement")
    
    elif(operator(user)!=None):
        print("It is an operator")
        
    elif(dataType(user)!=None):
        print("It is a data type")
        
    elif(forLoop(user)!=None):
        print("It is a for loop")
        
    elif(foreachLoop(user)!=None):
        print("It is a for each loop")
        
    elif(whileLoop(user)!=None):
        print("It is a while loop")
        
    elif(doWhileLoop(user)!=None):
        print("It is a do while loop")
        
    elif(ifStatement(user)!=None):
        print("It is an if statement")
        
    else:
        print("You are wrong")
            
    

x=1
print("**LEXICAL ANALYZER**")
print("......................")
while(x==1):
    user=input("Enter Input: ")
    print("......................")
    print("")
    result(user)
    print("............................")
    print("To enter another input press 1")
    print("Press any other digit to end")
    u=input("Enter Input: ")
    if(u==1):
        x=1
    else:
        x=2
