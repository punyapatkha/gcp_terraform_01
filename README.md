# gcp_terraform_01
![alt text](https://github.com/punyapatkha/gcp_terraform_01/blob/main/bi_req_script-Page-3.jpg)


Create compute engine and cloud sql for store data from api


1.set up terraform binary on local https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/gcp-get-started

2.register for binance api get token

3.create gcp project enable cloudsqlapi & create service account key

4.config project name as service account key in main.tf

5.run terraform plan to show current plan

6.run terraform apply to create infastruture 

7.ssh into vm install git and pull this repository


    sudo apt-get install git-core 
    or
    sudo apt-get install git -y
    git clone https://github.com/punyapatkha/gcp_terraform_01.git
    cd gcp_terraform_01

8.config serviceacouuntkey.json and project name

9.run bash script 

10.run following command to set cronjob
