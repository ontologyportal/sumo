declare -A SUMO
declare -A MILO
declare -A ALL
declare -A TERR
declare -A NONE

print_results() {
        prefix=$(echo $1 | sed -nr "s/([^0-9]+)([0-9]+)([^\.]+)(\..*)/\1/p")
        number=$(echo $1 | sed -nr "s/([^0-9]+)([0-9]+)([^\.]+)(\..*)/\2/p")
        fils=$(echo $1 | sed -nr "s/([^0-9]+)([0-9]+)([^\.]+)(\..*)/\3/p")
        suffix=$(echo $1 | sed -nr "s/([^0-9]+)([0-9]+)([^\.]+)(\..*)/\4/p")


        if grep --quiet -E 'Exception' $1 ; then
                value="Exception"
        elif grep --quiet -E 'Contradictory' $1 ; then
                value="Contradictory"
        elif grep --quiet -E 'Timeout' $1 ; then
                value="Timeout"
        elif grep --quiet -E 'User error' $1 ; then
                value="User error"                
        else
                value=$(sed -nr "s/.*Success in time ([0-9]+\.[0-9]+).*/\1/p" $1)
        fi
        
        if [[ $fils == *"f"* ]] ; then
                ALL["$prefix$number"]=$value
                #echo "full: $prefix$number \t$value"
        elif [[ $fils == *"T"* ]] ; then
                TERR["$prefix$number"]=$value  
                #echo "terrain: $prefix$number \t$value"              
        elif [[ $fils == *"M"* ]] ; then
                MILO["$prefix$number"]=$value 
                #echo "milo: $prefix$number \t$value"
        elif [[ $fils == *"S"* ]] ; then
                SUMO["$prefix$number"]=$value    
                #echo "sumo: $prefix$number \t$value"                                 
        else 
                NONE["$prefix$number"]=$value    
                #echo "sumo: $prefix$number \t$value"   
        fi
}

for FILE in results/*.tff.vout
do
        print_results $FILE
done

for FILE in results/*.tptp.vout
do
        print_results $FILE
done
          
for FILE in results/*.thf.vout
do
        print_results $FILE
done       

keys=( $(printf "%s\n" "${!SUMO[@]}" | sort) )

echo -e "Problem\t SUMO\t MILO\t Terrain\t All"

for key in ${keys[@]}
do
        echo -e "$key \t ${NONE[$key]} \t ${SUMO[$key]} \t ${MILO[$key]} \t ${TERR[$key]} \t ${ALL[$key]}"
done
        
  
