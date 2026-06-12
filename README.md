# ZutatenChef

ZutatenChef ist eine kleine Rezept-Finder-Webapp für das EDV-2-Projekt. Benutzer geben vorhandene Zutaten ein und bekommen passende Rezepte angezeigt. Die App kann außerdem ein bestimmtes Gericht mit den vorhandenen Zutaten vergleichen und fehlende Zutaten anzeigen.

## Funktionen

- Rezepte nach Zutaten suchen
- Pluralformen und Umlaute erkennen, zum Beispiel `Käse`, `Kase` und `Kaese`
- Rezepte nach Typ, Zeit, Schwierigkeit und Portionen filtern
- Fehlende Zutaten anzeigen
- Einkaufsliste aus fehlenden Zutaten erstellen
- Favoriten im Browser speichern
- Rezeptdaten aus `rezepte.yaml` laden
- Rezeptbilder anzeigen

## Technologien

- Python
- Bottle
- HTML Templates
- CSS
- YAML
- JavaScript im Browser fuer Favoriten und Einkaufsliste

## Projektstruktur

```text
.
├── app.py
├── rezepte.yaml
├── requirements.txt
├── views/
│   ├── index.tpl
│   ├── result.tpl
│   ├── check_result.tpl
│   └── about.tpl
└── static/
    └── style.css
```

## Installation

Voraussetzung: Python und pip sind installiert.

```bash
pip install -r requirements.txt
```

## Starten

```bash
python app.py
```

Danach im Browser öffnen:

```text
http://localhost:8080
```

## Wichtige Seiten

- Startseite: `http://localhost:8080/`
- About-Seite: `http://localhost:8080/about`

## Verantwortungsbereiche

Das Projekt wurde gemeinsam von Ali Almeman und Can Güzeyli entwickelt. Wir haben die Arbeit gemeinsam geplant, getestet und die wichtigsten Teile zusammen besprochen.

- Ali Almeman: Python und Bottle-Routen, Zutatenvergleich, YAML-Datenstruktur, Tests und Deployment mit GitHub und Render
- Can Güzeyli: Python-Logik für Rezeptfunktionen, HTML-Templates, CSS-Design, Rezeptdaten und Testen der Bedienung
- Gemeinsam: Rezeptsuche, Umlaut- und Plural-Erkennung, Favoriten, Einkaufsliste, Fehlerbehebung und Live-Demo

## Hinweise

Die Webapp ist als Lernprojekt gebaut. Der Fokus liegt auf Funktionalität, Struktur, Verständlichkeit und einer stabilen Live-Demo.
