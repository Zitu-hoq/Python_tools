def buy():
    print("\n\033[92m--------------------------------\033[0;42mBuying Calculator\033[0;92m-----------------------------\033[0m")
    bPrice = float(input("\nBuying Price($): "))
    bAmount = float(input("Buying Amount($): "))
    bFee = float(bAmount / 1000)
    Amount = float(bAmount - bFee)
    Token = float(Amount / bPrice)
    print("\n\t\033[45mNumber of Token: ", Token, "\033[0m\n")
    print("\033[92m------------------------------------------------------------------------------\033[0m")

def sell():
    print("\n\033[92m--------------------------------\033[0;42mSelling Calculator\033[0;92m-----------------------------\033[0m")
    sPrice = float(input("\nToken Price($): "))
    sToken = float(input("Number of Token: "))
    sAmount = float(sPrice * sToken)
    sFee = float(sAmount / 1000)
    Amount = float(sAmount - sFee)
    Amount = "%.3f" %Amount
    print("\n\t\033[45mSelling Amount: ", Amount, "$\033[0m\n")
    print("\033[92m-------------------------------------------------------------------------------\033[0m")


def calculate(price, token,bamount):
    print("Calculate Profit using: \t1.Selling Price \t2.Profit Amount")
    pOption = int(input("Enter your Option: "))
    isPrice=False
    isProfit=False
    if(pOption ==2): isProfit=True
    if(pOption==1): isPrice=True
    print("\033[41mEnter 0 in selling Price/profit amount to Exit\033[0m")
    print("\n\t\t\t\033[44mBuying Price: ", price, "$\033[0m")
    while(isPrice):
        sPrice = float(input("\nSelling Price($): "))
        if(sPrice==float(0)):
            isPrice=False
        sAmount = sPrice * token
        sFee = sAmount / 1000
        Amount = sAmount - sFee
        print("\033[35mSelling Amount: ", Amount, "$\033[0m")
        Change = (sPrice-price)*100/price
        Change = round(Change, 2)
        print("Price Change: \033[1;31m", Change, "\033[0m%")
        Profit = Amount - bamount
        Profit = '%.2f' %Profit
        print("\n\t\033[1;45m Profit: ", Profit, "$\033[0m\n")

    while(isProfit):
        profit= float(input("How much Profit you want: \t"))
        if(profit==float(0)):
            isProfit=False
        aSAmount = bamount + profit
        sAmount= (aSAmount * 1000)/999
        sPrice = sAmount/token
        Change = (sPrice-price)*100/price
        Change = round(Change, 2)
        print("Price Change: \033[1;31m", Change, "\033[0m%")
        print("\n\t\033[1;45m Selling Price: ", sPrice, "$\033[0m\n")
    
    print("Going back to the Main Menu\nLoding.........................")
    print("\033[32m[+]\033[0m", end='')
    return "sucessful"





def buySell():
    print("\n\033[92m--------------------------------\033[0;42mProfit Calculator\033[0;92m-----------------------------\033[0m")
    bPrice = float(input("\nBuying Price($): "))
    bAmount = float(input("Buying Amount($): "))
    bFee = bAmount / 1000
    Amount = bAmount - bFee
    Token = Amount / bPrice
    print("\033[35mNumber of Token: ", Token, "\033[0m")
    sPrice = float(input("\nSelling Price($): "))
    sAmount = sPrice * Token
    sFee = sAmount / 1000
    Amount = sAmount - sFee
    print("\033[35mSelling Amount: ", Amount, "$\033[0m")
    Change = (sPrice-bPrice)*100/bPrice
    Change = round(Change, 2)
    print("Price Change: \033[1;31m", Change, "\033[0m%")
    Profit = Amount - bAmount
    Profit = '%.2f' %Profit
    print("\n\t\033[1;45m Profit: ", Profit, "$\033[0m\n")
    cMore= int(input("\nFor more different selling scenario \033[43mEnter 1: \033[0m"))
    if(cMore==1):   
        x=calculate(bPrice,Token,bAmount)
        print(x)
    print("\033[92m------------------------------------------------------------------------------\033[0m")


print("\033[42m-------------------------Welcome To Crypto Calculator------------------------\033[0m")
while(1):
    print("\n1.Buy \t2.Sell \t3.Buy/Sell \t4.Exit")
    option = int(input("\033[92m[+] \033[0mEnter Your Option:\t"))
    if (option == 1):    buy()
    elif (option == 2):   sell()
    elif (option == 3):   buySell()
    else: break



