From **Flask Web Development**
Make a page that only sets a cookie
> note to self:  
> figure out the dynamic relationships thing in Example 5.4  
> make sure that you reread `Integration with the Python Shell`
Some of the auto importing seems like it would be super useful for testing  


##starting server that is available externally

* install flask-script
    * `pip install flask-script`
* run the script like `$ python script.py runserver --host 0.0.0.0`
* example of template doing conditionals
```HTML+Django
    {% if name %}
        < h1> {{ name }} just won!</h1>
    {% else %}
        <p>You won, I guess</p>
    {% endif %}
```
* example of looping through a conditional in a template
```HTML+Django
    <ul>  
        {% for comment in comments %}  
            <li>{{ comment }}</li>  
        {% endfor %}  
    </ul>  
```
* also works with macros
    * macros are stored in standalone file that is imported 
    as needed.
    * macro creation
```HTML+Django
        {% macro render_comment(comment) %}
            <li>{{ comment }}</li>
        {% endmacro %}
```
    * macro use
```HTML+Django
        <ul>  
            {% for comment in comments %}  
                {{ render_comment(comment) }}  
            {% endfor %}  
        </ul>  
```
* some things about sqlalchemy
    * correct url format - 
    mysql://username:password@hostname/database
    * holy crap, it is some next level magic stuff.
    * from icp db.create_all() builds out the structures 
    that you specify in application
```python
        >>> from t1 import db
        >>> db.create_all()
        >>> from t1 import Role, User
        >>> admin_role = Role(name='admin')
        >>> user_role = Role(name='user')
        >>> user_a = User(username="a", role=admin_role)
        >>> user_b = User(username="b", role=user_role)
        >>> db.session.add_all([admin_role, user_role, user_a, user_b])
        >>> db.session.commit()
        >>> print(admin_role.id)
        >>> admin_role.name = "Something Different"
        >>> db.session.add(admin_role)
        >>> db.session.commit()
```
    * `admin_role = Role(name='admin')` creating a row in 
    the table, basically
    * `user_a = User(username="a", role=admin_role)` 
    assigning foreign keys
    * `db.session.add_all([admin_role, user_role, user_a, user_b])` 
    preparing these rows from the objects
    * `db.session.commit()` actually making the queued 
    changes
    * `admin_role.name = "Something Different"` updating an 
    object that is created in the database
    * `db.session.add(admin_role)`queuing the change to be 
    written
    * `db.session.commit()` writing the change 
    * Also
        * `db.session.delete(object)` -> `db.session.commit()` 
        to delete an item from the database
        * `Role.query.all()` to get all items from the Role 
        table (note that Role is an object I imported from 
        my main script)
        * `User.query.filter_by(role=user_role).all()` brings
        back the users who are admin
    * when you have to build the data from scratch
        * `user_role = Role.query.filter_by(name='User`).first()

    * NOTE: do not try and build and run these concurrently.
    When anything calls commit() it commits whatever is there 
    right then. 

============================================================

###Email

* `pip install flask-mail`
* Example, sending mail though gmail, with credentials in 
the environment

```python
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
```

* example of setting up asynch mail, very nice!