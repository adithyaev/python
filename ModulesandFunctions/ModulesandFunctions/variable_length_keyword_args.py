def printDetails(item, **kwargs):
    print('Item name is %s'% (item))
    for key,value in kwargs.items():
        print('- %s is %s' % (key,value))
        
printDetails("Monitor",price=70,Quantity=85)