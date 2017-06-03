
def make_word_count(filename):
    file=(open(filename,"r"))
    lines=file.readlines()
    #sortedline=lines.sorted(counter,key=len)
    counter=dict()
    #counter=sorted(counter)
    #for word in sortedline():
    for word in lines:
       # print lines 
        var1=word.lower().split()
                 
        for item in var1:
            if item in counter:
               counter[item]+=1
                  
            else:
               counter[item]=1
            
 #   print(counter)
    return counter
    
  


def make_length_wordcount(filename):
    file=open(filename,"r")
    lines=file.readlines()
    counter=dict()
    for word in lines:
       # print lines 
        var1=word.lower().split()
        
        for item in var1:
            items=len(item) 
            if items in counter:
                      
               counter[items]+=1
            else:
               counter[items]=1
            

    return counter
    
   


def analyze_text(filename):
    a=make_length_wordcount(filename)
    b=make_word_count(filename)
    sdict=sorted(b)
    #print sdict
    #file=open("assign.txt","r")
    newfile=open(filename.split('.')[0] + "_analyzed_SANDEEP_RAMESH.txt","w")
    #make_length_wordcount(file)
    for i in a:
        
        newfile.write('words of length {} : {}'.format(i,a[i])+'\n')

    #make_word_count(file)
    for i in sdict:
        newfile.write('{} : {}'.format(i,b.get(i))+'\n')
   
    newfile.close()

analyze_text('nasdaq.txt')
analyze_text("raven.txt")
analyze_text("frankenstein.txt")