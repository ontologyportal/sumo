for FILE in *.tff 
do 
	if [ -f ${FILE}.vout ] 
	then 
		echo "$FILE.vout exists."
	else
		/home/apease/workspace/vampire/vampire --avatar off --mode casc --proof tptp -t 600 $FILE &>$FILE.vout &
	fi
done
