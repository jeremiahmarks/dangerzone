source ~/.webanize.conf
####
## webanize relies on a properly set up webanize.conf file as well as an 
## installation of Syntax Highlighter (http://alexgorbatchev.com/SyntaxHighlighter/download/)

if [[ -z "$1" ]]; then
	echo "Please pass a valid file to be webanized."
	exit 5
else
	if [[ ! -f "$1" ]]; then
		echo "please only pass me regular files."
		exit 6
	fi
fi

file_contents=$(cat "$1")



################################################################################
################################################################################
##
##		Get Desired Title
##		Set what the eventual foldername will be for the online path
##		get current timestamp

read -p "Please enter the title of the script:    " html_title

foldername=${html_title// /}
timestamp=$(date +"%F:%T")


################################################################################
################################################################################
##
##		1. Get list of available brushes
##		2. Prompt user to select one by number
##		3. set brush_lang variable to selection


startDir=$PWD
brush_filename_pattern="*shBrush*"
cd "$local_path_to_js_folder"
files=(*)
echo ":"
for i in "${!files[@]}"; do 
	if [[ "${files[$i]}" == $brush_filename_pattern ]]; then  #this comparison only works correctly without the quotes
		thislang="${files[$i]/shBrush/}"
		printf "%s  %s\n" "$i" "${thislang/.js/}"
	fi
done
read -p "Please select your language: " lang_no

brush_lang="${files[$lang_no]}"


################################################################################
################################################################################
##
##		convert from the brush_lang input to the needed format for the 
##		<pre class="brush $language"> line

classlang="${brush_lang/shBrush/}"
dblang="${classlang/.js/}"
classlang=$(echo "$dblang" | tr '[:upper:]' '[:lower:]')

################################################################################
################################################################################
##
##		move to local portfolio
##		if folder "my$classlang" does not exist create it
##		move into folder "my$classlang"
##		
##		if foldername does not exist create it
##		move into folder
##		if index.html exists rename to index.timedate:of:last:edit.html
##		: > index.html
##		cat "$html_output">>index.html
##		cat "original_file" >> index.html
##		cat "</pre>\n</body>\n</html>">>index.html

cd "$local_path_to_portfolio"

if [[ ! -e "my$classlang" ]]; then `mkdir "my$classlang"`; fi

cd "my$classlang"

if [[ ! -e "$foldername" ]]; then `mkdir "$foldername"`; fi

cd "$foldername"

if [[ -e "index.html" ]]; then
	newtimestamp=$(head -n 1 index.html)
	newtimestamp="${newtimestamp/<!--/}"
	newtimestamp="${newtimestamp/-->/}"
	if [[ ${#newtimestamp} = 19 ]]; then `mv ./index.html ./index."$newtimestamp".html`; else `mv ./index.html ./index.$(date +"%D-%T").html`; fi
fi

html_output="<!--$timestamp-->
<html>
<head>
	<title>$html_title</title>
	<script type=\"text/javascript\" src=\"$web_path_to_js_folder/shCore.js\"></script>
	<script type=\"text/javascript\" src=\"$web_path_to_js_folder/$brush_lang\"></script>
	<link type=\"text/css\" rel=\"stylesheet\" href=\"$web_path_to_css/shCoreDefault.css\"/>
	<link type=\"text/css\" rel=\"stylesheet\" href=\"$web_path_to_css/css/shThemeRDark.css\"/>
	<script type=\"text/javascript\">SyntaxHighlighter.all();</script>
</head>

<body>
<pre class=\"brush: $classlang;\">
"
echo "$html_output" >> index.html
echo "$file_contents" >> index.html
echo "</pre></body></html>" >> index.html

################################################################################
################################################################################
##
##	Upload file to server
## 	create temp file to add database comments in, 
##	cat the contents of the file into that file
##	open that file in $EDITOR
## after file is saved and closed connect to database and upload appropriate info
echo "uploading now, this may take a second."
`"$script_to_sync_local_content_to_webserver"` 


dbloc="$portfolio_address_on_web/my$classlang/$foldername"
dbdate=$(date +"%Y-%m-%d")
imageloc="$image_folder_on_web/$classlang.png"
################################################################################
## Write query to find all db entries where source code location is the same
##	SELECT * FROM 'portfolio' WHERE  `sourcecode` = $dbloc


oldaboutinfo=""

testquery="SELECT COUNT(id) FROM portfolio WHERE sourcecode LIKE '$dbloc'"
firstresults=`mysql --host=$hostname --user=$username --password=$pw -e "USE $dbname; $testquery;"`
otherrecords="${firstresults: -1}"


if [[ "$otherrecords" -ne 0 ]]; then



	myfirstquery="SELECT dateadded,about  FROM portfolio WHERE sourcecode LIKE '$dbloc'"

	i=1
	while read -r line
	do
		test $i -eq 1 && ((i=i+1)) && continue
		oldaboutinfo+="<br> $line <br>"
		oldaboutinfo+=$'\n'
	done < <(mysql --host=$hostname --user=$username --password=$pw -e "USE $dbname; $myfirstquery;")


	tempstring=$'"\n'
	tempstring+=$oldaboutinfo
	tempstring+=$'\n"'



	oldaboutinfo=$tempstring


else
	oldaboutinfo="\" \" "
fi

detailsfilename="$timestamp$foldername"
touch "$detailsfilename"

fileexplanation="################################################################################
## This file will be used to check that the information that will be submitted
## to the database is correct. All lines that are blank or start with a # are
## considered comments and excluded. 
## Please check the information, fill out the about section, and then save and 
## exit. After doing so this script will upload the data to a MySQL server whose
## details are stored in the file ~/pw.pw
##
## I am including the contents of $html_title at the bottom of this file to aid
## in creating the \"About\" section. Anything below the three consecutive lines
## of hash marks will not be included in the \"About\" section.
################################################################################
"

echo -e "$fileexplanation" >> "$detailsfilename"
echo -e "project_name=\"$html_title\"" >> "$detailsfilename"
echo -e "  added_date=$dbdate" >> "$detailsfilename"
echo -e " script_lang=$dblang" >> "$detailsfilename"
echo -e "  source_loc=$dbloc" >> "$detailsfilename"
echo -e "pic_location=$imageloc" >> "$detailsfilename"
echo -e "about_script=$oldaboutinfo" >> "$detailsfilename"
echo "################################################################################" >> "$detailsfilename"
echo "################################################################################" >> "$detailsfilename"
echo "################################################################################" >> "$detailsfilename"
echo "#### 5c608931d289623ad3212e3ea0d80b00###########################################" >> "$detailsfilename"
echo "## Below these lines will not be included in the database upload  ##############" >> "$detailsfilename"
echo "################################################################################" >> "$detailsfilename"
echo  "$file_contents"  >> "$detailsfilename"

"${EDITOR:-nano}" "$detailsfilename"

################################################################################
################################################################################
##
##	Before sourcing the file $detailsfilename, find where the file_contents start
##  and either truncate everything after that or delete it.
## 	create newconf file. 
##  read each line, if the line starts with one of the variable names
##		check if the line has an open quote
##		if line has open quote

conffile="$detailsfilename.conf"

(sed '/5c608931d289623ad3212e3ea0d80b00/q' "$detailsfilename") >>"$conffile"


source "$conffile"

if [[ "$otherrecords" -ne 0 ]]; then
	myquery="UPDATE portfolio SET about=\"$about_script\" WHERE sourcecode=\"$dbloc\""
else
	myquery="INSERT INTO portfolio (name, language, about, sourcecode, piclocation, dateadded) VALUES (\"$project_name\", \"$script_lang\", \"$about_script\", \"$source_loc\", \"$pic_location\", \"$added_date\")"
fi

results=`mysql --host=$hostname --user=$username --password=$pw -e "USE $dbname; $myquery;"`

echo $results
