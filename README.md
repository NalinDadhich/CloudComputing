# CloudComputing
<b>locustfile.py</b> - It contains the configuration of the locust framework used in our code.


<b>plot_csvs.py</b> - Contains the code to plot the following characteristics for all the different cloud computing platforms:
              1) Total Failures vs No. of Clients
              2) Average Latency (in ms) vs No. of Clients
              3) Maximum Latency (in ms) vs No. of Clients
              4) Requests per second handled vs No. of Clients
   
   
<b>plot_plat.py</b> - This file is used to see the behavior anad characteristics of a particular cloud computing platform.


<b>run_script_aws.py</b> - This python script is used to invoke the locust frame work on AWS server. Kindly ensure to up the server before using this file.


<b>run_script_azure.py</b> - This python script is used to invoke the locust frame work on Azure server. Kindly ensure to up the server before using this file.


<b>run_script_gcp.py</b> - This python script is used to invoke the locust frame work on GCP server. Kindly ensure to up the server before using this file.


<b>How to run these script?</b>

<b>Step 1)</b> Setup the server for GCP, AWS and Azure.

<b>Step 2)</b> Specify the IP address of the server on the python script (run_script_aws.py, run_srcipt_azure.py, run_script_gcp.py) and run it.

  <b>Note:</b> The data will be collected in the folder names specified in the python script.
  

<b>Step 3)</b> Specify the output directory of the step 2) in plot_plat.py (or plot_csvs.py).

<b>Step 4)</b> Run plot_plat.py (or plot_csvs.py) to get the desired plots.


