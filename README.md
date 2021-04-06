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

### Move into the csc415/expert_system directory
```bash 
$ cd csc415/expert_system
```

### Create a Virtual Environment 

- if you're on a mac or Linux machine, do
```bash 
$ python3 -m venv venv
$ source venv/bin/activate
```
- idk know how to do this on Windows (you can google it though!)

### Install Django 
For mac, Linux, and Windows 
```bash 
$ pip install django 
```

### Run the server 

```bash 
$ cd expert_system
$  python manage.py runserver
```

### Open your browser and use the application

```bash
 http://localhost:8000/app
```
