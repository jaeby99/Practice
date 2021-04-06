import re

def solution(new_id):
    characters="abcdefghijklmnopqrstuvwxyz0123456789-_."
    
    """1단계"""
    new_id=new_id.lower()
    
    """2단계"""
    for x in new_id:
        if x not in characters: 
            new_id=new_id.replace(x,"")
            
    """3단계"""
    new_id=re.sub("[.]+",".",new_id)
    
    """4단계"""
    if new_id.startswith('.'): new_id=new_id[1:]
    if new_id.endswith('.'): new_id=new_id[:-1]
        
    """5단계"""
    if len(new_id)==0: new_id="a"
        
    """6단계"""
    if len(new_id)>15:
        new_id=new_id[:15]
        while new_id.endswith('.'):new_id=new_id[:-1]
            
    """7단계"""
    if len(new_id)<3:
        while len(new_id)!=3:
            new_id+=new_id[-1]
        
    return new_id