import sys
import time
import random
import logging

logging.basicConfig(
    filename="./codelearn/log/01.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

timeset = 60
options = ["+","-","*","/"]
def get_div(anum):
    
    l = []
    for i in range(1,anum+1):
        if anum%i == 0:
            l.append(i)
    return random.choice(l)


def main():
    logging.info("开始游戏")
    question = []
    correct_num = 0
    wrong_num = 0
    start = time.time()
    while time.time()-start<=timeset:
        a = random.randint(1,99)
        op = random.choice(options)
        if op == '/':
            b = get_div(a)
        else:
            b = random.randint(1,99)
        a_op_b = str(a)+op+str(b)
        ans = int(eval(a_op_b))
        a_op_b_str = a_op_b+"="
        question.append(a_op_b_str+str(ans))

        if (time.time()-start) <=timeset:
            try:
                kehu = int(input(a_op_b_str))
            except:
                kehu = ""
            if kehu == ans:
                correct_num+=1
                print("CORRECT!",end=" ")
            else:
                wrong_num+=1
                print("Wrong Answer",end=" ")
            
            remaintime = timeset-(time.time()-start)
            print("remain time "+ str(remaintime)+ "second")
        else:
            break
    
    print("End the game,总题数为{:d},正确率为：{:.2f}".format(correct_num+wrong_num,correct_num/(correct_num+wrong_num)),end=" ")
    logging.info("End the game,总题数为{:d},正确率为：{:.2f}".format(correct_num+wrong_num,correct_num/(correct_num+wrong_num)))
    print("the question's answer is :")
    for item in question:
        print(item)
    print("see you next time")

    
    pass
if __name__ =='__main__':
    main()
