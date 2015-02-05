SYNOPSIS

       date [OPTION]... [+FORMAT]
       date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]

DESCRIPTION

       Display the current time in the given FORMAT, or set the system date.

       -d, --date=STRING
	      display time described by STRING, not 'now'

       -f, --file=DATEFILE
	      like --date once for each line of DATEFILE

       -r, --reference=FILE
	      display the last modification time of FILE

       -R, --rfc-2822
	      output date and time in RFC 2822 format

       --rfc-3339=TIMESPEC
	      output date and time in RFC 3339 format.	TIMESPEC='date', 'sec-
	      onds', or 'ns' for date and time to the indicated precision.

       -s, --set=STRING
	      set time described by STRING

       -u, --utc, --universal
	      print or set Coordinated Universal Time

       --help display this help and exit

       --version
	      output version information and exit

       FORMAT controls the output.  The only valid option for the second  form
       specifies Coordinated Universal Time.  Interpreted sequences are:

       %%     a literal %

       %a     locale's abbreviated weekday name (e.g., Sun)

       %A     locale's full weekday name (e.g., Sunday)

       %b     locale's abbreviated month name (e.g., Jan)

       %B     locale's full month name (e.g., January)

       %c     locale's date and time (e.g., Thu Mar  3 23:05:25 2005)

       %C     century; like %Y, except omit last two digits (e.g., 21)

       %d     day of month (e.g, 01)

       %D     date; same as %m/%d/%y

       %e     day of month, space padded; same as %_d

       %F     full date; same as %Y-%m-%d

       %g     last two digits of year of ISO week number (see %G)

       %G     year of ISO week number (see %V); normally useful only with %V

       %h     same as %b

       %H     hour (00..23)

       %I     hour (01..12)

       %j     day of year (001..366)

       %k     hour ( 0..23)

       %l     hour ( 1..12)

       %m     month (01..12)

       %M     minute (00..59)

       %n     a newline

       %N     nanoseconds (000000000..999999999)

       %p     locale's equivalent of either AM or PM; blank if not known

       %P     like %p, but lower case

       %r     locale's 12-hour clock time (e.g., 11:11:04 PM)

       %R     24-hour hour and minute; same as %H:%M

       %s     seconds since 1970-01-01 00:00:00 UTC

       %S     second (00..60)

       %t     a tab

       %T     time; same as %H:%M:%S

       %u     day of week (1..7); 1 is Monday

       %U     week number of year, with Sunday as first day of week (00..53)

       %V     ISO week number, with Monday as first day of week (01..53)

       %w     day of week (0..6); 0 is Sunday

       %W     week number of year, with Monday as first day of week (00..53)

       %x     locale's date representation (e.g., 12/31/99)

       %X     locale's time representation (e.g., 23:13:48)

       %y     last two digits of year (00..99)

       %Y     year

       %z     +hhmm numeric timezone (e.g., -0400)

       %:z    +hh:mm numeric timezone (e.g., -04:00)

       %::z   +hh:mm:ss numeric time zone (e.g., -04:00:00)

       %:::z  numeric  time  zone  with	 :  to necessary precision (e.g., -04,
	      +05:30)

       %Z     alphabetic time zone abbreviation (e.g., EDT)

       By default, date	 pads  numeric	fields	with  zeroes.	The  following
       optional flags may follow '%':

	      - (hyphen) do not pad the field _ (underscore) pad with spaces 0
	      (zero) pad with zeros ^ use upper case if possible #  use	 oppo-
	      site case if possible

       After  any  flags  comes	 an optional field width, as a decimal number;
       then an optional modifier, which is either E to use the locale's alter-
       nate  representations  if available, or O to use the locale's alternate
       numeric symbols if available.

ENVIRONMENT

       TZ     Specifies the timezone, unless overridden by command line param-
	      eters.  If neither is specified, the setting from /etc/localtime
	      is used.

AUTHOR

       Written by David MacKenzie.

REPORTING BUGS

       Report bugs to <bug-coreutils@gnu.org>.

COPYRIGHT

       Copyright (C) 2006 Free Software Foundation, Inc.
       This is free software.  You may redistribute copies  of	it  under  the
       terms	   of	    the	     GNU      General	   Public      License
       <http://www.gnu.org/licenses/gpl.html>.	There is NO WARRANTY,  to  the
       extent permitted by law.

SEE ALSO

       The  full documentation for date is maintained as a Texinfo manual.  If
       the info and date programs are properly installed  at  your  site,  the
       command

	      info date

       should give you access to the complete manual.

date 5.97			  March 2012			       DATE(1)

� 1994 Man-cgi 1.15, Panagiotis Christias <christia@theseas.ntua.gr>
