# gcp_terraform_01
![alt text](https://github.com/punyapatkha/gcp_terraform_01/blob/main/bi_req_script-Page-3%20(1).png)


Create Compute Engine and CloudSQL for store data from Binance API using Terraform and Bash Script


1.Set up Terraform binary on local https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/gcp-get-started

2.Register for Binance API and get token https://www.binance.com/en/support/articles/360002502072

3.Create GCP project enable CloudSQL API & create service account key

4.Config project name and service account key in main.tf

5.Run Terraform plan on your local to show current plan

    Terraform plan

6.Run Terraform apply on your local to create infrastructure 

    Terraform apply
    
7.SSH into Ubuntu VM ( Compute Engine ) install git and pull this repository


    $sudo apt-get install git-core 
    or
    $sudo apt-get install git -y
    
    $git clone https://github.com/punyapatkha/gcp_terraform_01.git
    $cd gcp_terraform_01


8.Run Bash script in VM
    
    $sudo bash bashfile1

9.Config database IP,Binance API Token in test_1.py

    $nano test_1.py

10.Run following command to set cronjob (change username to yours)

    $sudo echo '0 * * * * root cd /home/punyapat_kha/gcp_terraform_01 && python3 test_1.py' >> /etc/crontab
    
 --------------------------------------------------------------------------------------
 
 On Developing
 
    1.Script for initialize table in database
    2.Installation Testing
