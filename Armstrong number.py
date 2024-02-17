Num=int (input("Enter the Value"))
makestrng=str(Num)
findlen=len(makestrng)

power=[]
for digitchar in makestrng:
  makeint=int(digitchar)
  powers=makeint**findlen
  power.append(powers)
  total=sum(power)
if total==Num:
  print("Aramstrong Number")
else:
  print("Not Aramstrong Number")  