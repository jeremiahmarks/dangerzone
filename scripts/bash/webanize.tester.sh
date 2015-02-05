source ~/.webanize.conf



newstring=""

dbloc="http://portfolio.jlmarks.org/myJava/ASCIIBird"

testquery="SELECT COUNT(id) FROM portfolio WHERE sourcecode LIKE '$dbloc'"
firstresults=`mysql --host=$hostname --user=$username --password=$pw -e "USE $dbname; $testquery;"`
otherrecords="${firstresults: -1}"


if [[ "${firstresults: -1}" -ne 0 ]]; then
	echo "I am in the first firstresults if statement"


	myfirstquery="SELECT about,dateadded  FROM portfolio WHERE sourcecode LIKE '$dbloc'"

	i=1
	while read -r line
	do
		test $i -eq 1 && ((i=i+1)) && continue
		oldaboutinfo+="$line <br>"
		oldaboutinfo+=$'\n'
	done < <(mysql --host=$hostname --user=$username --password=$pw -e "USE $dbname; $myfirstquery;")

	echo "I just finished the queryloop and oldaboutinfo equals $oldaboutinfo"

	tempstring=$'"\n'
	tempstring+=$oldaboutinfo
	tempstring+=$'\n"'

	echo "i just completed the tempstring creator and tempstring = $tempstring"

	oldaboutinfo=$tempstring
	echo "now oldaboutinfo = $oldaboutinfo"

else
	oldaboutinfo="\" \" "
fi

echo $oldaboutinfo
# myfirstquery="SELECT dateadded,about  FROM portfolio WHERE sourcecode LIKE '$dbloc'"
# i=1
# while read -r line
# do
# 	test $i -eq 1 && ((i=i+1)) && continue
# 	newstring+="$line <br>"
# 	newstring+=$'\n'
# done < <(mysql --host=$hostname --user=$username --password=$pw -e "USE $dbname; $myfirstquery;")

# tempstring=$'"\n'
# tempstring+=$newstring
# tempstring+=$'\n"'

# echo "**********************************************"

# echo $newstring
# echo "**********************************************"
# echo "**********************************************"
# echo $tempstring