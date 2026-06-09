<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ergebnisse</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <main class="container">
        <section class="hero compact">
            <div class="badge">ZutatenChef</div>
            <h1>Gefundene Rezepte</h1>
            % if eingabe:
                <p>Suche nach: <strong>{{eingabe}}</strong></p>
            % else:
                <p>Bitte gib zuerst Zutaten ein.</p>
            % end
        </section>

        % if rezepte:
            <p class="anzahl">{{len(rezepte)}} Rezept(e) gefunden</p>
            % for name, rezept in rezepte.items():
                <article class="karte">
                    <img class="rezept-bild" src="{{rezept['bild']}}" alt="{{name}}">
                    <div class="kartenkopf">
                        <h2>{{name}}</h2>
                        <button class="favorit-btn" type="button" data-favorit="{{name}}">Favorit</button>
                    </div>
                    <div class="meta-zeile">
                        <span>{{rezept["typ"]}}</span>
                        <span>{{rezept["schwierigkeit"].capitalize()}}</span>
                        <span>ca. {{rezept["kalorien"]}} kcal/Portion</span>
                    </div>
                    % if rezept.get("portionen"):
                        <p><strong>Portionen:</strong> {{rezept["portionen"]}}</p>
                    % end
                    % if rezept.get("zeit"):
                        <p><strong>Zeit:</strong> {{rezept["zeit"]}}</p>
                    % end
                    <p><strong>Zutaten:</strong> {{", ".join(rezept["zutaten_anzeige"])}}</p>
                    % if rezept.get("fehlende_zutaten"):
                        <p><strong>Fehlende Zutaten:</strong> {{", ".join(rezept["fehlende_zutaten"])}}</p>
                        <button class="liste-btn" type="button" data-zutaten="{{', '.join(rezept['fehlende_zutaten'])}}">Einkaufsliste</button>
                    % else:
                        <p><strong>Status:</strong> Du hast alle wichtigen Zutaten.</p>
                    % end
                    % if rezept.get("schritte"):
                        <p><strong>Zubereitung:</strong></p>
                        <ol class="schritte">
                            % for schritt in rezept["schritte"]:
                                <li>{{schritt}}</li>
                            % end
                        </ol>
                    % else:
                        <p><strong>Anleitung:</strong> {{rezept["anleitung"]}}</p>
                    % end
                </article>
            % end
        % else:
            <p class="hinweis">Keine Rezepte gefunden.</p>
        % end

        <a class="zurueck" href="/">Zurück</a>
        <section id="favoriten-box" class="info-box"></section>
        <section id="einkaufsliste-box" class="info-box"></section>
    </main>
    <script>
        const favoritButtons = document.querySelectorAll(".favorit-btn");
        const listeButtons = document.querySelectorAll(".liste-btn");
        const favoritenBox = document.querySelector("#favoriten-box");
        const einkaufslisteBox = document.querySelector("#einkaufsliste-box");

        function ladeFavoriten() {
            return JSON.parse(localStorage.getItem("zutatenchefFavoriten") || "[]");
        }

        function speichereFavoriten(favoriten) {
            localStorage.setItem("zutatenchefFavoriten", JSON.stringify(favoriten));
        }

        function zeigeFavoriten() {
            const favoriten = ladeFavoriten();
            if (!favoriten.length) {
                favoritenBox.innerHTML = "";
                return;
            }
            favoritenBox.innerHTML = "<strong>Favoriten:</strong> " + favoriten.join(", ");
        }

        favoritButtons.forEach((button) => {
            button.addEventListener("click", () => {
                const name = button.dataset.favorit;
                const favoriten = ladeFavoriten();
                if (!favoriten.includes(name)) {
                    favoriten.push(name);
                    speichereFavoriten(favoriten);
                }
                button.textContent = "Favorit gespeichert";
                button.classList.add("is-done");
                zeigeFavoriten();
            });
        });

        listeButtons.forEach((button) => {
            button.addEventListener("click", () => {
                const zutaten = button.dataset.zutaten.split(",").map((zutat) => zutat.trim()).filter(Boolean);
                einkaufslisteBox.innerHTML = "<strong>Einkaufsliste:</strong><ul>" + zutaten.map((zutat) => `<li>${zutat}</li>`).join("") + "</ul>";
                button.textContent = "Einkaufsliste erstellt";
                button.classList.add("is-done");
            });
        });

        zeigeFavoriten();
    </script>
</body>
</html>
