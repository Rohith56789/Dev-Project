for file in $(ls); do
  if [ -f "$file" ]; then
    echo "File: $file"
  elif [ -d "$file" ]; then
    echo "Directory: $file"
  fi
done

#for cat files
for data in $(cat emails.txt); do
  echo "$data"
done