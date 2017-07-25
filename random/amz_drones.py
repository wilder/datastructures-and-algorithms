#requiredDrones: 'int' representing how many drones should be returned
#dronesFlightRange: array of 'Drone'
#inMaintenanceDrones: array of 'int' representing the ids of the drones that are in maintenance
def greatestFlightRangeDrones(requiredDrones, drones, inMaintenanceDrones):
    res = []
    from collections import defaultdict
    d = defaultdict(int)
    
    for i in drones:
        d[i.id] = i
        
    for i in inMaintenanceDrones:
        d[i] = Drone(i, 0)
        
    drones = list(d.values())

    drones.sort(key = lambda x: x.flightRange, reverse=False)
    
    while len(res) < requiredDrones:
        d = drones.pop()
        res.append(d.id)
    
      
    return res

