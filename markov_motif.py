import pandas as pd

colnames=['FoldID', 'EventID', 'start_index','seq', 'Bound'] 
df = pd.read_csv('Data/markov_files/motif.txt', delimiter = '\t',  names = colnames, header=None)
df1=df['seq']
df1.reset_index(drop=True,inplace=True)

def combinations_list():

    """
    returns list of combinations of ACGT of all lengths possible 
    """
    letters = ['0','A', 'C', 'G', 'T']
    max_length = 3
    b = len(letters) - 1
    #  base to convert to
    n = 0
    k = 0
    while (k < max_length) :
        n = (n * b) + b    
        k += 1
    #  number of combinations
    i = 1
    l=[]
    while (i <= n) :
        current = i
        #  m and q_n in the formula
        combination = ""
        while True :
            remainder = current % b
            if (remainder == 0) :
                combination += letters[b]
                current = int(current / b) - 1
            else :
                combination += letters[remainder]
                current = int(current / b)
            if((current > 0) == False) :
                break
        l.append(combination)
        i += 1
    return l


def markov_model_motif(): 
    """
    for a second degree motif markov model 
    returns dict2, dict3: count of the appearance of eg: A->C and eg: AC->T occuring
    """
    dict2 = {} 
    dict3 = {}
    l = combinations_list()
    for ele in l: 
        if len(ele)==2:
            dict2[ele]=0
        elif len(ele)==3:
            dict3[ele]=0

    for j in range(0,len(df1),2):
        seq=df1[j]
        #print(seq)
        print(" ")
        print(seq)

    for k in range(0,len(seq)-2):
        if (seq[k:k+2] in dict2.keys()):
            dict2[seq[k:k+2]]+=1
    #print(dict2)

    for i in range(0,len(seq)):
        if (seq[i:i+3] in dict3.keys()):
            dict3[seq[i:i+3]]+=1
    #print(dict3)
    #print(" ")

    for i1 in dict3:
        if (i1[0:2] in dict2):
            if dict2[i1[0:2]]!=0:
                dict3[i1] = dict3[i1]/dict2[i1[0:2]]

    return dict2, dict3

def motif_score():
    """
    returns the score of th markov model motif 
    """
    s = 'AAGTAACT' 
    import math
    score=1
    for i in range(0,len(s)):
        if (s[i:i+3] in dict3):
            score=score*dict3[s[i:i+3]]
    return (math.log(score))


dict2, dict3 = markov_model_motif()
score = motif_score()
print(dict2)
print(dict3)
print(score)