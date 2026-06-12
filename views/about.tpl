<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Über ZutatenChef</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <main class="container">
        <section class="hero compact">
            <div class="badge">Projektinfo</div>
            <h1>Über ZutatenChef</h1>
            <p>Eine Webapp zum Finden passender Rezepte aus vorhandenen Zutaten.</p>
        </section>

        <section class="search-panel about-panel">
            <h2>Zweck der App</h2>
            <p>
                ZutatenChef hilft Benutzern, aus vorhandenen Zutaten passende Rezepte zu finden.
                Zusätzlich kann ein bestimmtes Gericht geprüft werden: Die App zeigt dann das Rezept
                und die fehlenden Zutaten an.
            </p>

            <h2>Team und Aufgaben</h2>
            <div class="about-grid">
                <article>
                    <h3>Backend</h3>
                    <p>Python, Bottle-Routen, Rezeptsuche, Filter, Zutatenvergleich und Portionenberechnung.</p>
                </article>
                <article>
                    <h3>Daten</h3>
                    <p>Rezepte werden in der YAML-Datei <strong>rezepte.yaml</strong> gespeichert und in Python geladen.</p>
                </article>
                <article>
                    <h3>Frontend</h3>
                    <p>HTML-Templates, CSS-Design, Favoriten und Einkaufsliste im Browser.</p>
                </article>
                <article>
                    <h3>Deployment</h3>
                    <p>Der Code liegt auf GitHub und die Webapp wird über Render online bereitgestellt.</p>
                </article>
            </div>

            <h2>Verwendete Technologien</h2>
            <ul class="about-list">
                <li>Python mit Bottle</li>
                <li>HTML Templates im Ordner views</li>
                <li>Externes CSS im Ordner static</li>
                <li>YAML für die Rezeptdaten</li>
                <li>JavaScript für Favoriten und Einkaufsliste</li>
            </ul>
        </section>

        <a class="zurueck" href="/">Zurück zur Startseite</a>
    </main>
</body>
</html>
