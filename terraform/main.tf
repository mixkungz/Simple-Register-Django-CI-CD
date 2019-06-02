provider "google" {
  credentials = "${file("account.json")}"
  project     = "pronto-242401"
  region      = "asia-southeast1"
  zone        = "asia-southeast1-b"
}
