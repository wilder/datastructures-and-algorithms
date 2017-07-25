#requiredDrones: 'int' representing how many drones should be returned
#dronesFlightRange: array of 'Drone'
#inMaintenanceDrones: array of 'int' representing the ids of the drones that are in maintenance
def greatestFlightRangeDrones(requiredDrones, drones, inMaintenanceDrones):
    res = []
    #just testing
    #print(requiredDrones, drones[0].id, drones[0].flightRange, inMaintenanceDrones)
    
    #sorting drones
    drones.sort(key = lambda x: x.flightRange, reverse=False)
    
    while len(res) < requiredDrones:
        d = drones.pop()
        #TODO: improve "in"
        if d.id not in inMaintenanceDrones:
            res.append(d.id)
    
      
    return res
