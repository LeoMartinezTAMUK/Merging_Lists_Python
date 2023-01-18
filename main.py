""" Created by: Leo Martinez III, Spring 2022 """

S1 = [3, 9, 14, 18]
S2 = [2, 5, 6, 15, 56]
S = []

S = S1 + S2
def merge(S1, S2, S):
  # Merge S1 and S2 into properly sized list S
  i = j = 0
  while i+j < len(S):
    if j == len(S2) or (i<len(S1) and S1[i]<S2[j]):
      S[i+j] = S1[i]
      i = i+1
    else:
      S[i+j] = S2[j]
      j = j+1
  
merge(S1, S2, S)
print(S)
