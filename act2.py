Amount =int(input("Please Enter Amount for Withdraw :"))

note1 = Amount%10
note2 = (Amount%100)%10
note3 = ((Amount%100)  %50) %10

print( "notes of 100 squares" , note1)
print( "notes of 50 squares" , note2)
print( "notes of 10 squares" , note3)
