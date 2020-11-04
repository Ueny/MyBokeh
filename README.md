# MyBokeh
DSCI560-HW5

MyBokeh aims to do a visualization on the *cdph-race-ethnicity.csv* and *latimes-state-totals.csv* data. Through the Bokeh, we have the visualization of new confirmed coronavirus cases in California. Also, we have visualizations for *confirmed cases percent and population percent by race*, and *deaths percent and population percent by race*. 

# The steps to install and run the visualization
###(Note: please run the steps on the Mac OS)

## step 1: create a virual environment
  - Install the environment management tool. Run the command in your terminal *pip install virtualenv*
  - Create a new virtual environment called 'DSCI560HW5'. Run the command in your terminal *virtualenv DSCI560HW5*
  - Activate this virtual environment. Run the command in your terminal *source DSCI560HW5/bin/activate*
  ![image](https://user-images.githubusercontent.com/54614822/98071936-b71bcc00-1e19-11eb-8887-958977ee03a1.png)
  
## Step 2: install the required packages
  - Download the *requirements.txt* file and install the required packages in your virtual environment. Run the command in your terminal *pip install -r requirements.txt*
  
## Step 3: run the *resulting.py* file, doing the visualization
  - Download the data files and the *resulting.py* file, and run the command in your terminal *Bokeh serve --show resulting.py*
