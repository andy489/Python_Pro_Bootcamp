# Git, Github and Version Control
## Git and Github: Introduction to a powerful Version Control System (VCS)

<div style="font-size: 1.2em">
    <h3>FlapPyBird</h3>
    <div>
        <p>
            The entire implementation of flappy bird, and you can run it, or you can also look through
            their code base to see how they did this.
        </p>
        <ul>
            <li>
                <a href="https://github.com/sourabhv/FlapPyBird">
                    https://github.com/sourabhv/FlapPyBird
                </a>
            </li>
        </ul>
    </div>
    <h3>Gitignore</h3>
    <div>
        <p>
            A pre-made collection of useful .gitignore templates made by the GitHub team.
        </p>
        <ul>
            <li>
                <a href="https://github.com/github/gitignore">
                    https://github.com/github/gitignore
                </a>
            </li>
        </ul>
    </div>
    <h3>Cloning</h3>
    <div>
        <p>
            A list of Free Software network services and web applications which can be hosted on your own servers
        </p>
        <ul>
            <li>
                <a href="https://github.com/awesome-selfhosted/awesome-selfhosted">
                    https://github.com/awesome-selfhosted/awesome-selfhosted
                </a>
            </li>
        </ul>
        <h4>Quake III Arena</h4>
        <p>
            Did you know that you can run the original <b>"Quake III Arena"</b> video game in your web browser?
            It's entirely built in JavaScript
        </p>
        <ul>
            <li>
                <a href="https://github.com/inolen/quakejs">https://github.com/inolen/quakejs</a>
            </li>
        </ul>
        <p>Here is how to do it.</p>
        <ol>
            <li>Write: <code>git clone https://github.com/inolen/quakejs.git</code> in your terminal.</li>
            <li>Once it gets loaded to your own computer: <code>cd quakejs</code></li>
            <li>Install the required node.js modules:<code>npm install</code></li>
            <li>Set <code>content.quakejs.com</code> as the content server: <code>echo '{"content": "content.quakejs.com" }' > bin/web.json</code></li>
            <li>Run the server: <code>node bin/web.js --config ./web.json</code></li>
            <li>Your server is now running on: <a href="http://0.0.0.0:8080">http://0.0.0.0:8080</a></li>
        </ol>
        <h4>Wordle</h4>
        <p>
            Wordle is basically a word game where you have to guess a five-letter word using just six tries.
            It went completely viral a years ago, and eventually got bought by the New York Times. And the
            official Wordle is now accessed at the New York Times alongside all of their different crosswords 
            and puzzles.
        </p>    
        <ul>
            <li>
                <a href="https://www.nytimes.com/games/wordle/index.html">
                    https://www.nytimes.com/games/wordle/index.html
                </a>
            </li>
        </ul>
        <p>
            But somebody has created all the code for Wordle, and we can clone it and run it 
            on our own system.
        </p>
        <ul>
            <li>
                <a href="https://github.com/ritik48/Wordle-Game">
                    https://github.com/ritik48/Wordle-Game
                </a>
            </li>
        </ul>
        <p>
            You can see it's entirely created in Python and uses Tkinter.
        </p>
        <h4>Awesome for Beginners</h4>
        <p>A list of awesome beginners-friendly projects.</p>
        <ul>
            <li>
                <a href="https://github.com/MunGell/awesome-for-beginners">
                    https://github.com/MunGell/awesome-for-beginners
                </a>
            </li>
        </ul>
    </div>
    <h3>Branching and Merging</h3>
    <div>
    </div>
    <h3>Diving deeper into Git</h3>
    <div>
        <p>Learning about Cherry-Picking, Git Rebase and more:</p>
        <ul>
            <li>
                <a href="https://learngitbranching.js.org/">
                    https://learngitbranching.js.org/
                </a>
            </li>
        </ul>
    </div>
    <h3>Forking and Pull Requests</h3>
    <h4>Creating a Branch, Working on It, and Merging Changes from Main</h4>
    <p>Here's a step-by-step guide to Git branch workflow:</p>
    <ol>
        <li><b>Create a New Branch</b></li>
        <p>First, make sure you're starting from the main branch (sometimes called "master"):</p>
        <p><code>git checkout main</code></p>
        <p><code>git pull origin main  # Ensure you have the latest changes</code></p>
        <p>Now create and switch to your new branch:</p>
        <p><code>git checkout -b feature/new-feature</code></p>
        <li><b>Work on Your Branch</b></li>
        <p>Make your changes, commit them regularly:</p>
        <p><code># After making changes</code></p>
        <p><code>git add .</code></p>
        <p><code>git commit -m "Implement new feature X"</code></p>
        <p>Push your branch to remote (optional but recommended):</p>
        <p><code>git push -u origin feature/new-feature</code></p>
        <li><b>Merge Changes from Main into Your Branch</b></li>
        <p>While working, you may want to incorporate updates from main:</p>
        <p><code>git fetch origin  # Get latest changes from remote</code></p>
        <p><code>git merge main    # Merge main into your current branch</code></p>
        <p>If there are conflicts, resolve them, then:</p>
        <p><code>git add .         # Mark conflicts as resolved</code></p>
        <p><code>git commit        # Complete the merge</code></p>
        <li><b>Continue Working</b></li>
        <p>Repeat the process of making changes and committing:</p>
        <p><code>git add .</code></p>
        <p><code>git commit -m "Add more functionality to feature X"</code></p>
        <li><b>Final Merge Preparation</b></li>
        <p>Before merging back to main, ensure your branch is up to date:</p>
        <p><code>git fetch origin</code></p>
        <p><code>git merge main    # Merge latest main changes one more time</code></p>
        <li><b>Merge Your Branch into Main</b></li>
        <p><code>git checkout main</code></p>
        <p><code>git merge feature/new-feature</code></p>
        <p><code>git push origin main</code></p>
        <p><b>Alternative: Using Rebase Instead of Merge</b></p>
        <p>Some teams prefer rebasing to keep history linear:</p>
        <p><code>git checkout feature/new-feature</code></p>
        <p><code>git fetch origin</code></p>
        <p><code>git rebase main   # Instead of merge</code></p>
        <p>This replays your branch commits on top of main.</p>
        <p>Remember to regularly merge/rebase from main to avoid large merge conflicts later!</p>
    </ol>
    <h3>Git Cheat Sheet</h3>
    <ul>
        <li>
            <a href="./assets/git_cheat_sheet.pdf">
                git_cheat_sheet.pdf
            </a>
        </li>
    </ul>
</div>
