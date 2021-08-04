# Solution for the problem "Electronics Shop"
# https://www.hackerrank.com/challenges/electronics-shop/problem

#  Cash in hand, number of keyboard brands and number of usb brands
cash, numKeyboards, numUSB = map(int, input().strip().split(' '))

# List of keyboard prices
keyPrices = list(map(int, input().strip().split(' ')))
# List of USB prices
usbPrices = list(map(int, input().strip().split(' ')))

# -1 denotes that the money cannot be spent. We start here and then verify whether
# there is any possible combination of keyboard and usb within the budget
moneyToSpend = -1

# loop over keyboard prices
for keyPrice in keyPrices:
    # loop over usb prices
    for usbPrice in usbPrices:
        # Sum of the current keyboard and usb
        sumPrice = keyPrice + usbPrice

        # If the current combination of keyboard and usb costs more than the existing
        # seletion and it is within the available cash budget, we update the cost
        if sumPrice > moneyToSpend and sumPrice <= cash:
            moneyToSpend = sumPrice

print(moneyToSpend)