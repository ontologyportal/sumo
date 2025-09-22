for FILE in *.tff
do
      /home/apease/workspace/vampire/vampire --mode casc --cores 6 $FILE &> $FILE.vout 
done

for FILE in *.tptp
do
      /home/apease/workspace/vampire/vampire --mode casc --cores 6  $FILE &> $FILE.vout
done
          
for FILE in *.thf
do
      /home/apease/workspace/vampire/vampire-ho --mode casc --cores 6  $FILE &> $FILE.vout
done          
