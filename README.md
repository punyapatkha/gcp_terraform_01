# gcp_terraform_01
Create compute engine and cloud sql for store data from api

1.set up terraform binary on local https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/gcp-get-started

2.create gcp project enable cloudsqlapi & create service account key

2.5 config project name as service account key in main.tf

3.run terraform plan to show current plan

4.run terraform apply to create infastruture 

5.ssh into vm git pull this repository config serviceacouuntkey.json and project name


    sudo apt-get install git-core 
    or
    sudo apt-get install git -y
    git clone https://github.com/punyapatkha/gcp_terraform_01.git
    cd gcp_terraform_01


6.run bash script to initialize table in database and deploy script in cronjob

