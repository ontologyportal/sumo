for FILE in *.tff.vout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Timeout' $FILE ; then
                echo -e "\tTimeout"
        else
                sed -nr "s/.*Success in time ([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        fi
done

for FILE in *.tptp.vout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Timeout' $FILE ; then
                echo -e "\tTimeout"
        else
                sed -nr "s/.*Success in time ([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        fi
done
          
