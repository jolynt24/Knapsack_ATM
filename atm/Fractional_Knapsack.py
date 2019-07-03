class atm:
    def calculate_Amount(denominations,note_Count,requested_amount):
        ratio=[denominations[i]*note_Count[i] for i in range(len(denominations))]
        conv=sorted(list(zip(ratio,denominations,note_Count)),reverse=True)
        amount,remaining_amount=0,requested_amount
        for r,d,n in conv:
            if requested_amount==0: break
            if r<=remaining_amount:
                amount+=r
                remaining_amount-=r
            elif r>remaining_amount:
                amount=remaining_amount
                remaining_amount=0
                break
        return amount
    
    def dispense(denominations,note_count,amount): 
        disp={}
        currency=list(zip(denominations,note_count))
        currency.sort(reverse=True)
        for d,n in currency:
            if amount>0:
                if d>amount:continue
                count=int(amount/d)
                if n-count<0:
                    disp[d]=n
                    amount=amount-d*n
                else:
                    disp[d]=count
                    amount=amount-d*count
            else:break
        return disp