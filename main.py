# A program to sort my topsters albums

import math
import random

class album:
    def __init__(self, artist, name, rating):
        self.artist = artist
        self.name = name
        self.rating = rating
    def __str__(self):
        return self.name + " - " + self.artist

# create dict too??
albumDict = {}

def create_list():
    albumlist = []
    with open('topsters.txt', 'r') as r:
        artist = ""
        title = ""
        index = 0
        for line in r:
            if line.strip():
                # Get the rating
                index = line.find(' - ')
                rating = float(line[0:index])
                substr = line[index+3:]
                
                # Get the artist and title
                index = substr.find(' - ')
                artist = substr[0:index]
                title = substr[index+3:-1]

                newAlbum = album(artist, title, rating)
                albumlist.append( newAlbum )
                albumDict[newAlbum] = [newAlbum]

    return albumlist

def writeSorted(sortedAlb):
    with open('topsters.txt', 'w') as w:
        for a in sortedAlb:
            w.write(str(a.rating) + " - " + a.__str__() + "\n")

def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def EloRating(albumA, albumB, K, win):
    Pb = Probability(albumA.rating, albumB.rating)
    Pa = Probability(albumB.rating, albumA.rating)


    if( win == 1):
        albumA.rating = albumA.rating + K * (1 - Pa)
        albumB.rating = albumB.rating + K * (0 - Pb)
    
    else:
        albumA.rating = albumA.rating + K * (0 - Pa)
        albumB.rating = albumB.rating + K * (1 - Pb)

def compare(albumA, albumB):
    x = ""
    while(x == ""):
        x = input(albumA.__str__() + " [1] vs. " + albumB.__str__() + " [2] ")

    if(x == "1"):
        print("\t" + albumA.__str__() + " is better")
        EloRating(albumA, albumB, 30, 1)
        return 1
    elif(x == "2"):
        print("\t" + albumB.__str__() + " is better")
        EloRating(albumA, albumB, 30, 0)
        return 2
    else:
        return -1


def nCr(n):
    top = math.factorial(n)
    bottom = math.factorial(2) * math.factorial(n-2)
    return (top/bottom)

def makeSelections(myAlbums):
    count = 0

    print( "combinations: " + str(nCr(len(myAlbums))) + "\n")

    while( count < nCr(len(myAlbums)) ):
        a = myAlbums[random.randrange(0,len(myAlbums))]
        b = myAlbums[random.randrange(0,len(myAlbums))]
        if b in albumDict[a] :
            continue

        x = compare(a, b)
        if x == -1 :
            break
        
        albumDict[a].append( b )
        albumDict[b].append( a )
        count+=1

def main():
    topster = create_list()

    # for a in topster:
    #     print(str(round(a.rating, 6)) + " - " + a.__str__() )

    makeSelections(topster)

    sortedTopster = sorted(topster, key=lambda album: album.rating, reverse=True)

    # for a in sortedAlbums:
    #     print(a.artist + ", " + a.name + ", " + str(round(a.rating, 6)) )

    writeSorted(sortedTopster)
    
main()