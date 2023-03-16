#A tab z parami rozne liczby
#tabli c jaest k chaotyczna jesli dla a[i] po posortowaniu znajduje sie na pozycji rozniacej sie od i o najwyzej k

#k chaotyczna na wejsciu, algorytm sortuje ja, k jest na wejsciu
#jak bedziemy uzywac ta liczbe k

#cos z kopcem

#szukam w obrebie k i wybieram najmniejszy i ide dalej O(n*k)

#kopiec min, wrzucam k elementow i biore min element w czasie k
#przesuwamy o jeden, dodaejmy nastepny element w log k i wyciagamy
#i tak jedziemy itd. itp O(nlogk)