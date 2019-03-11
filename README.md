# Task Manager

## Installation

- Clone this repository.  
   `git clone https://github.com/dshubhadeep/fsf_2019_screening_task1.git`

- Install **pip** and **pipenv**. These two packages need to be installed globally on your system.

- Go to directory using `cd fsf_2019_screening_task1/`

- Setup a virtualenv with the following command.  
  `pipenv shell`  
  Make sure you are using **Python >=3.5**.

- Go into the project directory and install the dependencies.

```
cd taskmanager/
pipenv install
```

- Create and run the database migrations using the following commands

```
python manage.py makemigrations
python manage.py migrate
```
