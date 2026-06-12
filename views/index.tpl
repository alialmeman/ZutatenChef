<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZutatenChef</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <main class="container">
        <section class="hero">
            <div class="badge">Rezept-Finder</div>
            <h1>👨‍🍳 ZutatenChef</h1>
            <p>Gib deine Zutaten ein und finde passende Rezepte.</p>
            <a class="about-link" href="/about">Über das Projekt</a>
        </section>

        <section class="search-panel">
            <h2>Rezepte nach Zutaten finden</h2>
            <form class="suchbox" action="/ergebnis" method="post">
                <input id="zutaten-input" type="text" name="zutaten" placeholder="z.B. brot kase" required>
                <select name="typ" aria-label="Rezepttyp">
                    <option value="alle">Alle Typen</option>
                    <option value="vegetarisch">Vegetarisch</option>
                    <option value="fleisch">Fleisch</option>
                    <option value="fisch">Fisch</option>
                </select>
                <select name="zeit" aria-label="Zeit">
                    <option value="alle">Alle Zeiten</option>
                    <option value="15">bis 15 Min.</option>
                    <option value="30">bis 30 Min.</option>
                    <option value="45">bis 45 Min.</option>
                    <option value="60">bis 60 Min.</option>
                </select>
                <select name="schwierigkeit" aria-label="Schwierigkeit">
                    <option value="alle">Alle Level</option>
                    <option value="leicht">Leicht</option>
                    <option value="mittel">Mittel</option>
                    <option value="schwer">Schwer</option>
                </select>
                <input class="portionen-input" type="number" name="portionen" min="1" max="12" placeholder="Portionen">
                <button type="submit">Rezepte suchen</button>
            </form>

            <section class="quick-zutaten" aria-label="Häufige Zutaten">
                <button type="button" data-zutat="ei">Ei</button>
                <button type="button" data-zutat="milch">Milch</button>
                <button type="button" data-zutat="brot">Brot</button>
                <button type="button" data-zutat="kase">Käse</button>
                <button type="button" data-zutat="tomate">Tomate</button>
                <button type="button" data-zutat="nudeln">Nudeln</button>
                <button type="button" data-zutat="reis">Reis</button>
                <button type="button" data-zutat="huhn">Huhn</button>
                <button type="button" data-zutat="salat">Salat</button>
                <button type="button" data-zutat="gurke">Gurke</button>
                <button type="button" data-zutat="kartoffel">Kartoffel</button>
                <button type="button" data-zutat="paprika">Paprika</button>
                <button type="button" data-zutat="zwiebel">Zwiebel</button>
                <button type="button" data-zutat="knoblauch">Knoblauch</button>
                <button type="button" data-zutat="butter">Butter</button>
                <button type="button" data-zutat="mehl">Mehl</button>
                <button type="button" data-zutat="sahne">Sahne</button>
                <button type="button" data-zutat="mozzarella">Mozzarella</button>
                <button type="button" data-zutat="spinat">Spinat</button>
                <button type="button" data-zutat="mais">Mais</button>
                <button type="button" data-zutat="bohnen">Bohnen</button>
                <button type="button" data-zutat="thunfisch">Thunfisch</button>
                <button type="button" data-zutat="lachs">Lachs</button>
                <button type="button" data-zutat="avocado">Avocado</button>
                <button type="button" data-zutat="wrap">Wrap</button>
                <button type="button" data-zutat="curry">Curry</button>
                <button type="button" data-zutat="kokosmilch">Kokosmilch</button>
                <button type="button" data-zutat="linsen">Linsen</button>
                <button type="button" data-zutat="karotte">Karotte</button>
                <button type="button" data-zutat="banane">Banane</button>
            </section>
        </section>

        <section class="search-panel check-panel">
            <h2>Rezept und fehlende Zutaten prüfen</h2>
            <form class="check-form" action="/rezept-check" method="post">
                <input type="text" name="gericht" placeholder="Gericht, z.B. Pizza" required>
                <input type="text" name="vorhandene_zutaten" placeholder="Meine Zutaten, z.B. teig tomate" required>
                <input class="portionen-input" type="number" name="portionen" min="1" max="12" placeholder="Portionen">
                <button type="submit">Rezept prüfen</button>
            </form>
        </section>

        <section id="home-favoriten" class="search-panel favoriten-panel">
            <h2>Favoriten</h2>
            <p class="empty-favoriten">Noch keine Favoriten gespeichert.</p>
            <div class="favoriten-liste"></div>
            <p class="favoriten-status" aria-live="polite"></p>
        </section>
    </main>

    <script>
        const zutatenInput = document.querySelector("#zutaten-input");
        const zutatButtons = document.querySelectorAll("[data-zutat]");

        zutatButtons.forEach((button) => {
            button.addEventListener("click", () => {
                const zutat = button.dataset.zutat;
                const aktuelleZutaten = zutatenInput.value.trim().split(/\s+/).filter(Boolean);

                if (!aktuelleZutaten.includes(zutat)) {
                    aktuelleZutaten.push(zutat);
                }

                zutatenInput.value = aktuelleZutaten.join(" ");
                zutatenInput.focus();
            });
        });

        const favoritenPanel = document.querySelector("#home-favoriten");
        const favoritenListe = favoritenPanel.querySelector(".favoriten-liste");
        const emptyFavoriten = favoritenPanel.querySelector(".empty-favoriten");
        const favoritenStatus = favoritenPanel.querySelector(".favoriten-status");

        function ladeFavoriten() {
            return JSON.parse(localStorage.getItem("zutatenchefFavoriten") || "[]");
        }

        function speichereFavoriten(favoriten) {
            localStorage.setItem("zutatenchefFavoriten", JSON.stringify(favoriten));
        }

        function zeigeFavoriten() {
            const favoriten = ladeFavoriten();

            if (!favoriten.length) {
                emptyFavoriten.style.display = "block";
                favoritenListe.innerHTML = "";
                return;
            }

            emptyFavoriten.style.display = "none";
            favoritenListe.innerHTML = favoriten.map((name) => `
                <span class="favorit-chip">
                    ${name}
                    <button type="button" data-remove-favorit="${name}" aria-label="${name} aus Favoriten entfernen">Entfernen</button>
                </span>
            `).join("");
        }

        favoritenListe.addEventListener("click", (event) => {
            const button = event.target.closest("[data-remove-favorit]");
            if (!button) {
                return;
            }

            const name = button.dataset.removeFavorit;
            const favoriten = ladeFavoriten().filter((favorit) => favorit !== name);
            speichereFavoriten(favoriten);
            zeigeFavoriten();
            favoritenStatus.textContent = `${name} entfernt.`;
        });

        zeigeFavoriten();
    </script>
</body>
</html>
