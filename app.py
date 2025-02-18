import cv2
import numpy as np
from flask import Flask, request, send_file
from inference_sdk import InferenceHTTPClient
from flask import render_template

app = Flask(__name__)

# Initialisation du client Roboflow
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="KtxGboUg1XUNhMTSfHcI"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return "Aucune image envoyée", 400

    image = request.files["file"]
    image_path = "./temp_image.jpg"
    image.save(image_path)  # Sauvegarde temporaire de l'image

    try:
        # Envoi de l'image au modèle Roboflow
        result = CLIENT.infer(image_path, model_id="detection_logo/2")

        # Charger l'image
        img = cv2.imread(image_path)

        # Dessiner les détections
        for prediction in result["predictions"]:
            x, y, w, h = int(prediction["x"]), int(prediction["y"]), int(prediction["width"]), int(prediction["height"])
            label = prediction["class"]
            confidence = prediction["confidence"]

            # Définir les coins du rectangle
            x1, y1 = x - w // 2, y - h // 2
            x2, y2 = x + w // 2, y + h // 2

            # Dessiner le rectangle
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Ajouter le texte (classe + score de confiance)
            text = f"{label}: {confidence:.2f}"
            cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Sauvegarder l'image annotée
        output_path = "./annotated_image.jpg"
        cv2.imwrite(output_path, img)

        # Retourner l'image modifiée
        return send_file(output_path, mimetype="image/jpeg")

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
