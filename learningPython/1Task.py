appartment = int(input("Write the number of the appartment"))

floar = 1 
pod = 1
temp = appartment
if appartment <= 0:
   print("norm appartment napishi")
while(appartment > 0):
   if appartment <= 20:
      while(appartment > 0):
         appartment = appartment - 4
         if appartment <= 0:
            print("этаж: " + str(floar))
            break
         floar += 1
      print("подъезд: " , pod)
      break
   appartment = appartment - 20
   pod += 1   

# correct variant of the code above 

appartment_correct = int(input("again"))

entrance = (appartment_correct - 1) // 20 + 1
floar = (appartment_correct - 1) % 20 // 4 + 1
print(floar)
print(entrance)