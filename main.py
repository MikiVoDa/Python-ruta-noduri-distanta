# avem n noduri care sunt la distante "distance" respective si putem sa aflam
# distanta pe care trebuie sa o parcurgem pentru ruta "route" respectiva

def CalculateDistance(distance, route):

    final = 0
    starting_place = 0
    last_place = 0

    for k in range(len(route)):

        if k == 0:
            for i in range(last_place, route[k]):
                final += distance[i]
            last_place = route[k]

        elif route[k-1] < route[k] and k == len(route)-1:
            for i in range(last_place, route[k]):
                final += distance[i]
            last_place = route[k]
            for i in range(last_place, starting_place, -1):
                final += distance[i-1]

        elif route[k-1] > route[k] and k == len(route)-1:
            for i in range(last_place-1, route[k]-1, -1):
                final += distance[i]
            last_place = route[k]
            for i in range(last_place, starting_place, -1):
                final += distance[i-1]

        elif route[k-1] < route[k] and k != len(route)-1:
            for i in range(last_place, route[k]):
                final += distance[i]
            last_place = route[k]

        elif route[k-1] > route[k] and k != len(route)-1:
            for i in range(last_place-1, route[k]-1, -1):
                final += distance[i]
            last_place = route[k]

    return final



#Driver Code
distance = [75, 89, 90, 21, 30, 49]
route = [1, 5, 3]
print(f"distanta este {CalculateDistance(distance, route)}")
