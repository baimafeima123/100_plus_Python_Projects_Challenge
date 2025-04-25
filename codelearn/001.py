import sys
import time
import random



options = ["+","-","*","/"]
def get_div(anum):
    
    l = []
    for i in range(1,anum+1):
        if anum%i == 0:
            l.append(i)
    return random.choice(l)


def main():
    question = []
    start = time.time()
    while time.time()-start<=60:
        a = random.randint(1,99)
        op = random.choice(options)
        if op == '/':
            b = get_div(a)
        else:
            b = random.randint(1,99)
        a_op_b = str(a)+op+str(b)
        ans = int(eval(a_op_b))

        if 60-(time.time()-start) >= 0:
            try:
                kehu = int(input(a_op_b+'='))
            except:
                kehu = ""
            if kehu == ans:
                print("CORRECT!",end=" ")
            else:
                print("Wrong Answer",end=" ")
            remaintime = 60-(time.time()-start)
            print("remain time "+ str(remaintime)+ "second")
        else:
            break
            
        
        pass
if __name__ =='__main__':
    main()
    print("End the game")
