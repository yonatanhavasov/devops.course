# Security group for the Flask server
resource "aws_security_group" "flask_sg" {
  name        = "flask-sg"
  description = "Allow HTTP and SSH traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 instance for the Flask server
resource "aws_instance" "flask_server" {
  ami           = "ami-0df8c184d5f6ae949" # Updated Amazon Linux 2 AMI
  instance_type = "t2.micro"
  key_name      = var.key_name
  security_groups = [aws_security_group.flask_sg.name]

  # User data script
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y git docker libxcrypt-compat
              systemctl start docker
              systemctl enable docker
              usermod -aG docker ec2-user
              newgrp docker

              # Install Docker Compose (stable version 1.29.2)
              curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose

              # Log Docker and Compose versions for debugging
              docker --version > /var/log/docker-install.log
              docker-compose --version >> /var/log/docker-install.log
              EOF

  # File provisioner for docker-compose.yml
  provisioner "file" {
    source      = "docker-compose.yml"
    destination = "/home/ec2-user/docker-compose.yml"

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("C:/key-gen.pem") # Updated private key path
      host        = self.public_ip
    }
  }

  # File provisioner for Dockerfile
  provisioner "file" {
    source      = "Dockerfile"
    destination = "/home/ec2-user/Dockerfile"

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("C:/key-gen.pem") # Updated private key path
      host        = self.public_ip
    }
  }

  # Remote-exec provisioner to run commands on the instance
  provisioner "remote-exec" {
    inline = [
      "sleep 10",
      "sudo su - ec2-user",
      "sudo chmod +x /home/ec2-user/docker-compose.yml",
      "sudo chown ec2-user:ec2-user /home/ec2-user/docker-compose.yml",
      "sudo chown ec2-user:ec2-user /home/ec2-user/Dockerfile",
      "cd /home/ec2-user",
      "docker-compose build",
      "sleep 20",
      "docker-compose up -d"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("C:/key-gen.pem") # Updated private key path
      host        = self.public_ip
    }
  }

  tags = {
    Name = "Flask-Server"
  }
}

output "public_ip" {
  value = aws_instance.flask_server.public_ip
}
