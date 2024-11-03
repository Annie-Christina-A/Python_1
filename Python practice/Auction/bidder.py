import os
def won(bid_pep):
    max=0
    for i in bid_pep:
        if(bid_pep[i]>max):
            max=bid_pep[i]
    print(f"the one who bid {max} is the winner")


des={}
end_of_bidding = False
while not end_of_bidding:
    name=input("enter yor name: ")
    bid=int(input("your bid: "))
    des[name]=bid
    bidders=input("Are any other bidders? : Type 'yes' or 'no' ").lower()
    if(bidders=='yes'):
        os.system('cls')
    else:
        end_of_bidding=True
        won(des)
        
