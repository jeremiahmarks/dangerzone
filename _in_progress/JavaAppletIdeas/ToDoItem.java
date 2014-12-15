// The todoitem class creates a item for a todo list that has
// the following attributes and methods:
/*

Attributes:


itemName    - the name of the todo item
dueDate     - the date and time that the item is due
                if no time is specified it will default to 2359
itemURL     - if the item has a url, this is where it will go
itemLoc     - where the todo is to be done
reoccurance - if the item happens with a set frequency, this will hold
                that information
priority    - the priority level of the item
reminderTime- If the item has a reminder, this will be when it reminds
reminderHow - If the item has a reminder, this will be how
estTime     - a representation of the time needed to complete the item


Methods:
*****************************************************************
******
******   Creator/mutators
******
******************************************************************


ToDoItem(String name, Calendar dueDate, String itemURL, String itemLoc, int priority, calendar reminderTime, String reminderHow )

ToDoItem(String itemName, Calendar dueDate)

timeTillDue():Calendar
    - This will return a calendar representation of time until it is due
setPriority(int):void
setURL(String):void
setLocation(String):Void
setReoccurance(Calendar/String frequency, Calendar/String untilWhen ):void
addReminder(Calendar when, String how):String conformation
changeDueDate(Calendar newDueDate):void

*****************************************************
****                                             ****
****                 Accessor                    ****
****                                             ****
*****************************************************

getName
getDue
getURL
getLocation
getReoccurance
getPriority
getReminder


*/
import java.util.GregorianCalendar;
import java.util.Date;
import java.text.SimpleDateFormat;


public class ToDoItem
{
    private String itemName, itemURL, itemLoc, reminderHow;
    private GregorianCalendar dueDate;//, today, reminderTime, reoccurance, estTime;
    private int priority, dueMonth, dueDay, dueYear, dueHour, dueMinute;
    private Date itemsDDate;
    
    //DateFormat df1 = DateFormat.getDateTimeInstance(DateFormat.MEDIUM, DateFormat.MEDIUM);
    SimpleDateFormat format = new SimpleDateFormat("EEE MMM dd HH:mm:ss zzz yyyy");
/****************************************************
****                                             ****
****                 Constructor                 ****
****                                             ****
****************************************************/

    public ToDoItem(String name, int monthDue, int dayOfMonthDue, int yearDue, int hourDue, int minuteDue)
    {
        itemName=name;
        dueDate=new GregorianCalendar(yearDue, monthDue, dayOfMonthDue, hourDue, minuteDue);
        itemURL="";
        itemLoc="";
        reminderHow="";
        priority=1;
        itemsDDate=dueDate.getTime();
    }
    
    public String toString()
    {
        return format.format(itemsDDate);
    }
}
