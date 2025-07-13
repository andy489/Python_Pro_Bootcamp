## Databases with SQLite and SQLAlchemy

# Virtual Bookshelf
<h3>
    <p>
        <a href="./server.py">server.py</a>
    </p>
</h3>

<div style="text-align: center;">
    <img src="assets/1.gif" alt="" style="width: 840px;">
</div>

<div style="font-size:1.3em">
    <p>
        Have you ever wanted to keep track of the books you have read and give each book a rating?
    </p>
    <p>
        This is not a new concept and there are plenty of companies that have built something for exactly this purpose.
    </p>
    <p>
        e.g. <a href="https://www.librarything.com/">https://www.librarything.com/</a>
    </p>
    <p>
        But in order to do this, we will need to use a database. We will create an SQLite database and perform:
        create, read, update and delete data in the database.
    </p>
    <p>We'll also be hooking up our database with a Flask application to serve data whenever needed.</p>
</div>
<div style="font-size:1.3em">
    <h2>CRUD Operations with SQLAlchemy</h2>
    <h3>Create a New Database</h3>
    <div style="text-align: center;">
        <img src="assets/2.png" alt="" style="width: 840px;">
    </div>
    <p>
        As of flask-sqlalchemy version 3.1, you need to pass a subclass of DeclarativeBase to the constructor of the database.
    </p>
    <h3>Create a New Table</h3>
    <p>
        Next we define and create the model. 
        What is the <code>:</code> used for? 
        Explicitly declaring a variable type. 
        Below we are explicitly saying that <code>id</code> is of type <code>Mapped</code>. 
        SQLAlchemy uses the generic <code>Mapped</code> so that it can 
        <a href="https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#using-annotated-declarative-table-type-annotated-forms-for-mapped-column">type check</a>
        the data that will be stored in the database.
    </p>
    <div style="text-align: center;">
        <img src="assets/3.png" alt="" style="width: 840px;">
    </div>
    <p>
        In addition to these things, the most crucial thing to figure out when working with any new database 
        technology is how to CRUD data records.
    </p>
    <ul>
        <li><b>C</b>reate</li>
        <li><b>R</b>ead</li>
        <li><b>U</b>pdate</li>
        <li><b>D</b>elete</li>
    </ul>
    <p>
        Let's go through each of these using SQLite and SQLAlchemy:
    </p>
    <h3><u>Create</u> A New Record</h3>
    <div style="text-align: center;">
        <img src="assets/4.png" alt="" style="width: 840px;">
    </div>
    <p>NOTE: When creating new records, the primary key fields is optional. you can also write:</p>
    <p><code>new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)</code></p>
    <p>the <code>id</code> field will be auto-generated.</p>
    <h3><u>Read</u> All Records</h3>
    <div style="text-align: center;">
        <img src="assets/5.png" alt="" style="width: 840px;">
    </div>
    <p>
        To read all the records we first need to create a "query" to select things from the database. 
        When we execute a query during a database session we get back the rows in the database (a <code>Result</code> 
        object). We then use <code>scalars()</code> to get the individual elements rather than entire rows.
    </p>
    <h3><u>Read</u> A Particular Record By Query</h3>
    <div style="text-align: center;">
        <img src="assets/6.png" alt="" style="width: 840px;">
    </div>
    <p>To get a single element we can use <code>scalar()</code> instead of <code>scalars()</code>.</p>
    <h3><u>Update</u> A Particular Record By Query</h3>
    <div style="text-align: center;">
        <img src="assets/7.png" alt="" style="width: 840px;">
    </div>
    <h3><u>Update</u> A Particular Record By PRIMARY KEY</h3>
    <div style="text-align: center;">
        <img src="assets/8.png" alt="" style="width: 840px;">
    </div>
    <p>
        Flask-SQLAlchemy also has some handy 
        <a href="https://flask-sqlalchemy.palletsprojects.com/en/stable/queries/#queries-for-views">
            extra query methods
        </a> like <code>get_or_404()</code> that we can use. 
        Since Flask-SQLAlchemy version 3.0 the previous query methods like <code>Book.query.get()</code> 
        have been deprecated.
    </p>
    <h3><u>Delete</u> A Particular Record By PRIMARY KEY</h3>
    <div style="text-align: center;">
        <img src="assets/9.png" alt="" style="width: 840px;">
    </div>
    <p>
        You can also delete by querying for a particular value e.g. by title or one of the other properties. 
        Again, the <code>get_or_404()</code> method is quite handy.
    </p>
</div>