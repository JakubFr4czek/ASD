def radix_sort_MSD_for_strings (array, i):

    # base case (list must already be sorted)
    if len(array) <= 1:
        return array

    # divide (first by length, then by order of the first character)
    done_bucket = []
    buckets = [ [] for x in range(64,100) ] # ASCII TABLE A-Z is from 64 to 90

    for s in array:
        if i >= len(s):
            done_bucket.append(s)
        else:
            buckets[ ord(s[i]) - ord('a') ].append(s)

    # ***********conquer (recursively sort buckets)***********
    buckets = [ radix_sort_MSD_for_strings (b, i + 1) for b in buckets ]
    return done_bucket + [ b for blist in buckets for b in blist ]
def main():
    array_of_strings = ['VEYSEL','EGE','YASIN', 'SELIN']       # ASCII TABLE A-Z is from 64 to 90 if you want to    #change it  to lowercase letter Also change the bucket list's range                
                                                         
    print('before radix_sort:')
    print (array_of_strings)
    array_of_strings = radix_sort_MSD_for_strings (array_of_strings, 0)
    print('after radix_sort')
    print (array_of_strings)
main()
