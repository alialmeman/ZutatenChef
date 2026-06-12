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
            <p>
                Das Projekt wurde gemeinsam von <strong>Ali Almeman</strong> und
                <strong>Can Güzeyli</strong> entwickelt. Wir haben die Arbeit gemeinsam geplant,
                getestet und die wichtigsten Teile zusammen besprochen.
            </p>
            <div class="about-grid">
                <article>
                    <h3>Ali Almeman</h3>
                    <p>Python und Bottle-Routen, Zutatenvergleich, YAML-Datenstruktur, Tests und Deployment mit GitHub und Render.</p>
                </article>
                <article>
                    <h3>Can Güzeyli</h3>
                    <p>Python-Logik für Rezeptfunktionen, HTML-Templates, CSS-Design, Rezeptdaten und Testen der Bedienung.</p>
                </article>
                <article>
                    <h3>Gemeinsame Arbeit</h3>
                    <p>Rezeptsuche, Umlaut- und Plural-Erkennung, Favoriten, Einkaufsliste, Fehlerbehebung und Live-Demo.</p>
                </article>
                <article>
                    <h3>Projektziel</h3>
                    <p>Eine kleine, stabile und verständliche Webapp bauen, die auch auf anderen Computern gestartet werden kann.</p>
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
