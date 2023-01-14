'''Description
The prerequisite skill means a skill that is required to be learned prior to learning a certain skill.

For example, if the order of the prerequisite skill is Spark → Lightning bolt → Thunder, 
the Lightning bolt should be learned prior to learning Thunder, and Spark should be learned prior to learning Lightning bolt.

Other skills not listed in the above order (such as Healing) can be learned regardless of order. 
Therefore, skill tree such as Spark → Healing → Lightning bolt → Thunder is possible, but Lightning bolt → Spark → Healing → Thunder is impossible.

Given the order of prerequisite skill skill and an array skill_trees1 containing skill trees created by users are given as parameters, 
write a function solution to return the number of available skill trees.

Constraints
Skill is represented as the upper-case alphabet, and all strings consist of the upper-case alphabet only.
Order of skill and skill trees are represented as a string.
For example, C → B → D is presented by "CBD".
Length of skill, the order of prerequisite skill, is between 1 and 26, and there are no duplicated skills.
skill_trees is an array whose length is between 1 and 20.
Each element of skill_trees is a string of length between 2 and 26, and there are no duplicated skills.
Examples
skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
"BACDE": C skill should be learned prior to learning B skill. Hence this skill tree is impossible.
"CBADF": This is an available skill tree.
"AECB": This is an available skill tree.
"BDA": C skill should be learned prior to learning B skill. Hence this skill tree is impossible.
'''
def is_passed(skill, skill_tree):
    before = -1
    for s in skill:
        current = -1
        for i, st in enumerate(skill_tree):
            if s == st:
               current = i
               break
        
        if before == -1 and current == -1:
            return False
        
        if before < current:
            before = current
            
        if current != -1 and before > current:
            return False
        
        
               
        
    return True

def solution(skill:str, skill_trees):
    answer = -1
    for i, skill_tree in enumerate(skill_trees):
        if is_passed(skill, skill_tree):
            return i+1
    return answer



print(solution('CBD',["BACDE", "AECB", "BDA"]))
# print(solution('CBD',["CBADF"]))