# Sample CRUD App
This is a sample CRUD (Create, Read, Update, and Delete) application 
that runs on Google App Engine using Python and Datastore. 

## Overview

### Files
This application uses the following main file structure:

gce-uconn-crud                         <br>
├─ requirements.txt                       <br>
├─ app.yaml                               <br>
├─ main.py                                <br>
├─ templates                                <br>
│  ├── index.html                       <br>
│  ├── customer.html                       <br>
│  ├── create.html                       <br>
│  ├── update.html                       

#### requirements.txt
A list of the required packages for the app

#### app.yaml
A config file for google app engine

#### main.py
The main application

#### templates
HTML files used in the app


## Setup

### 1
Create a new project if needed.

You will be using Datastore Mode, so this will not work in a project with Firestore Native mode 
already enabled.

### 2
Start Cloud Shell

### 3
Pull the Repo

```shell script
git clone https://github.com/philku/gce-uconn-crud.git
```