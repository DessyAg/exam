def nbYear(p0,percent,aug,p):
   nilai = 0
   while p0 < p :
      p0 = p0 + p0 * (percent/100) +aug
      nilai += 1
   return nilai 

print(nbYear(1500,5,100,5000))