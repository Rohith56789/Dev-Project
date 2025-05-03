read -p "enter your age:" age
read -p "are you a citizen? (yes/no): " citizen

if [ "$age" -ge 18 ] && ["$citizen" = "yes"]; then 
    echo "you are eligible to vote"
elif ["$age" -lt 18 ]; then
    echo " you are underage and not eligible to vote"
else 
    echo "you must be a ciziten to vote"
fi 
