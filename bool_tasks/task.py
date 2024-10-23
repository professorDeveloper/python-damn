balance = int(input("Balance:"))  # 50
distance = int(input("Distance:"))  # 20
carKmPrice = int(input("CarKmPrice:"))  # 5
busKmPrice = int(input("BusKmPrice:"))  # 1

isEnoughBalanceForCar = distance * carKmPrice <= balance  # Agar  car false bo`lsa   bus true  agar bus true bo`lsa car false
isEnoughBalanceForBus = distance * busKmPrice <= balance

checkResult = (
        isEnoughBalanceForCar | isEnoughBalanceForBus)
## Agar Car =true  bus =false = true , car =false bus =true  = true   car =false bus =false false
print(checkResult)
