firstName="con"
lastName="cat"
#string concatentaion
echo "welcome $firstName $lastName"
#arithmetic operations
num1=10
num2=3
sum="$(($num1+$num2))"
echo "Result: $sum"
echo "Result: $(($num1-$num2))"
#take input from user
read -p "enter Ur Name: " user_name
echo "Hello, $user_name" 