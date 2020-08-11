# C1test
C1 technical test

# Instruction to setup
In order to set up the project, follow the next steps:
- Git clone the repository (https://github.com/Chrisart27/C1test.git)
- Set up a Python virtual environment. For information on how to create a virtual environment check the following link: https://docs.python.org/3/library/venv.html
- Activate the new virtual environment
- Execute the following command in a terminal, at the root of the project: ```pip install -r requirements.txt``` 
- Run, at the root of the project ```python manage.py runserver```

# URLS
- ```http://host:port/assessment/start```
    - Creates the user, if not found and starts the assessment
    -  HTTP Method: POST
    - Parameters
        - email: string
        - first_name: string
        - last_name: string
- ```http://host:port/assessment/next```
    - Retrieves the next Question with its answers
    -  HTTP Method: GET
- ```http://host:port/assessment/save```
    - Saves a question with the selected answer, to be called always before requesting the next question
    - HTTP Method: POST
    - Parameters
        - question_id: integer
        - answer_id: integer
- ```http://host:port/assessment/check```
    - Retrieves all the questions and selected answers for a final check before submitting
    - HTTP Method: GET
- ```http://host:port/assessment/end```
    - Submits the assessment
    - HTTP Method: POST
- ```http://host:port/admin```
    - Used to create the questions and their answers
    - superuser:
        - email: admin@admin.com
        - password: admin