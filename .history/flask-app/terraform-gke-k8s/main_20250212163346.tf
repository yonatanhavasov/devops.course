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

# Create a GKE cluster, no need to specify initial node count, no need to specify project.
resource "google_container_cluster" "primary" {
  name               = "yoni-flask-cluster"
  location           = var.region
  initial_node_count = 1

  deletion_protection = false
  remove_default_node_pool = true

  network    = "default"
  subnetwork = "default"

  logging_service    = "logging.googleapis.com/kubernetes"
  monitoring_service = "monitoring.googleapis.com/kubernetes"

  addons_config {
    http_load_balancing {
      disabled = false
    }
  }
}

# Create a node pool with auto-scaling enabled
resource "google_container_node_pool" "primary_nodes" {
  name     = "yoni-node-pool"
  cluster  = google_container_cluster.primary.name
  location = var.region
  node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 15
    disk_type    = "pd-standard"
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }

  management {
    auto_upgrade = true
    auto_repair  = true
  }
  
  # Ensure that the cluster is created before the node pool.
  depends_on = [ google_container_cluster.primary ]
}