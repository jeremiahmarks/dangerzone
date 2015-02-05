#!/usr/bin/env bash
source ~/.webanize.conf

projectFlag=false #This flag will be used to indicate that webanize should expect a folder with multiple files 
webanizehelp() 
{ 
	echo "Webanize currently accepts the following options:"
	echo "	-f <file>		the file that will be webanized. NOTE: -f and -p are mutually exclusive options"
	echo "	-p <folder>    	the project flag, this flag lets webanize know that the folder is a project of multiple files."
	echo "	-h 				print this help information"
}

timestamp=$(date +"%F:%T")
startDir=$PWD

setfilelanguage()
{
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

	#################################
	## Need to write code that checks if projectFlag is set and project_lang is not set. 
	## if that is the case this needs to set the project language
	#################################
	if [[]]

	brush_lang="${files[$lang_no]}"
	classlang="${brush_lang/shBrush/}"
	dblang="${classlang/.js/}"
	classlang=$(echo "$dblang" | tr '[:upper:]' '[:lower:]')
}

indexcleanup()
{
	if [[ -e "index.html" ]]; then
		if [[ ! -e "old" ]]; then `mkdir old`; fi 
		newtimestamp=$(head -n 1 index.html)
		newtimestamp="${newtimestamp/<!--/}"
		newtimestamp="${newtimestamp/-->/}"
		if [[ ${#newtimestamp} = 19 ]]; then `mv ./index.html ./old/index."$newtimestamp".html`; else `mv ./index.html ./old/index.$(date +"%D-%T").html`; fi
		cd old
		if [[ -e "index.html" ]]; then `rm index.html`; fi
		files=(*)
		echo "<html> <head> <link href=\"http://jlmarks.org/css/portfolio.css\" rel=\"stylesheet\" type=\"text/css\"> </head> <body> <h1>History of $html_title</h1> <div class=\"oldfileslist\"> " >> index.html
		for i in "${!files[@]}"; do
			thisdatetime="${files[$i]/.html/}"
			thisdatetime="${thisdatetime/index./}"
			echo "<div class=\"oldfile\"><a href=\"./${files[$i]}\">$thisdatetime</a></div></br>" >> index.html
		done
		echo "</div></body></html>" >> index.html
		cd ..

	fi


}

singlefilehtml()
{
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
}

createhtmlfilelocation()
{
	cd "$local_path_to_portfolio"

	if [[ ! -e "my$classlang" ]]; then `mkdir "my$classlang"`; fi

	cd "my$classlang"

	if [[ ! -e "$foldername" ]]; then `mkdir "$foldername"`; fi

	cd "$foldername"

	# if [[ -e "index.html" ]]; then
	# 	newtimestamp=$(head -n 1 index.html)
	# 	newtimestamp="${newtimestamp/<!--/}"
	# 	newtimestamp="${newtimestamp/-->/}"
	# 	if [[ ${#newtimestamp} = 19 ]]; then `mv ./index.html ./index."$newtimestamp".html`; else `mv ./index.html ./index.$(date +"%D-%T").html`; fi
	# fi
}

createsinglefileconf()
{

	dbdate=$(date +"%Y-%m-%d")
	imageloc="$image_folder_on_web/$classlang.png"

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

	conffile="$detailsfilename.conf"

	(sed '/5c608931d289623ad3212e3ea0d80b00/q' "$detailsfilename") >>"$conffile"
}

createinitialabout()
{
	dbloc="$portfolio_address_on_web/my$classlang/$foldername"
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
}

createprojectlocation()
{
	cd "$local_path_to_portfolio"

	if [[ ! -e "my$project_lang" ]]; then `mkdir "my$project_lang"`; fi

	cd "my$classlang"

	if [[ ! -e "$foldername" ]]; then `mkdir "$foldername"`; fi

	cd "$foldername"
}

webanizeAProject()
{
	read -p "Please enter the title of the project:    " project_title
	project_lang=false
	setfilelanguage




}


options='hf:p:'
while getopts $options option
do
	case $option in
		f ) targetfile=$OPTARG; file_contents=$(cat $targetfile); echo "f selected";;
		p ) projectFlag=true; projectfolder=$OPTARG;;
		h ) webanizehelp; exit;;
        \? ) echo "Unknown option: -$OPTARG" >&2; exit 1;;
        :  ) echo "Missing option argument for -$OPTARG" >&2; exit 1;;
        *  ) echo "Unimplemented option: -$OPTARG" >&2; exit 1;;
    esac
done

shift $(($OPTIND - 1))

echo "filecontents = $file_contents"

if ! $projectFlag && [[ -d $1 ]]
then
	echo "if a folder is included you must specify this as a project (-p)" >&2
	exit 1
fi 


if  ! $projectFlag 
then
	read -p "Please enter the title of the script:    " html_title
	foldername=${html_title// /}
	setfilelanguage
	createhtmlfilelocation
	indexcleanup
	singlefilehtml
	detailsfilename="$timestamp$foldername"
	touch "$detailsfilename"
	createinitialabout
	createsinglefileconf
	source "$conffile"
	if [[ "$otherrecords" -ne 0 ]]; then
		myquery="UPDATE portfolio SET about=\"$about_script\" WHERE sourcecode=\"$dbloc\""
	else
		myquery="INSERT INTO portfolio (name, language, about, sourcecode, piclocation, dateadded) VALUES (\"$project_name\", \"$script_lang\", \"$about_script\", \"$source_loc\", \"$pic_location\", \"$added_date\")"
	fi
	results=`mysql --host=$hostname --user=$username --password=$pw -e "USE $dbname; $myquery;"`
	echo $results
fi

