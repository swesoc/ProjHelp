### Prerequisites (Backend)

Install a recent Python 3 interpreter to run the Flask Backend on. To install Python, go to [install Python](https://www.python.org/). To confirm if locally installed, enter into the terminal
```shell
python3 --version
```
To install Flask, enter into the terminal
```shell
pip install flask python-dotenv


pip install flask-sqlalchemy
pip install marshmallow-sqlalchemy

```

Setps to run the project

1. If you haven't cloned the project, open the terminal and in the desired directory, run
```shell
  git clone https://github.com/swesoc/Project.git
```
  to clone this project repository to the local machine.

2. Once cloned, in the terminal run
```shell
  cd Project/API
```
  and create a virtual environment called `venv`, by entering (for Unix-based operating systems)
```shell
  $ python3 -m venv venv
  $ source venv/bin/activate
```
  and you will get the terminal as `(venv) $ `
  If you are using Windows, then you will do this instead:
```shell
  $ python -m venv venv
  $ venv\Scripts\activate
```

3. To get started, in `Project/API` run
   ```shell
    flask run
   ```
   to start the Flask development server. To stop the Flask server press Ctrl-C.

4. Visit api of the project locally at `http://localhost:5000/`
