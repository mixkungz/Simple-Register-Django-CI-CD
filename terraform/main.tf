provider "google" {
  credentials = "${file("account.json")}"
  project     = "pronto-242401"
  region      = "asia-southeast1"
  zone        = "asia-southeast1-b"
}

resource "google_compute_instance" "tf_instance" {
  name          = "tf-instance"
  machine_type  = "n1-standard-1"

  boot_disk {
    initialize_params {
      image     = "ubuntu-1804-bionic-v20190530"
      size      = 30
    }
  }

  metadata = {
    sshKeys = "pcr.mixkungz:${file("~/.ssh/id_rsa.pub")}"
  }

  network_interface {
    network = "default"
    access_config {}
  }

  tags = ["my-webs"]
}
