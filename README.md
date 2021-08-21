# `Real Time Numberplate Detection`

## `IEEE Project`


### **By Aayush and Hitanshu**
---

## ```System Setup```

 Create a virtual environment. To create use the commands below on any terminal
- Step 1:          
    ```bash
    pip install virtualenv
    ``` 
- Step 2:
    ```bash
    virtualenv env
    ```
    env is your environment name

- Step 3: To activate the environment
    ```bash
    .\env\Scripts\activate   ### For Windows ###

    source env/Scripts/activate   ### For Unix ###
    ```
    env is your environment name
- Step 4: To install dependencies
    ```bash
    pip install -r requirements.txt
    ```
To install tesseract:
[Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

It is necessary to include tesseract to path in the script

To do so use the command below

``pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'`` 

For haarcascades :
[Haarcascade xml file](https://github.com/opencv/opencv/tree/master/data/haarcascades)

Install the 
    ``haarcascade_russian_plate_number.xml"
    ``
and save it to the folder with the files you are working on for numberplate detection since it works best for deteecting numberplate



- Step 5: Once you are done with setting up a virtual environment, run the file
    ```bash
    python realtime_npd.py
    ```










