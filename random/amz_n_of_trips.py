#tripMaxWeight: 'int' representing the max weight per trip
#packagesWeight: array of 'int' representing the weight of each package

#TODO: dynamic programing
def deliver(tripMaxWeight, packagesWeight, ntrips):
    
    if not packagesWeight:
        return ntrips

    number_of_packages = 0
    current_weight = 0
    
    
    #current_weight < tripMaxWeight is not enough
    while packagesWeight and number_of_packages < 2 and current_weight < tripMaxWeight:
        pkg = packagesWeight.pop()
        """if current_weight+pkg >= tripMaxWeight:
            packagesWeight.append(pkg)
            break"""
        current_weight += pkg
        number_of_packages+=1
    
    return deliver(tripMaxWeight, packagesWeight, ntrips+1)

def minimumNumberOfTrips(tripMaxWeight, packagesWeight):
    if tripMaxWeight == 0:
        return 0
    
    packagesWeight.sort(reverse=True)
    val = deliver(tripMaxWeight, packagesWeight, 0)
    return val

