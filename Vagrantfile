# -*- mode: ruby -*-
# vi: set ft=ruby :

hosts = {
    "n0" => { "ip" => "192.168.77.10", "netmask" => "255.255.255.0", "cpus" => 2, "memory" => 2048 },
    "n1" => { "ip" => "192.168.77.11", "netmask" => "255.255.255.0", "cpus" => 2, "memory" => 2048 },
    "n2" => { "ip" => "192.168.77.12", "netmask" => "255.255.255.0", "cpus" => 1, "memory" => 1024 },
    "n3" => { "ip" => "192.168.77.13", "netmask" => "255.255.255.0", "cpus" => 1, "memory" => 1024 }
}

admin = { "ip" => "192.168.77.20", "netmask" => "255.255.255.0", "cpus" => 1, "memory" => 512 }

Vagrant.configure("2") do |config|

    config.ssh.insert_key = false
    config.ssh.private_key_path = ["ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]

    config.vm.box = "ubuntu/bionic64"

    hosts.each do |name, data|
        config.vm.define name do |m|
            m.vm.network :private_network, ip: data["ip"], netmask: data["netmask"]
            m.vm.hostname = name
            m.vm.provider "virtualbox" do |v|
                v.name = name
                v.cpus = data["cpus"]
                v.memory = data["memory"]
            end
            m.vm.provision "shell", 
                inline: "cat /vagrant/ssh/id_rsa.pub >> ~/.ssh/authorized_keys",
                privileged: false
        end
    end

    config.vm.define "admin" do |m|
        m.vm.network :private_network, ip: admin["ip"], netmask: admin["netmask"]
        m.vm.hostname = "admin"
        m.vm.provider "virtualbox" do |v|
            v.name = "admin"
            v.cpus = admin["cpus"]
            v.memory = admin["memory"]
        end
        m.vm.provision "shell", 
            inline: "cat /vagrant/ssh/id_rsa.pub >> ~/.ssh/authorized_keys", 
            privileged: false

        m.vm.provision "shell", 
            inline: "cp -f /vagrant/ssh/id_rsa ~/.ssh/id_rsa", 
            privileged: false
        m.vm.provision "shell", 
            inline: "cp -f /vagrant/ssh/id_rsa.pub ~/.ssh/id_rsa.pub", 
            privileged: false

        m.vm.provision "shell", 
            inline: "echo -e '[defaults]\nhost_key_checking = False' > ~/.ansible.cfg",
            privileged: false

        m.vm.provision "shell", 
            inline: "apt-get update && apt-get install -y python-pip"
        m.vm.provision "shell", 
            inline: "pip install ansible", 
            privileged: false

        m.vm.provision "shell", 
            inline: "ansible-playbook -i /vagrant/hosts.ini -v /vagrant/playbook.yaml", 
            privileged: false

        m.vm.provision "shell", 
            inline: "ansible-playbook -v /vagrant/playbook-local.yaml", 
            privileged: false
    end
end
