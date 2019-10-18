# Test Kubernetes playground

Here I'm tring play around with _Kuberenets_ on _Vagrant_ virtual machines (_Virtualbox_ only): setup cluster, deploy monitoring service, database, custom applications, etc.

## How to Run

* Required software:
    * _VirtualBox_ (https://www.virtualbox.org/wiki/Downloads)
    * _Vagrant_ (https://www.vagrantup.com/downloads.html)
    * _Git_
* Open command line, select directory and execute:
    * ```git clone https://github.com/nazarii-piontko/test-k8s-playground.git```
    * ```cd test-k8s-playground```
    * ```vagrant up```
* Wait untill it finish.
* Add the following into your hosts file (```/etc/hosts``` or ```c:\Windows\System32\Drivers\etc\hosts```):
    * ```192.168.77.12 prometheus.k8s.local```
    * ```192.168.77.12 grafana.k8s.local```
    * ```192.168.77.12 api.k8s.local```

## What you get

There are three services/resources publicly availabe:

* Prometheus: http://prometheus.k8s.local
* Grafana: http://grafana.k8s.local
    * Login: _admin_
    * Password: _admin_
* Dummy REST API service written in _Python_ with _Falcon_ framework:
    * Base URI: http://api.k8s.local
    * POST request to add body string into MongoDB: ```curl -X POST --data "Test Record" http://api.k8s.local```
    * GET request to get latest 10 records: ```curl http://api.k8s.local```
    
