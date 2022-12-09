import requests

def get_api_response(text):
    # URL de l'API Rasa
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"


    # Envoi de la requête à l'API et récupération de la réponse
    response = requests.post(rasa_url, json={
        "sender": "user",
        "message": text

    })

    # Affichage de la réponse de l'API
    print(response.json())
get_api_response("quel est mon gpa?")
get_api_response("quel mon agenda?")
get_api_response("quels sont mes modules?")
