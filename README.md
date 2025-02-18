# Detection_logo
🚀 Projet de Détection de Logos avec Flask et Roboflow


📌 Description

Ce projet est une application web permettant de détecter des logos à partir d'images en utilisant l'API de Roboflow. L'application est construite avec Flask pour gérer l'interface et l'API backend.

📷 Fonctionnalités

📂 Upload d'images : L'utilisateur peut charger une image.

🖼️ Détection de logos : L'image est envoyée à l'API Roboflow pour analyse.

🖥️ Affichage des résultats : L'application affiche l'image annotée avec les logos détectés.

🛠️ Installation et Exécution

1️⃣ Cloner le projet

git clone https://github.com/TON-UTILISATEUR/TON-DEPOT.git
cd TON-DEPOT

2️⃣ Installer les dépendances

Assurez-vous d'avoir Python 3.7+ installé, puis exécutez :

pip install -r requirements.txt

3️⃣ Lancer l'application Flask

python app.py

Accédez ensuite à l'application sur http://127.0.0.1:5000/.

🗂️ Arborescence du Projet

📂 Detection_logo
 ├── 📂 static           # Fichiers CSS, JS, images
 ├── 📂 templates        # Fichiers HTML (index.html, result.html...)
 ├── app.py             # Script principal de l'application Flask
 ├── requirements.txt   # Liste des dépendances Python
 ├── README.md          # Documentation du projet

🔑 Configuration de l'API Roboflow

Ajoutez votre clé API dans un fichier .env (évitez de la mettre dans le code directement) :

API_URL=https://detect.roboflow.com
API_KEY=VOTRE_CLE_API
MODEL_ID=detection_logo/2

Puis, chargez ces variables dans app.py avec python-dotenv.

✨ Exemple d'Utilisation de l'API Roboflow

from inference_sdk import InferenceHTTPClient

# Initialisation du client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="VOTRE_CLE_API"
)

# Détection sur une image locale
result = CLIENT.infer("test.jpg", model_id="detection_logo/2")

🔥 Contribuer

Forkez le projet 🍴

Créez une branche feature-mon-amélioration 🛠️

Faites un commit de vos modifications 💾

Poussez sur GitHub et ouvrez une Pull Request 🚀

📜 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

💡 Auteur : Fatima

