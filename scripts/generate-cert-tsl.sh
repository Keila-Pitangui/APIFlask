#/bin/bash

#shell script apenas para teste

# Definir o diretório relativo onde os certificados serão armazenados
CERT_DIR="$HOME/APIFlask/certificate-dir"

sudo mkdir -p ./certificate-dir
sudo chown -R $USER:$USER /home/ubuntu/APIFlask/certificate-dir

# Definir os arquivos de certificado
CERT_FILE="$CERT_DIR/cert.crt"
KEY_FILE="$CERT_DIR/cert.key"

cd $CERT_DIR

# Gerar um certificado autoassinado
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $KEY_FILE -out $CERT_FILE -subj "/CN=app-api-flask.local"

ls -l $CERT_DIR

# Criar o Secret no Kubernetes
kubectl create secret tls app-api-flask-tls-secret \
  --cert=$CERT_FILE \
  --key=$KEY_FILE \
  --namespace=development


# Aplicar o Deployment que vai usar esse Secret
kubectl apply -f /home/ubuntu/APIFlask/k8s/deployment.yaml