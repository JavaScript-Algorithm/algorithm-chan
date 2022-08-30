import re

def solution(skill, skill_trees):
    regex = '[^' + skill + ']'
    newTree = map(lambda x: re.sub(regex, '', x), skill_trees)
    
    count = 0
    for tree in newTree:
        if tree == skill[:len(tree)]: 
            count += 1
    return count