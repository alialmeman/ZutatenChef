import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "vendor"))

import yaml
from bottle import default_app, route, run, request, template, static_file


with open("rezepte.yaml", "r", encoding="utf-8") as file:
    rezepte = yaml.safe_load(file)


BILD_GRUPPEN = [
    (("curry",), [
        "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=900&q=80",
    ]),
    (("taco", "burrito", "wrap"), [
        "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=900&q=80",
    ]),
    (("bowl", "sushi", "quinoa", "couscous"), [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=900&q=80",
    ]),
    (("fisch", "lachs"), [
        "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=900&q=80",
    ]),
    (("pfannkuchen", "waffel", "pancake"), [
        "https://images.unsplash.com/photo-1528207776546-365bb710ee93?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1484723091739-30a097e8f929?auto=format&fit=crop&w=900&q=80",
    ]),
    (("auflauf", "lasagne", "quiche"), [
        "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1565958011703-44f9829ba187?auto=format&fit=crop&w=900&q=80",
    ]),
    (("pizza", "teig"), [
        "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1594007654729-407eedc4be65?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=900&q=80",
    ]),
    (("pasta", "nudeln"), [
        "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=900&q=80",
    ]),
    (("salat", "gurke"), [
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&w=900&q=80",
    ]),
    (("burger", "fleisch"), [
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=900&q=80",
    ]),
    (("toast", "brot"), [
        "https://images.unsplash.com/photo-1528736235302-52922df5c122?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1481070555726-e2fe8357725c?auto=format&fit=crop&w=900&q=80",
    ]),
    (("reis",), [
        "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=900&q=80",
    ]),
    (("suppe", "wasser"), [
        "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1604152135912-04a022e23696?auto=format&fit=crop&w=900&q=80",
    ]),
    (("ei", "omelett"), [
        "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1608039829572-78524f79c4c7?auto=format&fit=crop&w=900&q=80",
    ]),
    (("kartoffel",), [
        "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1590165482129-1b8b27698780?auto=format&fit=crop&w=900&q=80",
    ]),
    (("huhn",), [
        "https://images.unsplash.com/photo-1598103442097-8b74394b95c6?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=900&q=80",
    ]),
]

DEFAULT_BILDER = [
    "https://images.unsplash.com/photo-1495521821757-a1efb6729352?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=900&q=80",
]


UMLAUTS = str.maketrans({
    "ä": "a",
    "ö": "o",
    "ü": "u",
    "ß": "ss",
})

ZUTATEN_ALIASE = {
    "aepfel": "apfel",
    "apfeln": "apfel",
    "bananen": "banane",
    "bohnen": "bohnen",
    "broetchen": "brot",
    "chicken": "huhn",
    "eier": "ei",
    "gurken": "gurke",
    "haehnchen": "huhn",
    "hahnchen": "huhn",
    "kaese": "kase",
    "kartoffeln": "kartoffel",
    "karotten": "karotte",
    "moehren": "karotte",
    "nudel": "nudeln",
    "paprikas": "paprika",
    "pilze": "pilz",
    "pilzen": "pilz",
    "salate": "salat",
    "tomaten": "tomate",
    "zwiebeln": "zwiebel",
}

ZUTATEN_ANZEIGE = {
    "avocado": "Avocado",
    "bohnen": "Kidneybohnen",
    "brot": "Brot",
    "butter": "Butter",
    "curry": "Currypulver",
    "ei": "Eier",
    "feta": "Feta",
    "gurke": "Gurke",
    "huhn": "Hähnchenbrust",
    "karotte": "Karotten",
    "kartoffel": "Kartoffeln",
    "kase": "Käse",
    "knoblauch": "Knoblauch",
    "kokosmilch": "Kokosmilch",
    "mais": "Mais",
    "milch": "Milch",
    "mozzarella": "Mozzarella",
    "nudeln": "Nudeln",
    "olivenol": "Olivenöl",
    "paprika": "Paprika",
    "pesto": "Pesto",
    "pilz": "Pilze",
    "reis": "Reis",
    "sahne": "Sahne",
    "salat": "Salat",
    "schinken": "Schinken",
    "spinat": "Spinat",
    "thunfisch": "Thunfisch",
    "tomate": "Tomaten",
    "wrap": "Tortillas",
    "zucchini": "Zucchini",
    "zwiebel": "Zwiebel",
}

STOPWORDS = {
    "and",
    "ile",
    "mit",
    "und",
    "ve",
}

FLEISCH_ZUTATEN = {"fleisch", "huhn", "schinken", "salami"}
FISCH_ZUTATEN = {"fisch", "lachs", "thunfisch"}

KALORIEN_PRO_100G = {
    "avocado": 160,
    "banane": 89,
    "bohnen": 120,
    "brot": 250,
    "butter": 720,
    "ei": 155,
    "feta": 260,
    "fleisch": 250,
    "huhn": 165,
    "kase": 350,
    "kartoffel": 77,
    "kokosmilch": 190,
    "lachs": 208,
    "linsen": 116,
    "mehl": 364,
    "milch": 64,
    "mozzarella": 280,
    "nudeln": 150,
    "olivenol": 884,
    "reis": 130,
    "sahne": 292,
    "spaghetti": 150,
    "thunfisch": 132,
    "wrap": 310,
    "zucker": 387,
}

GEWICHT_PRO_STUECK = {
    "avocado": 150,
    "banane": 120,
    "brot": 40,
    "ei": 55,
    "gurke": 300,
    "karotte": 80,
    "kartoffel": 150,
    "knoblauch": 5,
    "paprika": 150,
    "tomate": 120,
    "wrap": 60,
    "zwiebel": 100,
}


def normalisiere_zutat(zutat):
    zutat = repariere_encoding(zutat)

    zutat = zutat.lower().translate(UMLAUTS)
    zutat = (
        zutat
        .replace("ae", "a")
        .replace("oe", "o")
        .replace("ue", "u")
    )
    zutat = re.sub(r"[^a-z0-9]+", "", zutat)

    if zutat in ZUTATEN_ALIASE:
        return ZUTATEN_ALIASE[zutat]

    if len(zutat) > 5 and zutat.endswith("s"):
        return zutat[:-1]

    return zutat


def lese_zutaten_eingabe(text):
    return {
        normalisiere_zutat(zutat)
        for zutat in repariere_encoding(text).split()
        if normalisiere_zutat(zutat)
        and normalisiere_zutat(zutat) not in STOPWORDS
    }


def repariere_encoding(text):
    for _ in range(3):
        vorher = text

        try:
            text = text.encode("latin1").decode("utf-8")
        except UnicodeError:
            pass

        text = (
            text
            .replace("ÃƒÂ¤", "ä")
            .replace("ÃƒÂ¶", "ö")
            .replace("ÃƒÂ¼", "ü")
            .replace("ÃƒÂ„", "Ä")
            .replace("ÃƒÂ–", "Ö")
            .replace("ÃƒÂœ", "Ü")
            .replace("ÃƒÂŸ", "ß")
            .replace("Ã¤", "ä")
            .replace("Ã¶", "ö")
            .replace("Ã¼", "ü")
            .replace("Ã„", "Ä")
            .replace("Ã–", "Ö")
            .replace("Ãœ", "Ü")
            .replace("ÃŸ", "ß")
            .replace("Â", "")
        )

        if text == vorher:
            break

    return text


def zeige_zutat(zutat):
    return ZUTATEN_ANZEIGE.get(zutat, zutat)


def zeige_eingabe(text):
    return repariere_encoding(text)


def rezept_mit_anzeige(name, rezept, bild_offset=0, ziel_portionen=None):
    rezept_anzeige = dict(rezept)
    rezept_anzeige["bild"] = bild_fuer_rezept(name, rezept, bild_offset)
    rezept_anzeige["zutaten_anzeige"] = zutaten_anzeigen(rezept, ziel_portionen)
    rezept_anzeige["typ"] = rezept_typ(rezept)
    rezept_anzeige["schwierigkeit"] = schwierigkeit(rezept)
    rezept_anzeige["kalorien"] = kalorien_schaetzen(rezept, ziel_portionen)
    if ziel_portionen:
        rezept_anzeige["portionen"] = f"{ziel_portionen} Portionen"
    return rezept_anzeige


def zutaten_namen(rezept):
    namen = []

    for zutat in rezept.get("zutaten", []):
        if isinstance(zutat, dict):
            namen.append(zutat.get("name", ""))
        else:
            namen.append(zutat)

    return namen


def zutaten_anzeigen(rezept, ziel_portionen=None):
    anzeigen = []
    faktor = portionen_faktor(rezept, ziel_portionen)

    for zutat in rezept.get("zutaten", []):
        if isinstance(zutat, dict):
            if zutat.get("anzeige"):
                anzeigen.append(skaliere_anzeige(zutat["anzeige"], faktor))
                continue

            name = zeige_zutat(zutat.get("name", ""))
            menge = skaliere_anzeige(zutat.get("menge", ""), faktor)
            anzeigen.append(f"{menge} {name}".strip())
        else:
            anzeigen.append(zeige_zutat(zutat))

    return anzeigen


def zahl_aus_text(text):
    treffer = re.search(r"\d+(?:[.,]\d+)?", str(text))
    if not treffer:
        return None
    return float(treffer.group(0).replace(",", "."))


def portionen_faktor(rezept, ziel_portionen):
    if not ziel_portionen:
        return 1
    basis = zahl_aus_text(rezept.get("portionen", ""))
    if not basis:
        return 1
    return max(0.25, float(ziel_portionen) / basis)


def skaliere_anzeige(text, faktor):
    if faktor == 1:
        return text

    def ersetze(match):
        wert = float(match.group(0).replace(",", "."))
        neu = wert * faktor
        if neu.is_integer():
            return str(int(neu))
        return f"{neu:.1f}".replace(".", ",")

    return re.sub(r"\d+(?:[.,]\d+)?", ersetze, text, count=1)


def rezept_typ(rezept):
    zutaten = {normalisiere_zutat(zutat) for zutat in zutaten_namen(rezept)}
    if zutaten & FISCH_ZUTATEN:
        return "Fisch"
    if zutaten & FLEISCH_ZUTATEN:
        return "Fleisch"
    return "Vegetarisch"


def minuten(rezept):
    return int(zahl_aus_text(rezept.get("zeit", "")) or 0)


def schwierigkeit(rezept):
    zeit = minuten(rezept)
    anzahl_zutaten = len(zutaten_namen(rezept))
    anzahl_schritte = len(rezept.get("schritte", []))
    if zeit <= 20 and anzahl_zutaten <= 5:
        return "leicht"
    if zeit <= 45 and anzahl_schritte <= 5:
        return "mittel"
    return "schwer"


def kalorien_schaetzen(rezept, ziel_portionen=None):
    faktor = portionen_faktor(rezept, ziel_portionen)
    gesamt = 0
    for zutat in rezept.get("zutaten", []):
        if not isinstance(zutat, dict):
            continue
        name = normalisiere_zutat(zutat.get("name", ""))
        menge = zahl_aus_text(zutat.get("menge", ""))
        if not menge or name not in KALORIEN_PRO_100G:
            continue
        if (
            "stück" in zutat.get("menge", "").lower()
            or "scheibe" in zutat.get("menge", "").lower()
        ):
            menge = menge * GEWICHT_PRO_STUECK.get(name, 100)
        gesamt += (menge * faktor) * KALORIEN_PRO_100G[name] / 100
    portionen = int(ziel_portionen or (zahl_aus_text(rezept.get("portionen", "")) or 1))
    return int(gesamt / max(1, portionen))


def passt_zu_filtern(rezept, typ_filter, zeit_filter, schwierigkeit_filter):
    if typ_filter and typ_filter != "alle" and rezept_typ(rezept).lower() != typ_filter:
        return False
    if schwierigkeit_filter and schwierigkeit_filter != "alle" and schwierigkeit(rezept) != schwierigkeit_filter:
        return False
    if zeit_filter and zeit_filter != "alle":
        limit = int(zeit_filter)
        if minuten(rezept) > limit:
            return False
    return True


def normalisiere_text(text):
    text = repariere_encoding(text)
    return " ".join(normalisiere_zutat(wort) for wort in text.split())


def finde_rezept_nach_name(gericht_name):
    gesuchter_name = normalisiere_text(gericht_name)
    gesuchter_name_kompakt = gesuchter_name.replace(" ", "")

    for name, rezept in rezepte.items():
        rezept_name = normalisiere_text(name)
        rezept_name_kompakt = rezept_name.replace(" ", "")

        if (
            rezept_name == gesuchter_name
            or gesuchter_name in rezept_name
            or rezept_name_kompakt == gesuchter_name_kompakt
            or gesuchter_name_kompakt in rezept_name_kompakt
        ):
            return name, rezept

    return None, None


def bild_fuer_rezept(name, rezept, offset=0):
    if rezept.get("bild_url"):
        return rezept["bild_url"]

    suchtext = normalisiere_text(
        str(rezept.get("bild_kategorie", ""))
        + " "
        + name
        + " "
        + " ".join(zutaten_namen(rezept))
    )
    seed = sum(ord(zeichen) for zeichen in suchtext)

    for keywords, bild_urls in BILD_GRUPPEN:
        if any(keyword in suchtext for keyword in keywords):
            return bild_urls[(seed + offset) % len(bild_urls)]

    return DEFAULT_BILDER[(seed + offset) % len(DEFAULT_BILDER)]


@route("/")
def index():
    return template("index")


@route("/about")
def about():
    return template("about")


@route("/ergebnis", method=["GET", "POST"])
def ergebnis():
    eingabe = zeige_eingabe(request.forms.get("zutaten", ""))
    user_zutaten = lese_zutaten_eingabe(eingabe)
    suchbegriffe = set(normalisiere_text(eingabe).split())
    typ_filter = request.forms.get("typ", "alle")
    zeit_filter = request.forms.get("zeit", "alle")
    schwierigkeit_filter = request.forms.get("schwierigkeit", "alle")
    ziel_portionen = int(request.forms.get("portionen", "0") or 0) or None
    rezept_treffer = []
    verwendete_bilder = set()

    if user_zutaten or suchbegriffe:
        for name, rezept in rezepte.items():
            if not passt_zu_filtern(
                rezept, typ_filter, zeit_filter, schwierigkeit_filter
            ):
                continue

            rezept_zutaten = [
                normalisiere_zutat(zutat) for zutat in zutaten_namen(rezept)
            ]
            rezept_zutaten = [zutat for zutat in rezept_zutaten if zutat]
            rezept_name_tokens = set(normalisiere_text(name).split())
            kategorie_tokens = set(normalisiere_text(rezept.get("bild_kategorie", "")).split())
            passende_zutaten = [
                zutat for zutat in rezept_zutaten if zutat in user_zutaten
            ]
            passende_texttreffer = suchbegriffe & (rezept_name_tokens | kategorie_tokens)
            fehlende_zutaten = [
                zutat for zutat in rezept_zutaten if zutat not in user_zutaten
            ]

            if not passende_zutaten and not passende_texttreffer:
                continue

            genug_treffer = len(passende_zutaten) >= min(2, len(rezept_zutaten))
            fast_machbar = len(fehlende_zutaten) <= 3
            komplett_machbar = not fehlende_zutaten
            name_passt = bool(passende_texttreffer)

            if komplett_machbar or (genug_treffer and fast_machbar) or name_passt:
                rezept_treffer.append((
                    len(fehlende_zutaten),
                    -(len(passende_zutaten) + len(passende_texttreffer)),
                    len(rezept_zutaten),
                    name,
                    rezept,
                    fehlende_zutaten,
                ))

    rezept_treffer.sort()
    gefundene_rezepte = {}

    for _, _, _, name, rezept, fehlende_zutaten in rezept_treffer[:18]:
        bild_offset = len(gefundene_rezepte)
        rezept_anzeige = rezept_mit_anzeige(
            name, rezept, bild_offset, ziel_portionen
        )
        rezept_anzeige["fehlende_zutaten"] = [
            zeige_zutat(zutat) for zutat in fehlende_zutaten
        ]

        while (
            rezept_anzeige["bild"] in verwendete_bilder
            and bild_offset < len(gefundene_rezepte) + 8
        ):
            bild_offset += 1
            rezept_anzeige = rezept_mit_anzeige(
                name, rezept, bild_offset, ziel_portionen
            )
            rezept_anzeige["fehlende_zutaten"] = [
                zeige_zutat(zutat) for zutat in fehlende_zutaten
            ]

        verwendete_bilder.add(rezept_anzeige["bild"])
        gefundene_rezepte[name] = rezept_anzeige

    return template(
        "result",
        rezepte=gefundene_rezepte,
        eingabe=eingabe,
        typ_filter=typ_filter,
        zeit_filter=zeit_filter,
        schwierigkeit_filter=schwierigkeit_filter,
        portionen=ziel_portionen,
    )


@route("/rezept-check", method=["POST"])
def rezept_check():
    gericht = zeige_eingabe(request.forms.get("gericht", ""))
    eingabe_zutaten = zeige_eingabe(request.forms.get("vorhandene_zutaten", ""))
    vorhandene_zutaten = lese_zutaten_eingabe(eingabe_zutaten)
    ziel_portionen = int(request.forms.get("portionen", "0") or 0) or None
    rezept_name, rezept = finde_rezept_nach_name(gericht)
    fehlende_zutaten = []

    if rezept:
        fehlende_zutaten = [
            zeige_zutat(zutat) for zutat in zutaten_namen(rezept)
            if normalisiere_zutat(zutat) not in vorhandene_zutaten
        ]
        rezept = rezept_mit_anzeige(rezept_name, rezept, ziel_portionen=ziel_portionen)

    return template(
        "check_result",
        gericht=gericht,
        vorhandene_zutaten=eingabe_zutaten,
        rezept_name=rezept_name,
        rezept=rezept,
        fehlende_zutaten=fehlende_zutaten,
        portionen=ziel_portionen,
    )


@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./static")


application = default_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    run(host="0.0.0.0", port=port, debug=True)
