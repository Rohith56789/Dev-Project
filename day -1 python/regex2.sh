#!/bin/bash

# Regex for phone number (e.g., (123) 456-7890 or 123-456-7890)
phone_regex="^(\([7-9]{3}\)\s?|[0-9]{3}-)[0-9]{3}-[0-9]{4}$"

read -p "Enter a phone number: " phone_number

if [[ $phone_number =~ $phone_regex ]]; then
    echo "Valid phone number."
else
    echo "Invalid phone number."
fi