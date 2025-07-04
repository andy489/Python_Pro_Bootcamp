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
            <div>
                <img src="../assets/13.png" alt="" style="width: 620px;">
            </div>
            <div>
                <img src="../assets/14.png" alt="" style="width: 620px;">
            </div>
        </li>
    </ol>
</div>
