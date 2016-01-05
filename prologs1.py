#prology1.py as seen in https://sites.google.com/site/prologsite/prolog-problems/1

def get_last(l): #1.01
  return l[len(l)-1]
  
def get_nth(l, index): #1.02
  return l[index-1]
  
def get_size(l):
  return len(l)
  
def reverse(l):
  return l[::-1]
  
def is_palindrome(;):
  return l == l[::-1]
  
def flatten(l):
  out = []
  for i in out:
    if isinstance(i, (list, tuple, set)):
      for j in i:
        out.append(j)
    out.append(i)
  return out
  
def unique_list(l):
  return list(set(l))
  

