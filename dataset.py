import random  
import string  
import numpy as np 

def get_num(a, b, x):
    """
    gets a unique number between a range (a,b), divisible by x 
    input:  a - start inde
            b - end index
            x = random number should be divisible by x 

    return: 
        random number divisible by x
    """
    if not a % x:
        return random.choice(range(a, b, x))
    else:
        return random.choice(range(a + x - (a%x), b, x))

def non_motif_string():  
    """
   generates a string of length (by get_num) of ACGT 
   returns: string of equal ACGT 
    """
    length = get_num(200,500,4)   
    #print("random length: " , length)
    len4 = length/4
    #print("len / 4 :" , len4)
    letters = ['A','C','G','T'] 
    letters_list = list(np.repeat(letters,len4))
    random.shuffle(letters_list)
    #print(" Random generated string with repetition:")
    str1 = "" 
    return (str1.join(letters_list))

def add_motif(motif):
    """
    adds a motif - string input, to output by non_motif_string
    returns: string consisting of a motif 
    """
    #motif = 'ATCAAG'
    result = list(non_motif_string())
    #print(''.join(result))
    i = random.choice(range(len(result)))
    #print(i)
    result.insert(i, motif)
    result = ''.join(result)
    return result
    
def write_to_file(length,add_motif_option): 
    """
    generate dataset 
    input: 
            length: number of rows 
            add_motif_option = True/False
    returns:  a .txt file

    """
    l=[]
    name = ''
    for i in range(int(length)):
        
        if(add_motif_option==True):
            name = "motif"
            result = add_motif('ATCAAG')
        else:
            name = "non_motif"
            result = non_motif_string()
        seq = ">seq" + str(i+1)
        l.append(seq)
        l.append(result)

    with open(name + ".txt", "w") as f:
        for s in l:
            f.write(str(s) +"\n")
        
write_to_file(1000,add_motif_option=False)
    
