class GIZ(object):
   def findpal(self, s):
      hd = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         hd[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  hd[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and hd[i+1][end-2]:
                  hd[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]
ob1 = GIZ()
print(ob1.findpal("babad"))