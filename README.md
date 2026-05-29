# 🚀 Kubernetes Training Project – Bekir

This project was created as part of my hands‑on learning journey with Docker and Kubernetes. I built a simple Flask web application, containerized it using Docker, and deployed it on Kubernetes using various core components such as Deployment, Service, ConfigMap, Secret, and Ingress. This repository represents a complete practical example of the steps I followed and the concepts I learned.

---

## 🎯 What I Did in This Project

1. I developed a simple Flask application (`app.py`) and configured it to run on port 8000.

2. I created a Dockerfile and built a Docker image for the application. I tested the container locally using:
   docker build -t bekir-kubernetes-app:1.0 .
   docker run -p 8000:8000 bekir-kubernetes-app:1.0

3. I created a Kubernetes Deployment using `deployment.yaml` to run multiple pods of the application:
   kubectl apply -f deployment.yaml

4. I created a Kubernetes Service using `service.yaml` to expose the application to the outside world:
   kubectl apply -f service.yaml

5. I performed scaling by increasing the number of replicas from 2 to 3 in the Deployment file and applied the changes:
   kubectl apply -f deployment.yaml
   kubectl get pods

6. I created and applied a ConfigMap (`configmap.yaml`) and a Secret (`secret.yml`) to manage configuration values and sensitive data:
   kubectl apply -f configmap.yaml
   kubectl apply -f secret.yml

7. I configured an Ingress using `ingress.yaml` to make the application accessible through a domain and to understand traffic routing:
   kubectl apply -f ingress.yaml

8. I used Git and GitHub for version control. I cleaned up unnecessary files such as `.venv`, created a proper `.gitignore`, and pushed the project to GitHub in a clean and professional structure.

---

## 📂 Project File Structure

.
├── app.py  
├── Dockerfile  
├── requirements.txt  
├── deployment.yaml  
├── service.yaml  
├── configmap.yaml  
├── secret.yml  
├── ingress.yaml  
└── .gitignore  

---

## 🧠 What I Learned

- How to build Docker images and run containers  
- Kubernetes architecture (Pod, Deployment, Service, Ingress)  
- Managing Kubernetes resources using YAML files  
- Scaling applications using replicas  
- Using ConfigMap and Secret for configuration management  
- Version control with Git and GitHub  
- Cleaning unnecessary files from Git (.venv, etc.)  

This project helped me understand the essential building blocks of a real DevOps workflow through practical implementation.

---

## 👤 Developer

Bekir Olsen  
Kubernetes & DevOps Learning Journey



# 🚀 Kubernetes Training Project – Bekir

Bu proje, Docker ve Kubernetes öğrenme sürecimde adım adım uygulayarak geliştirdiğim bir eğitim projesidir. Flask tabanlı bir web uygulamasını Docker ile containerize edip Kubernetes üzerinde çalıştırarak gerçek bir DevOps çalışma akışını deneyimledim. Bu repo, yaptığım tüm adımları, öğrendiğim kavramları ve oluşturduğum Kubernetes yapılarını içeren tam bir çalışma örneğidir.

---

## 🎯 Bu Projede Neler Yaptım?

1. Flask uygulaması geliştirdim. Basit bir app.py dosyası oluşturdum ve uygulamayı 8000 portundan çalışacak şekilde yapılandırdım.

2. Dockerfile oluşturarak uygulamayı container haline getirdim. Image build ettim ve container çalıştırarak test ettim:
   docker build -t bekir-kubernetes-app:1.0 .
   docker run -p 8000:8000 bekir-kubernetes-app:1.0

3. Kubernetes Deployment oluşturdum. deployment.yaml dosyasıyla Kubernetes üzerinde pod’lar oluşturdum:
   kubectl apply -f deployment.yaml

4. Kubernetes Service oluşturdum. service.yaml dosyasıyla uygulamayı dış dünyaya açtım:
   kubectl apply -f service.yaml

5. Scaling yaptım. Deployment içindeki replicas değerini 2’den 3’e çıkardım:
   kubectl apply -f deployment.yaml
   kubectl get pods

6. ConfigMap ve Secret oluşturdum. configmap.yaml ile uygulama ayarlarını, secret.yml ile gizli bilgileri yönettim:
   kubectl apply -f configmap.yaml
   kubectl apply -f secret.yml

7. Ingress yapılandırdım. ingress.yaml dosyasıyla uygulamayı domain üzerinden erişilebilir hale getirdim:
   kubectl apply -f ingress.yaml

8. Git ve GitHub ile versiyon kontrolü yaptım. .venv klasörünü Git’ten temizledim, .gitignore oluşturdum ve projeyi temiz bir şekilde GitHub’a gönderdim.

---

## 📂 Proje Dosya Yapısı

.
├── app.py
├── Dockerfile
├── requirements.txt
├── deployment.yaml
├── service.yaml
├── configmap.yaml
├── secret.yml
├── ingress.yaml
└── .gitignore

---

## 🧠 Bu Projede Ne Öğrendim?

- Docker image oluşturma ve container yönetimi  
- Kubernetes mimarisi (Pod, Deployment, Service, Ingress)  
- YAML dosyalarıyla Kubernetes kaynaklarını yönetme  
- Scaling (replica artırma/azaltma)  
- ConfigMap ve Secret kullanımı  
- Git ile versiyon kontrolü  
- Gereksiz dosyaların Git’ten temizlenmesi (.venv gibi)

Bu proje bana gerçek bir DevOps pipeline’ının temel taşlarını uygulamalı olarak öğretti.

---

## 👤 Geliştirici

Bekir Olsen  
Kubernetes & DevOps öğrenme yolculuğu
