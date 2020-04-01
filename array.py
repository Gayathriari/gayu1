arr = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
fr = [None] * len(arr);    
visited = -1;
for i in range(0, len(arr)):    
    count = 1;    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            count = count + 1;    
              
            fr[j] = visited;    
                
    if(fr[i] != visited):    
        fr[i] = count;
           
print(" Element - Frequency");    
for i in range(0, len(fr)):    
    if(fr[i] != visited):    
        print("    " + str(arr[i]) + "    -    " + str(fr[i]));
