def Anagrams(s1,s2):
    s1=s1.replace('','').lower()
    s2=s2.replace('','').lower()
    if len(s1)!=len(s2):
        return 'Word is not anagrams'
    if sorted(s1) == sorted(s2):
        return 'Anagrams'
    else:
        return 'Word is not anagrams'
