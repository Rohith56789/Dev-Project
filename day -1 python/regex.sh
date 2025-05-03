#!/bin/bash

read -p "Enter an email address: " email

# Regular expression for validating an email address
regex="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if [[ $email =~ $regex ]]; then
    echo "Valid email address."
else
    echo "Invalid email address."
fi

String="My Number is 1234567890"
#check if the string contaains a number
if [[ $String =~ [0-9]{8} ]]; then
    echo "String contains a number"
else
    echo "String does not contain a number"
fi