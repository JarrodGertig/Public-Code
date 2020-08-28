#Takes in skyline array of 1s (buildings) and 0s (skyline)
def TallestTower(x=[[1]]):      # Uses [[1]] default
    marker=False                # Marker used to exit when first 1 is found
    for row in x:               # In each row:
        for val in row:             # for each value:
            if val==1:                  # if the value is 1
                y=x.index(row)              # find that row value
                marker=True                 # exit loops
            if marker:                  #
                break                   #
        if marker:                  #
            break                   #
    return (len(x)-y)           # return the height
