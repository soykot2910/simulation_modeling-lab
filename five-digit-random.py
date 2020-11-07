import random
import math
from tabulate import tabulate

def poker_test():
    obserd_ferq=[]
    random_num=int(input('Enter total five digit random number:'))
    five_dift=int(input('Enter total five different digit: '))
    paris=int(input('Enter total number having pair:'))
    two_pair=int(input('Enter total number having two pairs:'))
    three_kind=int(input('Enter total number having three of kind:'))
    full_house=int(input('Enter total number full of house:'))
    four_kind=int(input('Enter total number four of kind:'))
    five_kind=int(input('Enter total number five of kind:'))

    obserd_ferq.append(five_dift)
    obserd_ferq.append(paris)
    obserd_ferq.append(two_pair)
    obserd_ferq.append(three_kind)
    obserd_ferq.append(full_house)
    obserd_ferq.append(four_kind)
    obserd_ferq.append(five_kind)

    d_alpha=16.812


    cal_five_dift=(10/10)*(9/10)*(8/10)*(7/10)*(6/10)*(math.factorial(5)/math.factorial(5))
    cal_pairs=(10/10)*(1/10)*(9/10)*(8/10)*(7/10)*(math.factorial(5)/(math.factorial(2)*math.factorial(3)))
    cal_two_pair=(10/10)*(1/10)*(1/10)*(9/10)*(8/10)*(math.factorial(5)/(math.factorial(2)*2))*(1/2)
    cal_three_kind=(10/10)*(1/10)*(1/10)*(9/10)*(8/10)*(math.factorial(5)/(math.factorial(3)*math.factorial(2)))
    cal_full_house=(10/10)*(1/10)*(1/10)*(1/10)*(9/10)*(math.factorial(5)/(math.factorial(3)*math.factorial(2)))
    cal_four_kind=(10/10)*(1/10)*(1/10)*(1/10)*(9/10)*(math.factorial(5)/math.factorial(4))
    cal_five_kind=(10/10)*(1/10)*(1/10)*(1/10)*(1/10)*(math.factorial(5)/(math.factorial(5)*math.factorial(0)))

    exp_freq=[]
    exp_freq.append(cal_five_dift*random_num)
    exp_freq.append(cal_pairs)
    exp_freq.append(cal_two_pair)
    exp_freq.append(cal_three_kind)
    exp_freq.append(cal_full_house)
    exp_freq.append(cal_four_kind)
    exp_freq.append(cal_five_kind)

    com_dist=["five different","pairs","Two pairs","Three of kind","full house","four of kind","five of kind"]
    #print(cal_five_dift,cal_pairs,cal_two_pair,cal_full_house,cal_four_kind,cal_five_kind)
    data=[]
    total=0
    for i in range(7):
        arr=[]
        arr.append(com_dist[i])
        arr.append(obserd_ferq[i])
        arr.append(exp_freq[i])
        dif=abs(obserd_ferq[i]-exp_freq[i])
        arr.append(dif)
        dif_seq=abs((obserd_ferq[i]-exp_freq[i])**2)
        arr.append(dif_seq)
        divid=abs(((obserd_ferq[i]-exp_freq[i])**2)/exp_freq[i])
        total +=abs(((obserd_ferq[i]-exp_freq[i])**2)/exp_freq[i])

        data.append(arr)

    print(tabulate(data,headers=["Combination","Ob-Frq","Exp-frq","(Oi-Ei)","(Oi-Ei)^2","((Oi-Ei)^2)/Ei"]))

    print("\n\n")
    print("Here alpha value is 0.01 ")
    if d_alpha<total:
        print("the given random number are independ")
    else:
        print("The given random number are not independ")
poker_test()


