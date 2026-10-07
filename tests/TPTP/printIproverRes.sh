for FILE in *Sp.tff.iout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Time Out Real' $FILE ; then
                echo -e "\tTimeout"
        elif grep --quiet -E 'total_time' $FILE ; then
                sed -nr "s/.*total_time:.*([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        else
                echo -e "\tTimeout"
        fi
done

for FILE in *Sp.tptp.iout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Time Out Real' $FILE ; then
                echo -e "\tTimeout"
        elif grep --quiet -E 'total_time' $FILE ; then
                sed -nr "s/.*total_time:.*([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        else
                echo -e "\tTimeout"
        fi
done

for FILE in *SMp.tff.iout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Time Out Real' $FILE ; then
                echo -e "\tTimeout"
        elif grep --quiet -E 'total_time' $FILE ; then
                sed -nr "s/.*total_time:.*([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        else
                echo -e "\tTimeout"
        fi
done

for FILE in *SMp.tptp.iout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Time Out Real' $FILE ; then
                echo -e "\tTimeout"
        elif grep --quiet -E 'total_time' $FILE ; then
                sed -nr "s/.*total_time:.*([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        else
                echo -e "\tTimeout"
        fi
done

for FILE in *SMpf.tff.iout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Time Out Real' $FILE ; then
                echo -e "\tTimeout"
        elif grep --quiet -E 'total_time' $FILE ; then
                sed -nr "s/.*total_time:.*([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        else
                echo -e "\tTimeout"
        fi
done

for FILE in *SMpf.tptp.iout
do
        echo -n $FILE
        if grep --quiet -E 'Exception|Contradictory' $FILE ; then
                grep -E 'Exception|Contradictory' $FILE
        elif grep --quiet -E 'Time Out Real' $FILE ; then
                echo -e "\tTimeout"
        elif grep --quiet -E 'total_time' $FILE ; then
                sed -nr "s/.*total_time:.*([0-9]+\.[0-9]+).*/\t\1/p" $FILE
        else
                echo -e "\tTimeout"
        fi
done