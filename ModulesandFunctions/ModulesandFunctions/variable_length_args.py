def printDetails(item,*components):
    print('Components of %s are'% (item))
    for component in components:
        print("-",component)
    return
printDetails('computer','CPU','Monitor','Motherboard','Mouse')