provider "google" {
  project = var.project_id
  region  = var.region
}

terraform {
  backend "gcs" {
    bucket  = "docker-badger-gifs"
    prefix  = "terraform/state"
  }
}

resource "google_container_cluster" "gke_cluster" {
  name     = "flask-gke-cluster"
  location = var.region

  remove_default_node_pool = true
  initial_node_count       = 1

  lifecycle {
    ignore_changes = [initial_node_count]
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "node-pool"
  location   = var.region
  cluster    = google_container_cluster.gke_cluster.name
  node_count = 2

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 30
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}

resource "google_sql_database_instance" "mysql" {
  name             = "flask-db-instance"
  region           = var.region
  database_version = "MYSQL_8_0"

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_user" "users" {
  name     = "flask-user"
  instance = google_sql_database_instance.mysql.name
  password = var.mysql_password
}
