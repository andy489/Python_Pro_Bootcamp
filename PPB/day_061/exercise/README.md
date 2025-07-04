## Building Advanced Forms with Flask-WTForms

<h3>
    <p>
        <a href="./main.py">main.py</a>
    </p>
</h3>

<div style="text-align: center;">
    <img src="../assets/3.png" alt="" style="width: 720px;">
</div>

<div style="font-size:1.2em">
    <p>
        <b>CHALLENGE</b>: Read 
        <a href="https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/">
            Flask-WTF Quickstart - Creating Forms
        </a> and use it to figure out how to create a simple login form.
    </p>
    <p>
        SPECIFICATIONS:
    </p>
    <ul>
        <li>
            It must have an <code>email</code> and <code>password</code> field.
        </li>
        <li>
            They can both be <code>StringFields</code>.
        </li>
        <li>
            You don't have to worry about <code>validators</code>.
        </li>       
        <li>
            Both <code>email</code> and <code>password</code> inputs should be size <b>30</b>. (This describes the width of the input).
        </li>
        <li>
            You should <b>not</b> need to create any <code>&lt;label&gt;</code> or <code>&lt;input&gt;</code> elements manually using HTML.
        </li>
    </ul>
    <p>
        HINT: If you want to add csrf protection, you will need to add the following code in your login.html:
    </p>
    <p>
        <code>{{ form.csrf_token }}</code>
    </p>
    <p>
        and you will need to create a 
        <a href="https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key">secret key</a> 
        in your main.py, which will be used to generate the csrf_token. e.g.
    </p>
    <p>
        <code>app.secret_key = "some secret string"</code>
    </p>
    <p>
        This is what you're aiming for:
    </p>
    <div style="text-align: center;">
        <img src="../assets/4.png" alt="" style="width: 620px;">
    </div>
    <h2>Code Improvements for Our WTForms</h2>
    <h3>A Few Code Improvements</h3>
    <ol>
        <li>We can change the <code>password</code> input to use a <code>PasswordField</code> from WTForms, this will 
        obscure the text typed into the input.</li>
        <div style="text-align: center;">
            <img src="../assets/5.png" alt="" style="width: 620px;">
        </div>
        <div style="text-align: center;">
            <img src="../assets/6.png" alt="" style="width: 620px;">
        </div>
        <div style="text-align: center;">
            <img src="../assets/7.png" alt="" style="width: 620px;">
        </div>
        <p>There are plenty of other fields you can read about in the WTForms documentation:
            <a href="https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields">
                https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields
            </a>
        </p>
        <li>The arguments given when creating a <code>StringField</code> or <code>PasswordField</code> is for the 
            <code>label</code> property of the form field. Even though the Quickstart doesn't add it, I prefer adding 
            the keyword argument when it's not clear what the argument is for.
            <div>
                <img src="../assets/8.png" alt="" style="width: 620px;">
            </div>
            <p>
                This is the <code>label</code> property in use in login.html when our <code>form</code> object 
                is passed over.
            </p>
            <div>
                <img src="../assets/9.png" alt="" style="width: 620px;">
            </div>
        </li>
        <li>
            You might have already done this, but in the Quickstart, they set the form action to <code>"/"</code>, 
            which is a static path. It's always a good idea to use dynamically built urls like this:
            <div>
                <img src="../assets/10.png" alt="" style="width: 620px;">
            </div>
        </li>
        <li>We can also better format the layout of the labels and inputs in our WTForms 
            generated form by using normal HTML elements.
            <p>e.g.</p>
            <div>
                <img src="../assets/11.png" alt="" style="width: 620px;">
            </div>
            <p>This will result in the following layout:</p>
            <br/>
            <div>
                <img src="../assets/12.png" alt="" style="width: 260px;">
            </div>
        </li>
        <li>
            Finally, did you spot the <code>SubmitField</code> when you were looking at the 
            <a href="https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields">documentation</a> in Step 1 ? 
            This can be used to replace the submit input/button.
            <br/>
            <br/>
            <div>
                <img src="../assets/13.png" alt="" style="width: 620px;">
            </div>
            <br/>
            <div>
                <img src="../assets/14.png" alt="" style="width: 620px;">
            </div>
        </li>
    </ol>
    <h3>Adding Validation to Forms with Flask-WTF</h3>
    <p>
        One of the biggest reasons why we would choose WTForms over HTML Forms is the built-in validation. 
        Instead of us having to write our own validation code e.g. emails should contain a "@" and a "." 
        to be valid or make sure that passwords are minimum of 8 characters, we can use all these 
        validation rules straight out of the box from WTForms.
    </p>
    <ol>
        <li>We can add validator objects when we create each field in our form. e.g.</li>
        <br/>
        <div>
            <img src="../assets/15.png" alt="" style="width: 620px;">
        </div>
        <p><a href="https://wtforms.readthedocs.io/en/3.0.x/crash_course/#validators">Documentation</a></p>
        <p>
            The <code>validators</code> parameter accepts a <b>List</b> of validator <b>Objects</b>. DataRequired 
            makes the two fields required fields, so the user must type something, otherwise an error will be generated.
        </p>
        <p>
            When a form is submitted, there may be a number of errors, so a List of <code>errors</code> can be 
            generated and passed over to our form HTML as a property on the field which generated the error, e.g.
        </p>
        <p><code>form.&lt;field&gt;.errors</code></p>
        <li>We can tap into these errors and loop through them to show some text when an error appears.</li>
        <p><a href="https://wtforms.readthedocs.io/en/3.0.x/crash_course/#displaying-errors">Documentation</a></p>
        <div>
            <img src="../assets/16.png" alt="" style="width: 620px;">
        </div>
        <li>The final step is to tell our form to validate the user's entry when they hit submit. 
        So we have to edit our route and make sure it is able to respond to <code>POST</code> requests and then 
        to <code>validate_on_submit().</code>
        </li>
        <br/>
        <div>
            <img src="../assets/17.png" alt="" style="width: 620px;">
        </div>
        <p>
            If you tried to test your form at the moment, you will see that if you leave a field empty, 
            it might give you a pop-up e.g. on Chrome:
        </p>
        <div>
            <img src="../assets/18.png" alt="" style="width: 300px;">
        </div>
        <p>
            This behaviour is not from our validator, in fact it's a built-in mechanism that varies from 
            browser to browser. You'll see something different on Firefox or Safari. But If your user is 
            running Internet Explorer, they won't see any validation.
        </p>
        <li>
            In order to make sure that we are giving all users field validation, we have to switch off the browser 
            validation, and we do that with an attribute on the form element called <code>novalidate</code>.
        </li>
        <br/>
        <div>
            <img src="../assets/19.png" alt="" style="width: 620px;">
        </div>
        <p>
            Now test your validation, it should give you a warning in red if you leave any field empty 
            and click "Log In". e.g.
        </p>
        <div>
            <img src="../assets/20.png" alt="" style="width: 300px;">
        </div>
        <p>
            CHALLENGE: Using <a href="https://wtforms.readthedocs.io/en/3.0.x/validators/#module-wtforms.validators">
            the documentation on WTForm validators</a>, add <code>Email</code> validation to the email field 
            so that you must type a <code>valid email</code> (with "@" and ".") otherwise you get an error. 
            Also add <code>Length</code> validation to the password, so you must type at least <b>8 characters</b>.
        </p>
        <p>e.g. Email without "@" and 4 character password:</p>
        <div>
            <img src="../assets/21.png" alt="" style="width: 360px;">
        </div>
        <div>
            <img src="../assets/22.png" alt="" style="width: 360px;">
        </div>
        <div>
            <img src="../assets/23.png" alt="" style="width: 360px;">
        </div>
        <div>
            <img src="../assets/24.png" alt="" style="width: 300px;">
        </div>
    </ol>
    <h3>
        Receiving Form Data with WTForms
    </h3>https://wtforms.readthedocs.io/en/3.0.x/crash_course/#how-forms-get-data
    <p>
        We saw that when using a basic HTML form, we can use the request object from Flask to access 
        the key-value pairs that were entered into the form when the POST request was made.
    </p>
    <p>
        With WTForms, it's even easier to get hold of the form data. All you have to do is to tap into the
    </p>
    <p><code>&lt;form_object&gt;.&lt;form_field&gt;.data</code></p>
    <p><a href="https://wtforms.readthedocs.io/en/3.0.x/crash_course/#how-forms-get-data">Documentation</a></p>
    <p>
        But one thing we should check before printing the field data is whether if the form has been submitted 
        (POST request) or if it's GET request when the form is being rendered.
    </p>
    <p>Previously we used</p>
    <p><code>if request.method == "POST"</code></p>
    <p>
        Now, we're simply going to check the return value of <code>validate_on_submit()</code> which will be 
        <code>True</code> if validation was <b>successful after the user submitted the form</b>, 
        or <code>False</code> if it failed.
    </p>
    <div>
        <img src="../assets/24.png" alt="" style="width: 300px;">
    </div>
    <p>
        CHALLENGE: Update the <code>/login</code> route in <b>main.py</b> so that if the form was <b>submitted</b> and 
        <b>validated</b> and their <b>credentials</b> matched the following:
    </p>
    <p>email: <b>admin@email.com</b></p>
    <p>password: <b>12345678</b></p>
    <p>email: <b>admin@email.com</b></p>
    <p>then show them the <b>success.html</b> page.</p>
    <p>Otherwise, show them the <b>denied.html</b> page</p>
    <p>e.g.</p>
    <div>
        <h4>Access Denied</h4>
        <img src="../assets/25.gif" alt="" style="width: 380px;">
    </div>
    <div>
        <h4>Access Granted</h4>
        <img src="../assets/26.gif" alt="" style="width: 380px;">
    </div>
</div>
