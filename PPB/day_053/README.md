## Topic

- Data Entry Job Automation - Capstone Project

## Zillow Data Entry

<h3>
    <p>
        <a href="main.py">main.py</a>
    </p>
</h3>

<h2>
    Set up your own Google Form
</h2>
<div style="font-size: 1.2em">
    <p>
        First, you need to create a new form in Google Forms,
    </p>
    <ol>
        <li>
            Go to 
            <a href="https://docs.google.com/forms/">https://docs.google.com/forms/</a>
            and create your own form:
            <div>
                <img src="assets/01.png" alt="google forms" style="width: 540px;"/>
            </div>
        </li>
        <li>
            Add 3 questions to the form, make all questions "short answer":
            <div>
                <img src="assets/02.png" alt="create form" style="width: 540px;"/>
            </div>
        </li>
        <li>
            Click send and copy the link address of the form. You will need to use this in your program.
            <div>
                <img src="assets/03.png" alt="publish form" style="width: 540px;"/>
            </div>
            <div>
                <img src="assets/04.png" alt="get url" style="width: 540px;"/>
            </div>
        </li>
    </ol>
</div>
<h2>
    Go to our Zillow-Clone Website (or use live search)
</h2>
<div style="font-size: 1.2em">
     <ol start="4">
        <li>
            Go to 
            <a href="https://appbrewery.github.io/Zillow-Clone/">https://appbrewery.github.io/Zillow-Clone/</a>
            and see how the website is structured. This is where you'll be scraping the data from:
            <div>
                <img src="assets/05.png" alt="zillow search" style="width: 540px;"/>
            </div>
        </li>
    </ol>
</div>
<h2>
    BeautifulSoup Requirements
</h2>
<div style="font-size: 1.2em">
    <ul>
        <li>
            Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address (Step 4 above).
        </li>
        <li>
            Create a list of links for all the listings you scraped. e.g.
        </li>
        <div>
            <img src="assets/06.png" alt="list of links" style="width: 540px;"/>
        </div>
        <li>
            Create a list of prices for all the listings you scraped. e.g.
        </li>
        <div>
            <img src="assets/07.png" alt="list of addresses" style="width: 540px;"/>
        </div>
    </ul>   
    Clean up the strings, by removing any "+" symbols and other information so that you are only left with a dollar price. The price should look like "$1,234" instead of "$1,234+ /mo"
    <ul>
        <li>
            Create a list of addresses for all the listings you scraped. e.g.
        </li>
        <div>
            <img src="assets/08.png" alt="list of prices" style="width: 540px;"/>
        </div>
    </ul> 
    Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.
</div>
<h3>
    Selenium Requirements
</h3>
<div style="font-size: 1.2em">
    <ul>
        <li>
            Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing. e.g.
        </li>
        <div>
            <img src="assets/09.gif" alt="requests" style="width: 540px;"/>
        </div>
        <li>
            Collect responses (observe selenium bot result):
        </li>
        <div>
            <img src="assets/10.gif" alt="collect" style="width: 540px;"/>
        </div>
        Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. You should end up with a spreadsheet with all the details from the properties.
    </ul>
</div>
<div>
    <img src="assets/11.png" alt="results" style="width: 540px;"/>
</div>

<h3>
    Objective 🎯
</h3>
<div style="font-size: 1.2em">
    You should end up with a spreadsheet that looks something like this.
</div>
<div>
    <img src="assets/12.png" alt="spreadsheet" style="width: 540px;"/>
</div>
<h3>
    Resources for this project
</h3>
<div style="font-size: 1.2em">
    <a href="https://appbrewery.github.io/Zillow-Clone/">🔗 Zillow Clone Site</a>
</div>
<h3>
    Useful or interesting links that contributed to the idea for the project
</h3>
<div style="font-size: 1.2em">
    <a href="https://www.indeed.com/jobs?q=data+entry&l=remote&vjk=5bdca26151adaeeb">🔗 Data Entry Jobs on Indeed</a><br>
    <a href="https://www.reddit.com/r/Python/comments/8uxifv/has_anyone_automated_their_job_completely/">🔗 Automating Your Job Reddit</a><br>
    <a href="https://workplace.stackexchange.com/questions/93696/is-it-unethical-for-me-to-not-tell-my-employer-i-ve-automated-my-job">🔗 Automated Job Story</a><br>
    <a href="https://www.zillow.com/san-francisco-ca/rentals/">🔗 Zillow Property Search</a><br>
    <a href="https://docs.google.com/forms/u/0/">🔗 Google Forms</a>
</div>


