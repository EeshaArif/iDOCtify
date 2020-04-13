# iDOCtify
_iDOCtify is an extended feature of [Patientio](https://github.com/EeshaArif/Patientio)._
#### Introduction:
iDOCtify efficiently displays records of patients by finding them through face recognition.

This web Application integrates [OpenCV](https://opencv.org/) in Django. The face recognition code can be found in [views.py](myapp/views.py).
#### Execution:
Run the following command in the root folder.

`$python manage.py runserver`
#### Admin Credentials:
- __Username:__ eesha
- __Password:__ django123
#### Face Recognition:
Follow the following steps:
1. Add the patient. 


![main-page](https://github.com/EeshaArif/iDOCtify/blob/master/Screenshot%20(268).png)


2. Upload a reference image for the application to identify the person. 


![Reference image upload](https://github.com/EeshaArif/iDOCtify/blob/master/Screenshot%20(269).png)
###### You must be logged in as an admin to perform the above step. 

3. Go back to the main page and start detection:

![detecting image](https://github.com/EeshaArif/iDOCtify/blob/master/Screenshot%20(270).png)
###### Press **"q"** on the keyboard while the frame is being shown.

4. The application displays the saved record.

![Records-displayed](https://github.com/EeshaArif/iDOCtify/blob/master/Screenshot%20(271).png)
