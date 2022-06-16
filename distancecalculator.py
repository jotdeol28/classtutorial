#user will input the unit to convert
userinput =(input("Kilometers or Miles: "))

#if userinput is miles
if userinput=="miles":


#convert miles into kilometers
    Miles = float(input("Enter distance in miles: "))
 
#conversion formula
    conv_fac = 1.60934
 
#km calculator
    Kilometers = miles * conv_fac
    
#print the results
    print('%0.3f miles is equal to %0.3f Kilometers' %(Miles,Kilometers))

#if the input is not miles then kilometers calculator
else:
    #convert kilometers into miles
    Kilometers = float(input("Enter distance in kilometers: "))
 
#conversion formula
    conv_fac = 0.621371
 
#calculate miles
    Miles = Kilometers * conv_fac
    
#print the result
print('%0.3f kilometers is equal to %0.3f miles' %(Kilometers,Miles))
