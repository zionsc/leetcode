class Solution:
  def wonderfulSubstrings(self, word: str) -> int:
    res=0
    mask=0
    count=[0]*1024
    count[0]=1

    for c in word:
        mask^=1<<ord(c)-ord('a')
        res+=count[mask]
        res+=sum(count[mask^1<<i] for i in range(10))
        count[mask]+=1

    return res