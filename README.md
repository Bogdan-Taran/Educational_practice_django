# A test project to create a local library.
To launch the website, follow these instructions

- Download the project using **zip**

- Transfer to a folder where only Latin characters are found in the path, for example:
`C:\Programming\DCIC\Educational_practice\project_deployment`

- Unzip the archive. Delete the archive. Moving the directory from the folder to the directory above. It should look like this:
`C:\Programming\DCIC\Educational_practice\project_deployment\Educational_practice_django-practical_work_1_1`

And the structure is like this:
```catalog/
locallibrary/
tmplates/
manage.py
...
```

- Open the 
Educational_practice_django-practical_work_1_1 project in the IDE
- Create a virtual environment through the terminal:

*Windows*:
```powershell
python -m venv env  
```
*Ubuntu*
```bash
sudo apt install python3-venv
python3 -m venv venv
```

*Windows*
And activate env:
```powershell
env\Scripts\activate
```

```bash
source venv/bin/activate
```

- Let's check if python is updated:
  
*Windows*
```poweshell
python --version
```

*Ubuntu*
```bash
python3 --version
```

If not installed, download:

*Windows:*
https://www.python.org/downloads/windows/
When installing, BE SURE to check the box "Add Python to PATH"

*Ubuntu:*
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
```
On Ubuntu, the python command may not be available — use python3 and pip3


- Install Django and packages via requirements.txt:

*Windows, Ubuntu:*
```bash
pip install -r requirements.txt
```
Let's check the installation:
```bash
python -m django --version
```

- Launching the project:
```bash
python manage.py runserver
```

Done. The locallibrary website is working.

Here are some users with data that can work in the application:
```bash
Admin:
Bogdan
taranbogdan9.2@mail.ru
usefulDjango
```
```bash
User:
egormur
thisIsLibrary1
```
```bash
Employeer:
marina_ivanovna_lib
LibraryMember_1A test project to create a local library.
```
