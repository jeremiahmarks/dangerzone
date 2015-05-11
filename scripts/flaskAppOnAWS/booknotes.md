From **Flask Web Development**
Make a page that only sets a cookie

##starting server that is available externally

* install flask-script
    * `pip install flask-script`
* run the script like `$ python script.py runserver --host 0.0.0.0

* example of template doing conditionals  

    {% if name %}  
        &lt; h1> {{ name }} just won!&lt;/h1>  
    {% else %}  
        &lt;p>You won, I guess&lt;/p>  
    {% endif %}  

* example of looping through a conditional in a template

    &lt;ul>  
        {% for comment in comments %}  
            &lt;li>{{ comment }}&lt;/li>  
        {% endfor %}  
    &lt;/ul>  

* also works with macros
    * macros are stored in standalone file that is imported 
    as needed.
    * macro creation  
        {% macro render_comment(comment) %}  
            &lt;li>{{ comment }}&lt;/li>  
        {% endmacro %}  
    * macro use  
        <ul>  
            {% for comment in comments %}  
                {{ render_comment(comment) }}  
            {% endfor %}  
        </ul>  

* some things about sqlalchemy
    * correct url format - mysql://username:password@hostname/database