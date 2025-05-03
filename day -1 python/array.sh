#array Declaration
names=("John" "Doe" "Jane" "Smith")

#Accessing array elements
echo "First element: ${names[0]}" #first element
echo "Second element: ${names[3]}" #third element
echo "All elements: ${names[@]}" #all elements

echo "Number of elements: ${#names[@]}" #number of elements
#Adding elements to an array

names+=("Alice")
 
 #accessing all element
echo "All elements after adding Alice: ${names[@]}" #all elements

#Removing elements from an array
unset names[1] #remove second element
echo "All elements after removing second element: ${names[@]}" #all elements

#change array elemets
names[1]="Bob" #change second element
echo "chnaged ele:${names[1]}" #changed element


echo "All elements after changing second element: ${names[@]}" #all elements

for name in "${names[@]}"; do
    echo "Name: $name"
done
 ##iterate and store all values in one variable and print
all_names=""
for name in "${names[@]}"; do
    all_names+="$name "
done
echo "All names: $all_names"