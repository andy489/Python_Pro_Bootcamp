## Blog Capstone Project Part 2 - Adding Styling

<h3>
    <p>
        <a href="./server.py">server.py</a>
    </p>
</h3>
<h3>
    Blog upgrade
</h3>
<div style="text-align: center;">
    <img src="assets/1.png" alt="" style="width: 440px;">
</div>

<div style="font-size:1.2em">
    <p>
        We already built an upgraded version of our blog website that uses Bootstrap for styling. 
        The only part of the website that doesn't work is the contact form on the Contact Page.
        This is because we need to learn about submitting HTML forms and catching the submitted data in our Flask server. 
    </p>
    <h3>HTML Forms in Flask</h3>
    <p>
        So the goal for today is to understand how HTML forms are submitted and how to use the data from the form to 
        actually send an email to ourselves with the data submitted by the user.
    </p>
</div>

<h3>Sending Email with smtplib</h3>
<div style="font-size:1.2em">
    <p>
        We've learnt how to send email using smtplib already (e.g. Day 32), let's use this knowledge to make the 
        contact form complete and actually send us (website owner) an email when a user is trying to get in touch. 
    </p>
    <p>
        Result: 
    </p>
    <div style="text-align: center;">
        <img src="assets/2.gif" alt="" style="width: 770px;">
    </div>
</div>

https://www.w3schools.com/tags/att_form_method.asp

https://www.w3schools.com/tags/att_form_action.asp