# the_internet

First of all, you can clone the repository by running on your terminal (Powershell on Windows) the following command:

```
git clone https://github.com/jmatheuscdias/the_internet.git
```
Then, procceed to the following steps

## Setup and running

### Step 1: Install Python

Make sure you have Python installed on your machine. You can check if Python is already installed by running on your terminal the following command:

```
python --version
```

If Python is already installed, the terminal will display the installed version. Otherwise, if you receive a response somewhat like "command not found: python", you probably don't have it installed. If so, you can download it from the <a href="https://www.python.org/downloads">Python Official Website</a>.

### Step 2: Running the Python Virtual Environment

On a terminal, find the repository's root folder. There, you'l need to run the following command to activate the <a href="https://docs.python.org/3/library/venv.html">Python Virtual Environment</a> with the test dependencies already installed

```
source venv/bin/activate
```

### Step 3: Run the Test

From the root folder, run the following command:

```
pytest tests/web/drag_and_drop/success/home.py -s
```
> The -s flag is an alias to the flag --capture=no, which lets 'print' statements be displayed on console. It shouldn't have any other impact on the test.
