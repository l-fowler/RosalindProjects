
def rabbitPairs(numMonths, numOffspring):
    """
    :param numMonths: the number of months that rabbits will be reproducing. Note that rabbits may not reproduce until
    at least 1 month old - where numMonths < 2, there will only be one pair of rabbits.
    :param numOffspring: the number of offspring produced by adult rabbit pairs (adult meaning older than 1 month)
    :return: the number of offspring produced by adult rabbits + number of adult rabbits in the population = total pop.
    """
    if numMonths < 2:
        return numMonths
    else:
        return rabbitPairs(numMonths - 1, numOffspring) + (rabbitPairs((numMonths - 2), numOffspring)) * numOffspring
        # use Fibonacci sequence Fn = Fn-1 + Fn-2

numMonths = int(input("Enter the number of months: "))
numOffspring = int(input("Enter the number of offspring: "))

print(rabbitPairs(numMonths, numOffspring))
