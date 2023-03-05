for FILE in *.tff.vout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Timeout' $FILE ; then
                echo -e "\tTimeout"
        else
                grep Success $FILE
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
                grep Success $FILE
        fi
done
          
