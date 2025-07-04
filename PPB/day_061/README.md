## Building Advanced Forms with Flask-WTForms

<h3>
    <p>
        <a href="./server.py">server.py</a>
    </p>
</h3>

<div style="font-size:1.2em">
    <p>
        We saw how we could make HTML forms work with our Flask server and get hold of the data that a user 
        enters into the form. Today, we're going to improve on that, we're going to build forms using a Flask extension 
        called <b>Flask-WTF</b>. It has a number of benefits over the simple HTML Form. e.g. 
    </p>
    <ul>
        <li>
            <b>Easy Form Validation</b> - Makes sure the user is entering data in the required format in all the 
            required fields. e.g. checking that the user's email entry has a "@" and a "." at the end. All without 
            having to write your own validation code.
        </li>
        <li>
            <b>Less Code</b> - If you have a number of forms in your website, using WTForm can dramatically reduce 
            the amount of code you have to write (or copy & paste).
        </li>
        <li>
            <b>Built in CSRF Protection</b> - CSRF stands for 
            <a href="https://owasp.org/www-community/attacks/csrf">Cross Site Request Forgery</a>, it's an attack that 
            can be made on website forms which forces your users to do unintended actions 
            (e.g. transfer money to a stranger) or compromise your website's security if it's an admin.
        </li>
    </ul>
    <p>
        Flask developers will usually choose Flask-WTF to create forms in their websites. However, in the wild, 
        you might also see projects that are built with HTML Forms. So it's important to understand how both of 
        them work.
    </p>
</div>

<h3>Secrets</h3>
<div style="font-size:1.2em">
    <p>
        By the end of today, we will build a website that holds some secrets. Only with the right username and password 
        can you access the page with our secrets. 
    </p>
</div>

<h3>Installing packages and the requirements.txt</h3>
<div style="font-size:1.2em">
    <p>
        The <b>requirements.txt</b> file is a file where you can specify all the dependencies (the installed packages 
        that your project depends on) and their versions. This means that you can share your project without all the 
        installed packages, making it a lot more lightweight. When someone downloads your project (like you have done 
        here), the requirements.txt file tells their code editor which packages need to be installed. 
        <a href="https://docs.google.com/document/u/1/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub">
        Read more on this here</a>.
    </p>
    <p>
        To install a particular package you can use the <b>Terminal</b>. To install <b>Flask-WTF</b> you would use the 
        <code>pip install</code> command.
    </p>
    <p>
        You can install all the required packages listed in the requirements.txt file for the project at the same time:
    </p>
    <p> 
        <div>
            On Windows type:
            <code>python -m pip install -r requirements.txt</code>
        </div>
        <div>
            On MacOS type:
            <code>pip3 install -r requirements.txt</code>
        </div>
    </p>
</div>

