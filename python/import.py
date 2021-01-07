var1 = 20
var2 = 30
var3 = 40
 
res1 = (not (var1 > 30))
res2 = not var2 > -30
res3 = ((var3 == 50 or var2 > 10) and var1 < 90)
 
resultado = ( (res1 != res2) and ( var1 > res2 + res1) )

print(resultado)