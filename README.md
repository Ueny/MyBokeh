# MyBokeh
DSCI560-HW5

MyBokeh aims to do a visualization on the *cdph-race-ethnicity.csv* and *latimes-state-totals.csv* data. Through the Bokeh, we have the visualization of new confirmed coronavirus cases in California. Also, we have visualizations for *confirmed cases percent and population percent by race*, and *deaths percent and population percent by race*. You are able to have a view of the plot by selecting a datetime as you want.

# The steps to install and run the visualization
### (Note: please run the steps on the Mac OS)

## step 1: create a virual environment
  - Install the environment management tool. Run the following command in your terminal
    `pip install virtualenv`
  - Create a new virtual environment called 'DSCI560HW5'. Run the following command in your terminal
    `virtualenv DSCI560HW5`
  - Activate this virtual environment. Run the following command in your terminal
     `source DSCI560HW5/bin/activate`
  ![image](https://user-images.githubusercontent.com/54614822/98071936-b71bcc00-1e19-11eb-8887-958977ee03a1.png)
  
## Step 2: install the required packages
  - Download the *requirements.txt* file and install the required packages in your virtual environment. Run the following command in your terminal 
     `pip install -r requirements.txt`
  
## Step 3: run the *resulting.py* file, doing the visualization
  - Download the data files and the *resulting.py* file, and run the following command in your terminal 
     `Bokeh serve --show resulting.py`

# Serving the visualization through Docker
  - Download the Docker first to make sure you have docker installed in your local computer
  - Clone the repository content first, and enter the directory of the folder
     `git clone https://github.com/Ueny/MyBokeh.git`
     `cd MyBokeh`
    ![image](https://user-images.githubusercontent.com/54614822/98190274-898f5b00-1ecb-11eb-9642-b879d9b10872.png)
  - Build the image called *dsci560hw5*
     `docker build --tag dsci560hw5`
    ![image](https://user-images.githubusercontent.com/54614822/98190180-54830880-1ecb-11eb-996c-c94f2903258e.png)
  - You can check your images now by running the following command
     `docker images`
    ![image](https://user-images.githubusercontent.com/54614822/98190140-3f0dde80-1ecb-11eb-9586-f498df46ce53.png)
  - Now you have built your image, and you are able to run it
     `docker run -p 5006:5006 -it dsci560hw5`
    ![image](https://user-images.githubusercontent.com/54614822/98190074-29001e00-1ecb-11eb-8bda-6e2810c351c7.png)
  - Finally once you execute it successfully, you are able to open the link to check the visualization results
     `http://localhost:5006/resulting`
    


# Result examples
![image](https://user-images.githubusercontent.com/54614822/98072965-1ed31680-1e1c-11eb-94a1-05df77d23704.png)
![image](https://user-images.githubusercontent.com/54614822/98073017-3a3e2180-1e1c-11eb-92fb-b9db477adcee.png)
![image](https://user-images.githubusercontent.com/54614822/98073051-4d50f180-1e1c-11eb-81d1-cfde24af1688.png)
