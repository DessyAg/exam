def  nbYear(p0,p,percent,aug)  :
  
   percent = int(percent) / int(100)
   number= int(p0)+ int(p) *int(percent) +int(aug)
   return number

print(nbYear(1000,1000,2,50))

   