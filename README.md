# CloudComputing
locustfile.py - It contains the configuration of the locust framework used in our code.


plot_csvs.py - Contains the code to plot the following characteristics for all the different cloud computing platforms:
              1) Total Failures vs No. of Clients
              2) Average Latency (in ms) vs No. of Clients
              3) Maximum Latency (in ms) vs No. of Clients
              4) Requests per second handled vs No. of Clients
   
   
plot_plat.py - This file is used to see the behavior anad characteristics of a particular cloud computing platform.


run_script_aws.py - This python script is used to invoke the locust frame work on AWS server. Kindly ensure to up the server before using this file.


run_script_azure.py - This python script is used to invoke the locust frame work on Azure server. Kindly ensure to up the server before using this file.


run_script_gcp.py - This python script is used to invoke the locust frame work on GCP server. Kindly ensure to up the server before using this file.


How to run these script?

Step 1) Setup the server for GCP, AWS and Azure.

Step 2) Specify the IP address of the server on the python script (run_script_aws.py, run_srcipt_azure.py, run_script_gcp.py) and run it.

  Note: The data will be collected in the folder names specified in the python script.
  

Step 3) Specify the output directory of the step 2) in plot_plat.py (or plot_csvs.py).

Step 4) Run plot_plat.py (or plot_csvs.py) to get the desired plots.


