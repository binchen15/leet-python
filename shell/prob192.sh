# Read from the file words.txt and output the word frequency list to stdout.

declare -A arr

while IFS= read -r line
do
    for word in $line
    do
        if [[ ! ${arr[$word]} ]]
        then
            arr[$word]=1
        else
            arr[$word]=$((${arr[$word]} + 1))
        fi
    done
done < "./words.txt"

for key in "${!arr[@]}"
do 
echo $key ${arr[$key]} 
done | sort -k 2 -r -n
