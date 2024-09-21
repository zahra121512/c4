print("Enter marks obtained in 4 subjects: ")
math = int(input("Maths :"))
english = int(input("English :"))
science = int(input("Science :"))
hindi = int(input("Hindi :"))

sum = math+english+science+hindi
print("sum of math,elnglish,science and hindi:")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)