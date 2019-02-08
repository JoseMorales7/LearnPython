def scan(s):
    ##has to enter a string and theres number so i assume that have to going to use exception here
    directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
    verbs = ('go', 'stop', 'kill', 'eat')
    stop = ('the', 'in', 'of', 'from', 'at', 'it')
    nouns = ('door', 'bear', 'princess', 'cabinet', 'honey')
    words = s.split()
    tuples = []
    for x in words:
        if x in directions:
            tuples.append(('direction', x))
            
        elif x in verbs:
            tuples.append(('verb', x))
            
        elif x in stop:
            tuples.append(('stop', x))
            
        elif x in nouns:
            tuples.append(('noun', x))
            
        elif isNumber(x) != None:
            tuples.append(('number', int(x)))
            
        else:
            tuples.append(('error', x))
    
    return tuples
    
def isNumber(n):
    try:
        return int(n)
    
    except ValueError:
        return None
