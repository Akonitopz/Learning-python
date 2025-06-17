#Slice list into 3 equal chunks and reverse each chunk

def sliceandReverse(l1):
  print(f"Slice 1: {l1[0:3]}")
  print(f"Reverse: {l1[2::-1]}")
  print(f"Slice 2: {l1[3:6]}")
  print(f"Reverse: {l1[5:2:-1]}")
  print(f"Slice 3: {l1[6:9]}")
  print(f"Reverse: {l1[9:5:-1]}")

sliceandReverse([11, 45, 8, 23, 14, 12, 78, 45, 89])