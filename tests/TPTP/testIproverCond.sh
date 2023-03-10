for FILE in *.tff
do
	if [ -f ${FILE}.iout ]
	then
		echo "$FILE.iout exists."
	else
		/home/apease/workspace/iprover/iproveropt --time_out_real 6000 $FILE &>$FILE.iout &
	fi
done

for FILE in *.tptp
do
	if [ -f ${FILE}.iout ]
	then
		echo "$FILE.iout exists."
	else
		/home/apease/workspace/iprover/iproveropt --time_out_real 6000 $FILE &>$FILE.iout &
	fi
done