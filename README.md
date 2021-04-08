# Breast cancer expert system using the Breast Cancer Wisconsin (Diagnostic) Data Set


## How to use 

### Setup Python 3

If you don't have python installed on your machine, you can install it like so:

- if you're on a mac, just do

```bash
$ brew install python
```

- if you're on Linux, do
```bash 
$ sudo apt install python3-venv python3-pip
```
- if you're on Windows, you'd have to download Python directly from [here](https://www.python.org/downloads/windows/) 

### Clone this git repository (dowload the code)

```bash
$ git clone https://github.com/ebresafegaga/csc415
```

### Move into the csc415/ directory
```bash 
$ cd csc415/
```

### Create a Virtual Environment (Not required, but recommended)

- if you're on a mac or Linux machine, do
```bash 
$ python3 -m venv venv
$ source venv/bin/activate
```
- idk know how to do this on Windows (you can google it though!)

### Install Django and Sklearn-Kit
For mac, Linux, and Windows 
```bash 
$ pip install django 
$ pip install sklearn
```

### Train the Model and serialize to disk 
- Open Jupyter Notebooks in the currect directory
```bash 
$ jupyter notebook
```
- Run all the code in the notebook

### Copy the trianed ML model to the expert_system/app directory
- If you're on a mac or Linux, just run this on your terminal
```bash 
$ chmod +x move.sh
$ ./move.sh
```

- If you're on Windows, copy it to that folder yourself 

### Run the server 

```bash 
$ cd expert_system
$ python manage.py runserver
```

### Open your browser and use the application

```bash
 http://localhost:8000/app
```
