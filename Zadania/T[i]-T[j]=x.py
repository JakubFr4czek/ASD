def find(T,x):

    i = 0
    j = 0

    while i < len(T):
        if T[i]-T[j]<x:
            i+=1
        elif T[i]-T[j]>0:
            j+=1
        else:
            return i,j

#odwracanie listy jednokierunkowej
#ciag z brakującymi elementem (wyszukiwanie binarne)
