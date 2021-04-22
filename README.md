## **Cropping Face Images**

Crop the faces from images in a directory and save them to another directory by using this code.
For finding faces [face-recognition](https://github.com/ageitgey/face_recognition) has been used. 



### **Steps to Follow**

**On Windows**

* Clone the project and open it with your IDE
  
* In the project folder run the below commands to create a virtual environment and activate it:
    
        mkdir venv
        cd venv
        python -m virtualenv .
        cd..
        .\Scripts\activate
  
* Install the libraries imported in main.py
      
        pip install Pillow
        # if you get errors while installing below package, you should check the dependency packages via the link given above and try manually installing them
        pip install face-recognition  
  
* Change the paths of image folders as the paths of your image folders
  
* Finally run:

        python main.py
        