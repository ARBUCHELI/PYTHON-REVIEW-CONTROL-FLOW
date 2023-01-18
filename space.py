print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  weight = weight * 0.91
  planet = "Venus"
elif planet == 2:
  weight = weight * 0.38
  planet = "Mars"
elif planet == 3:
  weight = weight * 2.34
  planet = "Jupiter"
elif planet == 4:
  weight = weight * 1.06
  planet = "Saturn"
elif planet == 5:
  weight = weight * 0.92
  planet = "Uranus"
elif planet == 6:
  weight = weight * 1.19
  planet = "Neptune"

print("Your planet:", planet)
print("Your weight:", weight)