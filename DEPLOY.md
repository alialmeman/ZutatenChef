# ZutatenChef online deploy

Diese App ist fuer Render/Railway/Python-Hosting vorbereitet.

## Render

1. Projektordner zu GitHub hochladen.
2. Render.com oeffnen und "New Web Service" waehlen.
3. GitHub Repository auswaehlen.
4. Build Command:
   `pip install -r requirements.txt`
5. Start Command:
   `gunicorn app:application`
6. Deploy starten.

Danach erzeugt Render eine echte Internet-Adresse, zum Beispiel:
`https://zutatenchef.onrender.com`

Wichtig: `localhost:8080` funktioniert nur auf dem eigenen Computer. Eine Render-Adresse funktioniert auf allen Geraeten und Browsern.
