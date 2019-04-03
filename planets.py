def weight_on_planets():
   w = int(input('What do you weigh on earth? '))

   wmars =  str(0.38 * w)
   wjup =  str(2.34 * w)

   print('\nOn Mars you would weigh '+wmars+' pounds.\nOn Jupiter you would weigh '+wjup+' pounds.')

   
   
   
if __name__ == '__main__':
   weight_on_planets()