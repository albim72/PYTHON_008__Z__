liczby = (900,1001,-787,0,57,-7,56,5,4,12,44,578,867,-99,-134,0,9,343,-347,-990,1245)

def statystyki(dane)->tuple:
    minimum:int = min(dane)
    maximum:int = max(dane)
    rozstep:int = maximum - minimum
    sr_arytm:float = sum(dane)/len(dane)
    return minimum,maximum,rozstep,sr_arytm


wynik = statystyki(liczby)
print(type(wynik))
print(wynik)

mini,maxi,roz,srsrtm = statystyki(liczby)
print(f'wartośc maxymalna: {maxi}, wartośc minimalna: {mini}, rozstęp: {roz}, średnia arytmetyczna: {srsrtm}')
