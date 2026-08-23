# Python Tetris Container Info (By WMTOLLEY) :


## Coming Soon:
- GAMEOVER Screen


## To Clone Repo:

1. If you don't already have Visual Studio Code (VSCode), download it to your computer. (https://code.visualstudio.com/)
1. If you don't already have DockerDesktop, download it to your computer. (https://docs.docker.com/desktop/)
1. Open DockerDesktop
1. Open VSCode and click "File" -> "Open Folder" and select the folder you want as your project's parent.
1. Run: `git clone https://github.com/WMTolley/Tetris_Container_Example.git`
1. Click "File" -> "Open Folder" and select the created folder.
1. If using windows immedietely run `git stash` after cloning to reverse WindowOS's changes.
1. Press: `Ctrl + Shift + P`
1. Click Dev Containers: Reopen in Container
1. Creates Dev Container, first time took me 74.7 seconds
1. Once thats loaded run `cp .env.example .env` and change the third line to: "LOCALHOST=3005"


## To Reopen Container (Once you've already started the project):

1. Open DockerDesktop
1. Open VSCode and click "File" -> "Open Folder" and select this project's folder.
1. Press: `Ctrl + Shift + P`  
1. Clicked Dev Containers: Reopen in Container  
1. Should take less than 30 seconds  


## To Rebuild Container (Rebuilds Cache):

1. Open DockerDesktop
1. Open VSCode and click "File" -> "Open Folder" and select this project's folder.
1. Press: `Ctrl + Shift + P`
1. Clicked Dev Containers: Rebuild Container Without Cache  
1. Should take a little more than 1 minute  


## Walk Through:

### For a basic view:
Run `tree --charset=ascii`  
Or Run `tree -a --charset=ascii`  
Or Run `tree -a -f --charset=ascii`  
### For each file:
- **.devcontainer/**: &emsp;Handles the Dev container.  
- **data/**: &emsp;To store any *.csv, *.json, or database files, now a placeholder.  
- **src/**: &emsp;Contains the actual project. Including the file "server.py" which is where the project will start when running with `python -m src.project.server`. Also contains the *.svg and *.html files.  
- **tests/**: &emsp;Contains the tests of the project, separated from src since the client doesn't need them when the project is deployed.  
- **.env**: &emsp;The Environmental Variables we are using and for security shouldn't be shared (Not included from remote repository, will have to create your own based off of .env.example).  
- **.env.example**: &emsp;When the project is deployed this file will include all the necessary Environmental Variables the user will need to have in their .env file.  
- **.gitignore**: &emsp;The files that shouldn't be shared when uploaded with git.  
- **Dockerfile**: &emsp;The Dockerfile the user will use without the unnecessary development features.  
- **Makefile**: &emsp;Automates frequent processes, using the `make` command-line tool.  
- **play_tetris.sh**: &emsp;Bash file that can be run with the command `./play_tetris.sh` to easily run the project.  
- **pyproject.toml**: &emsp;Configuration file for this python project. Included to support the lint tool.  
- **README.md**: &emsp;What you are reading right now, or at least the preview of.  
- **requirements.txt**: &emsp;The libraries the user will need to install.  
- **run_pylint.sh**: &emsp;Bash file that can be run with the command `./run_pylint.sh` to easily run pylint.  
- **run_pytest.sh**: &emsp;Bash file that can be run with the command `./run_pytest.sh` to easily run pytest.  
- **WebDesign-SVG-TetrisPythonContainer.svg**: &emsp;SVG icon used to identify project.  


## Troubleshooting:

1. Currently the .env file isn't included in the remote repository, so once you've cloned/forked this repo run: `cp .env.example .env` then provide each of the variables listed now in .env with a valid value (For example LOCALHOST=3005)  

1. **If you get the error: failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.**  
Just opening the Docker Desktop application fixes this error.  
  
1.  **If you wish to add/remove python libraries from requirements.txt to only include whats necessary, I recommend the command:**  
`pipdeptree --warn silence | grep -E '^\w+' > requirements.txt`  

1. **In case you want to remove all python libraries, I would recommend the command:**   
`pip freeze | xargs pip uninstall -y`  

1. **If you ever need to redownload the python librarires manually:**  
While in the root/code directory  
Run `pip install -r requirements.txt`  


## Notes:

### To Create a New Basic Container:
1. Create .devcontainer directory  
1. Create devcontainer.json file (can use code we used)  
1. Create Dockerfile.dev file (can use code we used)  
1. Open DockerDesktop  
1. In VSCode Press: `Ctrl + Shift + P`  
1. Click Dev Containers: Reopen in Container  
1. Creates Dev Container, first time took me 74.7 seconds  
1. If the root/code directory doesn't contain a file named .env:  
    1. Edit .env.example by adding random text after the two first equal signs  
    1. Rename .env.example as .env  

### To Run Project:
1. While in the root/code directory  
1. Run either `make run` or `./play_tetris.sh` or `python -m src.project.server`  
1. Should Output:  
    &emsp;&emsp;Running Code  
    &emsp;&emsp;python -m src.project.server  
    &emsp;&emsp;INFO:&emsp;&emsp;Started server process [3997]  
    &emsp;&emsp;INFO:&emsp;&emsp;Waiting for application startup.  
    &emsp;&emsp;INFO:&emsp;&emsp;Application startup complete.  
    &emsp;&emsp;INFO:&emsp;&emsp;Uvicorn running on http://0.0.0.0:3005 (Press CTRL+C to quit)  
1. Open in a web browser the URL: "http://Localhost:3005", changing the value of the environmental variable "LOCALHOST" changes the port value.  
1. This page should link to two others (which you can open in other windows):
    1. Controller
    1. Display
1. Play Tetris!

### To Test Project:
1. While in the root/code directory  
1. You can run the command `./run_pytest.sh` or to do it manually with `python -m pytest`  
1. For code coverage run: `python -m pytest --cov=src --cov-report=term-missing --cov-branch`  
1. For an html report:  
    1. Run `python -m pytest --cov=src --cov-report=html --cov-branch`  
    1. Run `python -m http.server 8080 --directory htmlcov`  
    1. In a browser go to: http://localhost:8080/  
1. To run the tests and view any results run: `make test-dx`  

### To Statically Analyze Code:
1. While in the root/code directory  
1. You can run the command `./run_pylint.sh` or to do it manually:   
    1. Run `pylint src`  
    1. If you wish to instead analyze the test files code run `pylint tests`  
    1. To instead output in the form of a JSON object to a file run:  
        `pylint --output-format=json . > pylint.coverage`  
1. This should list the detected flaws for each file, also listing the line number of the problem, which should look like this (if there are any):  
    &emsp;&emsp;Running static analysis...  
    &emsp;&emsp;./run_pylint.sh  
    &emsp;&emsp;************* Module server  
    &emsp;&emsp;src/project/server.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)  
    &emsp;&emsp;src/project/server.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)  
    &emsp;&emsp;src/project/server.py:48:9: W1514: Using open without explicitly specifying an encoding &emsp;&emsp;(unspecified-encoding)  
    &emsp;&emsp;src/project/server.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)  
    &emsp;&emsp;src/project/server.py:54:9: W1514: Using open without explicitly specifying an encoding &emsp;&emsp;(unspecified-encoding)  
    &emsp;&emsp;src/project/server.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)  
    &emsp;&emsp;src/project/server.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)  
    &emsp;&emsp;src/project/server.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)  
    &emsp;&emsp;src/project/server.py:76:15: W0718: Catching too general exception Exception (broad-exception-caught)  
    &emsp;&emsp;src/project/server.py:85:0: C0116: Missing function or method docstring (missing-function-docstring)  
    &emsp;&emsp;src/project/server.py:100:11: W0718: Catching too general exception Exception (broad-exception-caught)  
1. At the bottom seperated by a horizontal line should be a rating of your code, for example:  
    &emsp;&emsp;"Your code has been rated at 8.00/10 (previous run: 8.00/10, +0.00)"  

### When Delivering:
* **Libraries**:  
    Since this is a python project, run `pipdeptree --warn silence | grep -E '^\w+' > requirements.txt`  
    This will create a file named requirements.txt listing all the libraries installed, like Dotenv, Pylint, and Websockets.  
    The client will need this file and to run `pip install -r requirements.txt` (this is done already with the dev container, but can also be done manually) to install all the libraries you have.  
    If you get the warning that starts with "WARNING": Running pip as the 'root' user" and you want to use a virtual environment then. Run the following three commands for a virtual environment:   
            &emsp;&emsp;python -m venv venv (Creates the isolated environment)  
            &emsp;&emsp;source venv/bin/activate (Activates it—on Windows use venv\Scripts\activate)  
            &emsp;&emsp;pip install -r requirements.txt (Installs everything safely)  
* **System Dependencies**:  
    In Dockerfile.dev look for a line with `apt-get install`  
    Make sure your project will actually rquire these tools, and they aren't just for development.  
    If the client is using docker, include all these in the production Dockerfile.  
    Otherwise inform them to install these tools on their OS.  
* **Environment Variables**:  
    Check for any environmental variables, they might be in devcontainer.json, a *.env file in the root folder, or Dockerfile.dev, or anywhere else. They will probably be labedl as "ENV"  
    Provide a env.example file so the client knows which variables they need to set up on their end.  
    The client should copy .env.example to a new file named .env and fill in their own values. 
    This project is configured to ignore the actual .env for security  
* **Production DockerFile**:  
    "./Dockerfile" is included to remind you to create a production Dockerfile, the contents of this file and the process you use to deploy it will depend widely on your project.  


## Sources / Additional Resources:

"WebSockets and Real-Time Applications"  
by Emily Elim  
https://emily-elim04.medium.com/building-real-time-apps-using-websockets-dc137ccdd34b  
https://emily-elim04.medium.com/  

"ABOUT TETRIS"  
by Tetris  
https://tetris.com/about  
https://tetris.com/  

"Tetris"  
by Tetris  
https://play.tetris.com/  
https://tetris.com/  

"Understanding align-content , align-items, and align-self:"  
by Ugwuanyi Chibuikem Christian  
https://medium.com/@chrisroyalty001/understanding-css-align-content-align-items-and-align-self-998b7db0ec6a  
https://medium.com/@chrisroyalty001  

"WebSocket API (WebSockets)"  
by Mozilla.org Contributors  
https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API  
https://developer.mozilla.org/en-US/  

"CSS: Styling the content"  
by Mozilla.org Contributors  
https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Styling_the_content  
https://developer.mozilla.org/en-US/  

"Development or Dev Containers in 5 minutes"  
by COMMAND  
https://www.youtube.com/watch?v=Un2Nw00oL2s  
https://www.youtube.com/@cmd_labs  

"Docker Desktop"  
by DockerDocs  
https://docs.docker.com/desktop/  
https://www.docker.com/products/docker-desktop/  

"Basic CSS 02 — CSS Layouts (Flexbox, Positioning, Margin/Padding)"  
by Juwono (ジュウｵノ)  
https://medium.com/@unosega/basic-css-02-css-layouts-flexbox-positioning-margin-padding-8fd4d86208d4  
https://medium.com/@unosega  

"CSS Box Model"  
by w3schools  
https://www.w3schools.com/css/css_boxmodel.asp  
https://www.w3schools.com/  

"Developing in Python with Dev Containers — Part 1: Setup"  
by Andy Pickup  
https://andypickup.com/developing-in-python-with-dev-containers-part-1-setup-f1aeb89cbfed  
https://andypickup.com/  

"Setting A Dockerized Python Environment — The Elegant Way"  
by Rami Krispin  
https://medium.com/data-science/setting-a-dockerized-python-environment-the-elegant-way-f716ef85571d  
https://medium.com/@rami.krispin  

"Create a Dev Container"  
by Visual Studio Code  
https://code.visualstudio.com/docs/devcontainers/create-dev-container  
https://code.visualstudio.com/  
