import sys


# Function to generate the product of all elements in a given set
# and update maximum product found so far
def findMaxProduct(set, maximum):

    product = 1

    for j in set:
        product = product * j

    # if the set is not empty, then update the product
    if set:
        maximum = max(maximum, product)

    return maximum


# Function to generate a power set of a given set `S`
def findPowerSet(S, s, n, maximum):

    # if we have considered all elements, we have generated a subset
    if n == 0:
        # compute its product of elements and update the maximum product found so far
        return findMaxProduct(s, maximum)

    # consider the n'th element
    s.append(S[n - 1])
    maximum = findPowerSet(S, s, n - 1, maximum)

    s.pop(len(s) - 1)  # backtrack

    # or don't consider the n'th element
    return findPowerSet(S, s, n - 1, maximum)


if __name__ == "__main__":

    S = [-6, 4, -5, 8, -10, 0, 8]
    n = len(S)

    s = []
    maximum = findPowerSet(S, s, n, -sys.maxsize)

    print("The maximum product of a subset is", maximum)
