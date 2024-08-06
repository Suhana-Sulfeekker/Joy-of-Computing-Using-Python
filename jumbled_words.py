import random

def choose():
    words=["apple","banana","carrot","dragonfruit","egg","fork","goose","horn","igloo"]
    pick=random.choice(words)
    return pick

def jumble(word):
    x="".join(random.sample(word,len(word)))
    return x

def thank(p1name,p2name,pp1,pp2):
    print("\n\n",p1name," scored ",pp1,sep="")
    print(p2name,"scored",pp2)
    print("Thank you for playing :)")
    print ("Have a Nice Day !!")
    
    
def play():
    p1name=input("Player 1,please input your name:")
    p2name=input("Player 2, please input your name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if turn%2==0:
            print(p1name,"Your turn")
            ans=input("Answer:")
            if ans==picked_word:
                pp1+=1
                print("Score:",pp1)
            else:
                print("Better Luck Next Time! Word=",picked_word)
        else:
            print(p2name,"Your turn")
            ans=input("Answer:")
            if ans==picked_word:
                pp2+=1
                print("Score:",pp2)
            else:
                print("Better Luck Next Time! Word=",picked_word)
        c=int(input("Do you want to continue?(0/1):"))
        if c==0:
            thank(p1name,p2name,pp1,pp2)
            break
        turn=turn+1


play()
