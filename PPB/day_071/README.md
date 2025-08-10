<h1>Publishing Our Flask Website</h1>
<div style="font-size:1.2em">
    <ul>
        <li>GitHub</li>
        <li>Heroku</li>
        <li>GUnicorn</li>
    </ul>
    <h2>Deploy Your Website</h2>
    <ul>
        <li>
            <b>Add .gitifnore file</b>
            <ul>
                <li><p>Prevents Sensitive Data from Being Committed</p></li>
            </ul>
        </li>
        <li>
            <b>Use environment variables to store sensitive information</b>
            <ul>
                <li>
                    <p>We don't want any configuration details and sensitive data inside our app.py</p>
                </li>
            </ul>
        </li>
        <li>
            <b>Set your app to run in debug=False mode</b>
        </li>
        <li>
            <b>Review requirements.txt file</b>
            <ul>
                <li><p>Add "gunicorn" and "psycopg2-binary" packages</p></li>
            </ul>
        </li>
        <li>
            <b>Setup a WSGI server with gunicorn</b>
            <ul>
                <li>
                    <p>
                        You might recall that every time we ran our app, we got a warning telling us that when we want 
                        to make our website go live and go from development to production mode that we should 
                        use a WSGI server.
                    </p>
                </li>
                <li>
                    <p>
                        WSGI stands for Web Server Gateway Interface, and it's described here: 
                        <a href="https://www.python.org/dev/peps/pep-3333/">
                            https://www.python.org/dev/peps/pep-3333/
                        </a>
                    </p>
                </li>
                <li>
                    <p>
                        In summary: normal web servers can't run Python applications, so a special type of server was 
                        created (WSGI) to run our Flask app.  Essentially, a WSGI server standardises the language and 
                        protocols between our Python Flask application and the host server.
                    </p>
                </li>
                <li>
                    <p>
                        There are many WSGIs to choose from, but we'll use the most popular - 
                        <a href="gunicorn"><b>gunicorn</b></a>. 
                        That way our hosting provider will call gunicorn to run our code.
                    </p>
                </li>
            </ul>
        </li>
        <li>
            <b>Create a Procfile</b>
            <ul>
                <li>
                    <p>
                        We need to tell our hosting provider about our gunicorn server, what our app is called, 
                        and how to run our Flask app. We do that using a config file called a <b>Procfile</b>.
                    </p>
                </li>
                <li>
                    <p>
                        Create a new file in the project top-level folder called <code>Procfile</code>.
                    </p>
                    <p>
                        NOTE: make sure you spell the name of the file exactly as you see above, with a capital P 
                        and no file extension.
                    </p>
                </li>
                <li>
                    <p>
                        Type the following into the Procfile: <code>web: gunicorn app:app</code>.
                        The first "app" is the name of the server .py file and the second is a key word
                    </p>
                    <p>
                        This will tell our hosting provider to create a <code>web</code> <b>worker</b> that is able to 
                        receive HTTP requests. The Procfile also says to use <b>gunicorn</b> to serve your web app. A
                        nd finally it specifies the Flask <b>app</b> object is the <b>main.py</b> file. That way the 
                        hosting provider knows about the entry point for the app and what our app is called.
                    </p>
                    <hr>
                    <p style="text-align: center">
                        <img src="assets/01.png" alt="" style="width: 540px;"/>
                    </p>
                    <hr>
                    <p>
                        NOTE: If your app is not inside a file called main.py then you should change main to your 
                        file name.
                    </p>
                </li>
            </ul>
        </li>
    </ul>
    <h2>Sign up to a hosting provider and create your web service</h2>
    <h3>Create an account with a hosting provider</h3>
    <ul>
        <li>
            <p>
                There are many different hosting providers to choose from when it comes to making your app go 
                live on the internet. Features and pricing vary between them and their pricing plans can change. 
                It's up to us to choose. For this project, we choose to host on render.com
            </p>
            <table>
                <tr>
                    <th>Provider</th>
                    <th>~Cost/Month</th>
                    <th>Name of Plan</th>
                </tr>
                <tr>
                    <td><a href="https://www.heroku.com/pricing/" target="_blank">Heroku</a></td>
                    <td>$5</td>
                    <td>Eco & Basic</td>
                </tr>
                <tr>
                    <td><a href="https://render.com/pricing" target="_blank">render</a></td>
                    <td>$5</td>
                    <td>Individual</td>
                </tr>
                <tr>
                    <td><a href="https://render.com/pricing" target="_blank">Cyclic</a></td>
                    <td>$0</td>
                    <td>Free Forever</td>
                </tr>
                <tr>
                    <td><a href="https://glitch.com/pricing" target="_blank">Glitch</a></td>
                    <td>$0</td>
                    <td>Starter</td>
                </tr>
                <tr>
                    <td><a href="https://vercel.com/pricing" target="_blank">Vercel</a></td>
                    <td>$0</td>
                    <td>Hobby</td>
                </tr>
                <tr>
                    <td><a href="https://www.pythonanywhere.com/pricing/" target="_blank">PythonAnywhere</a></td>
                    <td>$0</td>
                    <td>Beginner</td>
                </tr>
            </table>
            <p>
                The nice thing about most of these providers is that they can easily deploy your app straight from a 
                GitHub repo. We've done most of the difficult bits already. There are just a few steps left:
            </p>
            <ol style="list-style: arabic">
                <li>Create an account with the hosting provider</li>
                <li>Link our GitHub repo with the host</li>
                <li>Set up a PostgreSQL database with the host</li>
                <li>Store the key-value pairs for our environment variables with our host</li>
            </ol>
        </li>
    </ul>
    <h3>Create an account e.g., on render.com</h3>
    <p>
        Heroku discontinued their free plan, but other providers are still offering one. You can create an 
        account on render.com simply by signing up via Github.
    </p>
</div>
