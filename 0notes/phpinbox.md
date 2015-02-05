**php inbox notes

on jlmarks.org/inbox there will exist a text field that will allow input. it
will have radio buttons below the field, however those can be overwritten with
short code precedimg the entry. for instance a todo item could be entered
as"do:something". 

other shortcodes may include:

* *log* to log an item
* *buy* to reme,ber a purchasable

after entry the item will be added to a db.

There will also exist various folders which will sort and display the data in
the database. ie:

* list.jlmarks.org/all -- all items in the database
* list.jlmarks.org/todo -- all todo items
* list.jlmarks.org/tobuy -- all to buy items
* list.jlmarks.org/log -- all log items
* list.jlmarks.org/unsort -- all unsorted items

future development will include additional fields for each set of information.

====================================
Different types of information that the inbox will need to handle:

* todo
* tobuy
* log
* link
* image
* idea
* transactions

=====================================
Display formats:

if all images: tiled boxed images where the box attempts to auto form to
correct size. 

if all transactions: spreadsheet type view

=======================================

File Structure

* index.php     -- the main file which loads the other files as needed. 
* functions.php -- the main "driver" file which will have all of the functions needed to run the website
* config.php    -- this file will contain the needed information to access the database, etc.
* css/style.css -- the main css-styling for this project

=======================================================
Logic/Approach

* index.php will initially display a welcome message, perhaps a logo, and a text field for input.
* index.php will also have several hidden fields to record date/time/location information
* index.php will have a submit button.
* upon submitting the data will be parsed to figure out what type of information it is.
* data type will determine how the information is processed/which function will be used to connect to database.
