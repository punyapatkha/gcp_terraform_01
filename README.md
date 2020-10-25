# gcp_terraform_01
![alt text](https://github.com/punyapatkha/gcp_terraform_01/blob/main/bi_req_script-Page-3.jpg)


Create compute engine and CloudSQL for store data from API


1.Set up Terraform binary on local https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/gcp-get-started

2.Register for Binance API and get token

3.Create gcp project enable CloudSQL API & create service account key

4.Config project name and service account key in main.tf

5.Run Terraform plan to show current plan

6.Run Terraform apply to create infastruture 

7.SSH into VM install git and pull this repository


    $sudo apt-get install git-core 
    or
    $sudo apt-get install git -y
    $git clone https://github.com/punyapatkha/gcp_terraform_01.git
    $cd gcp_terraform_01


8.Run bash script in VM
    
    $sudo bash bashfile1

9.Config database IP,Binance API Token,service account.json in test_1.py

10.Run following command to set cronjob

    $sudo echo '0 * * * * root cd /home/punyapat_kha/gcp_terraform_01 && python3 test_1.py' >> /etc/crontab
    
 --------------------------------------------------------------------------------------
 
 on develop
 script for initialize table in database
 
