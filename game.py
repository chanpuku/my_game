def main():
    import taku
    import basic

    #卓の設定
    numOfPeople=3
    numOfAkadora=4
    numOfSet=3
    numOfTonpu=1
    mochiten=35000

    janshi=[basic.nomal_agent(mochiten) for i in range(numOfPeople)]

    taku=taku.taku(numOfPeople,numOfAkadora,janshi,numOfTonpu=numOfTonpu,mochiten=mochiten,numOfSet=numOfSet,torikiri=True,saifu=True)

    while not taku.state=='finished':
        taku.controll()
main()		