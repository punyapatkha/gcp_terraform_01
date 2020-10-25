terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  version = "3.5.0"

  credentials = file("terraform-293515-4d6d53349361.json")

  project = "terraform-293515"
  region  = "asia-southeast1"
  zone    = "asia-southeast1-b"
}
// double slash for comment in json
// resource "google_compute_network" "vpc_network" {
//  name = "terraform-network"
// }


resource "google_compute_instance" "apps" {
  count        = 2
  name         = "apps-${count.index + 1}"
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1804-lts"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }
}



locals {
  onprem = ["0.0.0.0/0"]
  
}

resource "google_sql_database_instance" "mysql1" {
  name             = "postgres-instance-terraform-02"
  database_version = "MYSQL_5_6"
  region = "asia-southeast1"
  settings {
    tier = "db-f1-micro"

    ip_configuration {
      ipv4_enabled = true
      require_ssl  = false
      dynamic "authorized_networks" {
        for_each = google_compute_instance.apps
        iterator = apps

        content {
          name  = apps.value.name
          value = apps.value.network_interface.0.access_config.0.nat_ip
        }
      }

      dynamic "authorized_networks" {
        for_each = local.onprem
        iterator = onprem

        content {
          name  = "onprem-${onprem.key}"
          value = onprem.value
        }
      }
    }
  }
}

resource "google_sql_user" "mysql-users" {
  name     = "mysql"
  instance = google_sql_database_instance.mysql1.name
  password = "mysql"
}

resource "google_sql_database" "stock-mysqldb" {
  name     = "stock"
// charset  = "UTF8"
//  collation= "en_US.UTF8"
  instance = google_sql_database_instance.mysql1.name
}
