from dataclasses import dataclass
from typing import List, Optional

from app.schemas.weather import WeatherForecastResponse, CropAdviceResponse, CropAction


@dataclass
class CropProfile:
    name: str
    temp_max_critical: float
    temp_min_critical: float
    water_per_week: int
    disease_risk_rain: int
    is_fungal_sensitive: bool
    main_diseases: List[str]


CROPS = {
    # ──────────────────────────────────────────────
    # LÉGUMES FRUITS
    # ──────────────────────────────────────────────
    "tomate":        CropProfile("Tomate",        32, 10, 35, 10, True,  ["mildiou", "alternariose"]),
    "pomme de terre":CropProfile("Pomme de terre",30,  5, 30, 10, True,  ["mildiou"]),
    "pdt":           CropProfile("Pomme de terre",30,  5, 30, 10, True,  ["mildiou"]),
    "courgette":     CropProfile("Courgette",     35, 10, 40, 10, True,  ["oïdium"]),
    "poivron":       CropProfile("Poivron",       32, 12, 35, 10, True,  ["mildiou"]),
    "piment":        CropProfile("Piment",        35, 12, 30, 10, True,  ["mildiou", "botrytis"]),
    "aubergine":     CropProfile("Aubergine",     35, 12, 35, 10, False, ["mildiou"]),
    "concombre":     CropProfile("Concombre",     32, 12, 45, 10, True,  ["mildiou", "oïdium"]),
    "melon":         CropProfile("Melon",         38, 15, 30,  8, True,  ["fusariose", "oïdium"]),
    "pastèque":      CropProfile("Pastèque",      38, 15, 40,  8, True,  ["fusariose", "anthracnose"]),
    "pasteque":      CropProfile("Pastèque",      38, 15, 40,  8, True,  ["fusariose", "anthracnose"]),
    "citrouille":    CropProfile("Citrouille",    35, 10, 40, 10, True,  ["oïdium", "mildiou"]),
    "courge":        CropProfile("Courge",        35, 10, 40, 10, True,  ["oïdium", "mildiou"]),
    "butternut":     CropProfile("Butternut",     35, 10, 35, 10, True,  ["oïdium"]),
    "potiron":       CropProfile("Potiron",       35, 10, 40, 10, True,  ["oïdium", "mildiou"]),
    "potimarron":    CropProfile("Potimarron",    35, 10, 35, 10, True,  ["oïdium"]),
    "gombo":         CropProfile("Gombo",         38, 15, 35, 10, True,  ["fusariose", "mildiou"]),

    # ──────────────────────────────────────────────
    # LÉGUMES RACINES & BULBES
    # ──────────────────────────────────────────────
    "carotte":       CropProfile("Carotte",       30,  5, 25, 12, False, ["alternariose"]),
    "oignon":        CropProfile("Oignon",        32,  5, 20, 10, True,  ["mildiou"]),
    "ail":           CropProfile("Ail",           30, -5, 20, 10, True,  ["rouille", "mildiou"]),
    "échalote":      CropProfile("Échalote",      28, -5, 20, 10, True,  ["rouille", "mildiou"]),
    "echalote":      CropProfile("Échalote",      28, -5, 20, 10, True,  ["rouille", "mildiou"]),
    "betterave":     CropProfile("Betterave",     28, -3, 25, 12, True,  ["cercosporiose", "mildiou"]),
    "radis":         CropProfile("Radis",         22, -2, 20, 10, False, ["alternariose"]),
    "navet":         CropProfile("Navet",         22, -5, 25, 12, True,  ["mildiou"]),
    "panais":        CropProfile("Panais",        25, -8, 25, 12, False, ["septoriose"]),
    "patate douce":  CropProfile("Patate douce",  35, 12, 35, 10, True,  ["alternariose", "fusariose"]),
    "céleri":        CropProfile("Céleri",        25,  2, 40, 10, True,  ["septoriose", "mildiou"]),
    "celeri":        CropProfile("Céleri",        25,  2, 40, 10, True,  ["septoriose", "mildiou"]),
    "céleri-rave":   CropProfile("Céleri-rave",   25,  2, 40, 10, True,  ["septoriose"]),
    "fenouil":       CropProfile("Fenouil",       28,  0, 25, 10, False, ["rouille"]),
    "topinambour":   CropProfile("Topinambour",   30, -10, 25, 12, False, ["rouille"]),
    "manioc":        CropProfile("Manioc",        38, 15, 40, 10, True,  ["anthracnose"]),
    "igname":        CropProfile("Igname",        35, 15, 40, 10, True,  ["anthracnose"]),
    "taro":          CropProfile("Taro",          35, 12, 50, 10, True,  ["mildiou"]),
    "gingembre":     CropProfile("Gingembre",     35, 15, 50, 10, True,  ["fusariose"]),
    "curcuma":       CropProfile("Curcuma",       35, 15, 50, 10, True,  ["fusariose"]),

    # ──────────────────────────────────────────────
    # LÉGUMES FEUILLES & TIGES
    # ──────────────────────────────────────────────
    "laitue":        CropProfile("Laitue",        28,  5, 30,  8, True,  ["mildiou"]),
    "épinard":       CropProfile("Épinard",       25, -5, 25, 10, False, ["mildiou"]),
    "epinard":       CropProfile("Épinard",       25, -5, 25, 10, False, ["mildiou"]),
    "roquette":      CropProfile("Roquette",      22, -3, 25, 10, True,  ["mildiou"]),
    "mâche":         CropProfile("Mâche",         18, -8, 20, 10, True,  ["mildiou"]),
    "mache":         CropProfile("Mâche",         18, -8, 20, 10, True,  ["mildiou"]),
    "endive":        CropProfile("Endive",        18, -3, 25, 10, True,  ["mildiou", "botrytis"]),
    "blette":        CropProfile("Blette",        28, -5, 30, 10, True,  ["mildiou", "cercosporiose"]),
    "bette":         CropProfile("Blette",        28, -5, 30, 10, True,  ["mildiou", "cercosporiose"]),
    "chou":          CropProfile("Chou",          25, -5, 30, 15, True,  ["mildiou", "alternariose"]),
    "chou rouge":    CropProfile("Chou rouge",    25, -5, 30, 15, True,  ["mildiou", "alternariose"]),
    "chou-fleur":    CropProfile("Chou-fleur",    25, -2, 30, 15, True,  ["mildiou"]),
    "choufleur":     CropProfile("Chou-fleur",    25, -2, 30, 15, True,  ["mildiou"]),
    "brocoli":       CropProfile("Brocoli",       25, -5, 30, 15, True,  ["mildiou", "alternariose"]),
    "romanesco":     CropProfile("Romanesco",     22, -2, 30, 15, True,  ["mildiou"]),
    "chou de bruxelles": CropProfile("Chou de Bruxelles", 22, -8, 30, 15, True, ["mildiou"]),
    "kale":          CropProfile("Kale",          25,-10, 30, 12, True,  ["mildiou"]),
    "poireau":       CropProfile("Poireau",       25, -8, 25, 12, True,  ["rouille", "mildiou"]),
    "asperge":       CropProfile("Asperge",       28, -5, 20, 10, True,  ["rouille"]),
    "artichaut":     CropProfile("Artichaut",     28, -5, 30, 10, True,  ["mildiou", "botrytis"]),
    "cresson":       CropProfile("Cresson",       20, -3, 40,  8, True,  ["mildiou"]),
    "pourpier":      CropProfile("Pourpier",      32,  5, 25,  8, False, ["mildiou"]),
    "pak choï":      CropProfile("Pak choï",      25,  2, 30, 10, True,  ["mildiou"]),
    "pak choi":      CropProfile("Pak choï",      25,  2, 30, 10, True,  ["mildiou"]),

    # ──────────────────────────────────────────────
    # LÉGUMINEUSES & CÉRÉALES
    # ──────────────────────────────────────────────
    "haricot":       CropProfile("Haricot",       32,  8, 30, 12, True,  ["rouille"]),
    "haricot vert":  CropProfile("Haricot vert",  30,  8, 30, 12, True,  ["rouille", "anthracnose"]),
    "petit pois":    CropProfile("Petit pois",    22, -2, 25, 12, True,  ["oïdium", "mildiou"]),
    "pois":          CropProfile("Petit pois",    22, -2, 25, 12, True,  ["oïdium", "mildiou"]),
    "fève":          CropProfile("Fève",          20, -5, 25, 12, True,  ["rouille", "botrytis"]),
    "feve":          CropProfile("Fève",          20, -5, 25, 12, True,  ["rouille", "botrytis"]),
    "lentille":      CropProfile("Lentille",      28, -2, 20, 12, True,  ["botrytis", "rouille"]),
    "pois chiche":   CropProfile("Pois chiche",   35,  0, 20, 10, True,  ["botrytis"]),
    "soja":          CropProfile("Soja",          32,  5, 35, 15, True,  ["rouille", "mildiou"]),
    "maïs":          CropProfile("Maïs",          38,  8, 45, 20, False, ["charbon"]),
    "blé":           CropProfile("Blé",           35, -5, 25, 15, False, ["rouille"]),
    "orge":          CropProfile("Orge",          32, -8, 20, 15, False, ["rouille", "oïdium"]),
    "avoine":        CropProfile("Avoine",        30, -8, 25, 15, False, ["rouille"]),
    "seigle":        CropProfile("Seigle",        30,-10, 20, 15, False, ["ergot", "rouille"]),
    "tournesol":     CropProfile("Tournesol",     35,  5, 30, 15, True,  ["mildiou", "botrytis"]),
    "colza":         CropProfile("Colza",         28, -8, 20, 12, True,  ["phoma", "sclerotinia"]),

    # ──────────────────────────────────────────────
    # HERBES AROMATIQUES
    # ──────────────────────────────────────────────
    "basilic":       CropProfile("Basilic",       30, 10, 30, 10, True,  ["mildiou", "botrytis"]),
    "persil":        CropProfile("Persil",        25, -5, 25, 10, True,  ["septoriose"]),
    "coriandre":     CropProfile("Coriandre",     28,  5, 20, 10, False, ["alternariose"]),
    "thym":          CropProfile("Thym",          35, -5, 15,  8, False, ["rouille"]),
    "romarin":       CropProfile("Romarin",       35, -8, 12,  8, False, ["oïdium"]),
    "menthe":        CropProfile("Menthe",        28, -5, 30,  8, True,  ["rouille"]),
    "ciboulette":    CropProfile("Ciboulette",    25,-10, 20, 10, True,  ["rouille"]),
    "estragon":      CropProfile("Estragon",      30, -5, 20,  8, False, ["rouille"]),
    "sauge":         CropProfile("Sauge",         32, -5, 15,  8, False, ["oïdium"]),
    "laurier":       CropProfile("Laurier",       35, -5, 12,  8, False, ["oïdium"]),
    "origan":        CropProfile("Origan",        35, -5, 15,  8, False, ["rouille"]),
    "mélisse":       CropProfile("Mélisse",       28, -5, 25,  8, True,  ["rouille"]),
    "melisse":       CropProfile("Mélisse",       28, -5, 25,  8, True,  ["rouille"]),
    "lavande":       CropProfile("Lavande",       38,-10, 10,  8, False, ["phytophthora"]),

    # ──────────────────────────────────────────────
    # PETITS FRUITS (BAIES)
    # ──────────────────────────────────────────────
    "fraise":        CropProfile("Fraise",        28, -5, 40,  8, True,  ["botrytis", "oïdium"]),
    "framboise":     CropProfile("Framboise",     30,-10, 35, 10, True,  ["botrytis", "rouille"]),
    "mûre":          CropProfile("Mûre",          32,-15, 30, 10, True,  ["botrytis"]),
    "mure":          CropProfile("Mûre",          32,-15, 30, 10, True,  ["botrytis"]),
    "myrtille":      CropProfile("Myrtille",      28,-15, 45,  8, True,  ["botrytis", "anthracnose"]),
    "groseille":     CropProfile("Groseille",     28,-15, 30, 10, True,  ["oïdium"]),
    "cassis":        CropProfile("Cassis",        28,-15, 35, 10, True,  ["oïdium", "rouille"]),
    "raisin":        CropProfile("Raisin",        35, -2, 20,  8, True,  ["mildiou", "oïdium", "botrytis"]),
    "vigne":         CropProfile("Raisin",        35, -2, 20,  8, True,  ["mildiou", "oïdium", "botrytis"]),

    # ──────────────────────────────────────────────
    # ARBRES FRUITIERS TEMPÉRÉS
    # ──────────────────────────────────────────────
    "pomme":         CropProfile("Pomme",         32, -5, 25, 10, True,  ["tavelure", "oïdium"]),
    "poire":         CropProfile("Poire",         32, -5, 25, 10, True,  ["tavelure", "feu bactérien"]),
    "pêche":         CropProfile("Pêche",         35, -2, 30,  8, True,  ["cloque", "moniliose"]),
    "peche":         CropProfile("Pêche",         35, -2, 30,  8, True,  ["cloque", "moniliose"]),
    "nectarine":     CropProfile("Nectarine",     35, -2, 30,  8, True,  ["cloque", "moniliose"]),
    "abricot":       CropProfile("Abricot",       38,  0, 25,  8, True,  ["moniliose", "cloque"]),
    "cerise":        CropProfile("Cerise",        30, -2, 20,  8, True,  ["moniliose", "anthracnose"]),
    "prune":         CropProfile("Prune",         32, -3, 25,  8, True,  ["moniliose", "rouille"]),
    "figue":         CropProfile("Figue",         40,  5, 20, 10, False, ["rouille"]),
    "coing":         CropProfile("Coing",         30, -5, 20, 10, True,  ["feu bactérien", "tavelure"]),
    "noix":          CropProfile("Noyer",         32, -5, 20,  8, True,  ["anthracnose", "bactériose"]),
    "amande":        CropProfile("Amandier",      38,  0, 20,  8, True,  ["moniliose"]),
    "noisette":      CropProfile("Noisetier",     28,-10, 20,  8, True,  ["oïdium"]),
    "châtaigne":     CropProfile("Châtaignier",   30, -5, 25,  8, True,  ["encre", "chancre"]),
    "chataigne":     CropProfile("Châtaignier",   30, -5, 25,  8, True,  ["encre", "chancre"]),

    # ──────────────────────────────────────────────
    # AGRUMES
    # ──────────────────────────────────────────────
    "citron":        CropProfile("Citron",        38,  5, 30, 10, False, ["gommose"]),
    "orange":        CropProfile("Orange",        38,  5, 30, 10, False, ["gommose"]),
    "mandarine":     CropProfile("Mandarine",     38,  5, 25, 10, False, ["gommose"]),
    "clémentine":    CropProfile("Clémentine",    38,  5, 25, 10, False, ["gommose"]),
    "clementine":    CropProfile("Clémentine",    38,  5, 25, 10, False, ["gommose"]),
    "pamplemousse":  CropProfile("Pamplemousse",  38,  5, 35, 10, False, ["gommose"]),
    "citron vert":   CropProfile("Citron vert",   38, 10, 35, 10, False, ["anthracnose"]),
    "kumquat":       CropProfile("Kumquat",       35,  3, 25, 10, False, ["gommose"]),

    # ──────────────────────────────────────────────
    # FRUITS TROPICAUX & EXOTIQUES
    # ──────────────────────────────────────────────
    "mangue":        CropProfile("Mangue",        40, 12, 30,  8, True,  ["anthracnose", "oïdium"]),
    "avocat":        CropProfile("Avocat",        38,  8, 40,  8, True,  ["phytophthora"]),
    "banane":        CropProfile("Banane",        38, 12, 60,  8, True,  ["cercosporiose", "fusariose"]),
    "ananas":        CropProfile("Ananas",        38, 15, 50, 10, False, ["fusariose"]),
    "papaye":        CropProfile("Papaye",        38, 15, 50,  8, True,  ["anthracnose", "mildiou"]),
    "goyave":        CropProfile("Goyave",        40, 10, 40,  8, True,  ["anthracnose"]),
    "litchi":        CropProfile("Litchi",        38, 10, 35,  8, True,  ["anthracnose"]),
    "lychee":        CropProfile("Litchi",        38, 10, 35,  8, True,  ["anthracnose"]),
    "fruit de la passion": CropProfile("Maracuja",35, 12, 45,  8, True,  ["fusariose"]),
    "maracuja":      CropProfile("Maracuja",      35, 12, 45,  8, True,  ["fusariose"]),
    "kiwi":          CropProfile("Kiwi",          30, -5, 40, 10, True,  ["botrytis"]),
    "grenade":       CropProfile("Grenade",       40,  5, 20,  8, False, ["alternariose"]),
    "datte":         CropProfile("Dattier",       45,  5, 15,  5, False, ["bayoud"]),
    "olive":         CropProfile("Olivier",       40, -5, 10,  5, True,  ["oeil de paon", "anthracnose"]),
    "noix de coco":  CropProfile("Cocotier",      38, 18, 80,  8, True,  ["jaunissement"]),
    "cacao":         CropProfile("Cacaoyer",      35, 18, 70,  8, True,  ["phytophthora"]),
    "café":          CropProfile("Caféier",       30, 12, 50,  8, True,  ["rouille"]),
    "cafe":          CropProfile("Caféier",       30, 12, 50,  8, True,  ["rouille"]),
    "longan":        CropProfile("Longan",        38, 10, 35,  8, True,  ["anthracnose"]),
    "ramboutan":     CropProfile("Ramboutan",     38, 15, 45,  8, True,  ["anthracnose"]),
    "carambole":     CropProfile("Carambole",     35, 15, 40,  8, True,  ["anthracnose"]),
    "durian":        CropProfile("Durian",        38, 18, 60,  8, True,  ["phytophthora"]),
    "mangoustan":    CropProfile("Mangoustan",    35, 18, 50,  8, True,  ["anthracnose"]),
    "jacquier":      CropProfile("Jacquier",      38, 15, 50,  8, False, ["pourriture"]),
    "tamarin":       CropProfile("Tamarinier",    42, 10, 20,  5, False, ["anthracnose"]),
    "sapotille":     CropProfile("Sapotillier",   38, 15, 35,  8, False, ["anthracnose"]),
    "corossol":      CropProfile("Corossolier",   35, 15, 45,  8, True,  ["anthracnose"]),
    "pitaya":        CropProfile("Pitaya",        38, 10, 25,  8, False, ["anthracnose"]),
    "fruit du dragon": CropProfile("Pitaya",      38, 10, 25,  8, False, ["anthracnose"]),
    "feijoa":        CropProfile("Feijoa",        32,  2, 25,  8, False, ["anthracnose"]),
    "physalis":      CropProfile("Physalis",      28,  5, 25,  8, True,  ["botrytis"]),
}

ALIASES = {
    # English → French key
    "tomato":           "tomate",
    "potato":           "pomme de terre",
    "patate":           "pomme de terre",
    "sweet potato":     "patate douce",
    "yam":              "igname",
    "zucchini":         "courgette",
    "pepper":           "poivron",
    "hot pepper":       "piment",
    "chili":            "piment",
    "chilli":           "piment",
    "eggplant":         "aubergine",
    "cucumber":         "concombre",
    "pumpkin":          "citrouille",
    "squash":           "courge",
    "watermelon":       "pastèque",
    "carrot":           "carotte",
    "onion":            "oignon",
    "garlic":           "ail",
    "shallot":          "échalote",
    "lettuce":          "laitue",
    "salade":           "laitue",
    "spinach":          "épinard",
    "arugula":          "roquette",
    "rocket":           "roquette",
    "corn salad":       "mâche",
    "chard":            "blette",
    "swiss chard":      "blette",
    "cabbage":          "chou",
    "red cabbage":      "chou rouge",
    "cauliflower":      "chou-fleur",
    "broccoli":         "brocoli",
    "brussels sprouts": "chou de bruxelles",
    "leek":             "poireau",
    "celery":           "céleri",
    "fennel":           "fenouil",
    "beet":             "betterave",
    "beetroot":         "betterave",
    "radish":           "radis",
    "turnip":           "navet",
    "parsnip":          "panais",
    "asparagus":        "asperge",
    "artichoke":        "artichaut",
    "watercress":       "cresson",
    "bean":             "haricot",
    "green bean":       "haricot vert",
    "pea":              "petit pois",
    "broad bean":       "fève",
    "fava bean":        "fève",
    "lentil":           "lentille",
    "chickpea":         "pois chiche",
    "soybean":          "soja",
    "corn":             "maïs",
    "mais":             "maïs",
    "wheat":            "blé",
    "barley":           "orge",
    "oat":              "avoine",
    "oats":             "avoine",
    "rye":              "seigle",
    "sunflower":        "tournesol",
    "rapeseed":         "colza",
    "canola":           "colza",
    "basil":            "basilic",
    "parsley":          "persil",
    "cilantro":         "coriandre",
    "coriander":        "coriandre",
    "thyme":            "thym",
    "rosemary":         "romarin",
    "mint":             "menthe",
    "chive":            "ciboulette",
    "chives":           "ciboulette",
    "tarragon":         "estragon",
    "sage":             "sauge",
    "bay":              "laurier",
    "oregano":          "origan",
    "lemon balm":       "mélisse",
    "lavender":         "lavande",
    "strawberry":       "fraise",
    "raspberry":        "framboise",
    "blackberry":       "mûre",
    "blueberry":        "myrtille",
    "currant":          "groseille",
    "blackcurrant":     "cassis",
    "grape":            "raisin",
    "grapevine":        "vigne",
    "apple":            "pomme",
    "pear":             "poire",
    "peach":            "pêche",
    "apricot":          "abricot",
    "cherry":           "cerise",
    "plum":             "prune",
    "fig":              "figue",
    "quince":           "coing",
    "walnut":           "noix",
    "almond":           "amande",
    "hazelnut":         "noisette",
    "chestnut":         "châtaigne",
    "lemon":            "citron",
    "orange":           "orange",
    "tangerine":        "mandarine",
    "clementine":       "clémentine",
    "grapefruit":       "pamplemousse",
    "lime":             "citron vert",
    "mango":            "mangue",
    "avocado":          "avocat",
    "banana":           "banane",
    "pineapple":        "ananas",
    "papaya":           "papaye",
    "guava":            "goyave",
    "lychee":           "litchi",
    "passion fruit":    "fruit de la passion",
    "kiwi":             "kiwi",
    "pomegranate":      "grenade",
    "date":             "datte",
    "olive":            "olive",
    "coconut":          "noix de coco",
    "cacao":            "cacao",
    "cocoa":            "cacao",
    "coffee":           "café",
    "longan":           "longan",
    "rambutan":         "ramboutan",
    "starfruit":        "carambole",
    "durian":           "durian",
    "mangosteen":       "mangoustan",
    "jackfruit":        "jacquier",
    "tamarind":         "tamarin",
    "sapodilla":        "sapotille",
    "soursop":          "corossol",
    "dragon fruit":     "pitaya",
    "feijoa":           "feijoa",
    "cape gooseberry":  "physalis",
    "okra":             "gombo",
    "pak choy":         "pak choï",
    "bok choy":         "pak choï",
    "bok choi":         "pak choï",
    "ginger":           "gingembre",
    "turmeric":         "curcuma",
    "cassava":          "manioc",
    "taro":             "taro",
    "sunchoke":         "topinambour",
    "jerusalem artichoke": "topinambour",
}


def normalize_crop_name(name: str) -> str:
    name = name.strip().lower()
    return ALIASES.get(name, name)


def get_crop(name: str) -> Optional[CropProfile]:
    normalized_name = normalize_crop_name(name)
    return CROPS.get(normalized_name)


def advice_for_crops(forecast: WeatherForecastResponse, crops: list[str]) -> CropAdviceResponse:
    if not forecast.daily:
        return CropAdviceResponse(
            crops=[c.strip().lower() for c in crops if c.strip()],
            summary="Aucune donnée météo disponible.",
            actions=[
                CropAction(
                    title="Météo indisponible",
                    reason="Impossible de générer des conseils sans prévisions météo.",
                    when="Réessayez plus tard",
                    priority="medium",
                )
            ],
            raw_forecast=forecast,
        )

    cleaned_crops = [c.strip() for c in crops if c.strip()]
    actions: list[CropAction] = []

    total_rain = sum(d.precipitation_mm for d in forecast.daily)
    max_wind = max(d.wind_max_kmh for d in forecast.daily)
    max_temp = max(d.temp_max for d in forecast.daily)
    min_temp = min(d.temp_min for d in forecast.daily)

    hot_days = sum(1 for d in forecast.daily if d.temp_max >= 32)
    cold_nights = sum(1 for d in forecast.daily if d.temp_min <= 5)
    rainy_days = sum(1 for d in forecast.daily if d.precipitation_mm >= 10)

    crop_profiles: list[CropProfile] = []
    seen_names = set()

    for crop in cleaned_crops:
        profile = get_crop(crop)
        if profile and profile.name not in seen_names:
            crop_profiles.append(profile)
            seen_names.add(profile.name)

    if not crop_profiles:
        return CropAdviceResponse(
            crops=[c.lower() for c in cleaned_crops],
            summary="Culture inconnue.",
            actions=[
                CropAction(
                    title="Culture non reconnue",
                    reason="Vérifiez le nom de vos cultures.",
                    when="Maintenant",
                    priority="low",
                )
            ],
            raw_forecast=forecast,
        )

    if min_temp <= 0:
        frost_crops = [p.name for p in crop_profiles if min_temp < p.temp_min_critical]
        if frost_crops:
            actions.append(
                CropAction(
                    title="🚨 Attention au gel !",
                    reason=f"Il va faire {min_temp:.0f}°C cette nuit. Vos plantes peuvent souffrir ou mourir. Couvrez-les avec un tissu, un voile ou un plastique adapté.",
                    when="Ce soir avant la nuit",
                    priority="critical",
                )
            )
    elif cold_nights >= 2:
        actions.append(
            CropAction(
                title="⚠️ Nuits froides",
                reason=f"{cold_nights} nuits froides à environ {min_temp:.0f}°C sont prévues. Vos plantes risquent de pousser moins vite.",
                when="Surveillez vos plantes cette semaine",
                priority="medium",
            )
        )

    if max_temp >= 38:
        actions.append(
            CropAction(
                title="🔥 Très forte chaleur",
                reason=f"Des températures jusqu'à {max_temp:.0f}°C sont prévues. Vos plantes risquent un stress hydrique important.",
                when="Matin (6h-8h) et soir (18h-20h)",
                priority="critical",
            )
        )
    elif hot_days >= 2:
        actions.append(
            CropAction(
                title="☀️ Temps chaud",
                reason=f"{hot_days} jours très chauds sont prévus. Arrosez plus souvent que d'habitude.",
                when="Tôt le matin ou le soir",
                priority="high",
            )
        )

    avg_water_need = sum(p.water_per_week for p in crop_profiles) / len(crop_profiles)

    if total_rain < avg_water_need * 0.3:
        liters_per_10m2 = max(0, int((avg_water_need - total_rain) * 10))
        actions.append(
            CropAction(
                title="💧 Arrosez vos plantes",
                reason=f"Très peu de pluie est prévue. Donnez environ {liters_per_10m2} litres d'eau pour chaque 10m², répartis sur 2 à 3 arrosages.",
                when="2 à 3 fois cette semaine",
                priority="high",
            )
        )
    elif total_rain < avg_water_need * 0.7:
        liters_per_10m2 = max(0, int((avg_water_need - total_rain) * 10))
        actions.append(
            CropAction(
                title="💧 Un peu d'eau en plus",
                reason=f"La pluie prévue semble insuffisante ({total_rain:.0f} mm). Ajoutez environ {liters_per_10m2} litres d'eau pour 10m².",
                when="1 à 2 fois cette semaine",
                priority="medium",
            )
        )

    if rainy_days >= 2:
        sensitive_crops = [p for p in crop_profiles if p.is_fungal_sensitive]
        if sensitive_crops:
            crop_names = ", ".join(p.name for p in sensitive_crops)
            actions.append(
                CropAction(
                    title="🍄 Risque de maladies",
                    reason=f"{rainy_days} jours de pluie augmentent le risque de maladies fongiques sur : {crop_names}. Surveillez les feuilles et envisagez un traitement préventif adapté.",
                    when="Avant la pluie et dans les jours qui suivent",
                    priority="critical",
                )
            )

    if max_wind >= 50:
        actions.append(
            CropAction(
                title="💨 Vent fort",
                reason=f"Le vent peut atteindre {max_wind:.0f} km/h. Certaines plantes peuvent se coucher ou se casser.",
                when="Avant l'épisode venteux",
                priority="high",
            )
        )

    # ──────────────────────────────────────────────
    # CONSEILS SPÉCIFIQUES PAR CULTURE
    # ──────────────────────────────────────────────
    for profile in crop_profiles:
        if profile.name == "Tomate" and rainy_days == 0:
            actions.append(CropAction(
                title="🍅 Conseils Tomate",
                reason="Arrosez au pied de la plante, jamais sur les feuilles. Supprimez les gourmands pour concentrer l'énergie sur les fruits.",
                when="Chaque semaine", priority="low",
            ))
        elif profile.name == "Pomme de terre" and rainy_days == 0:
            actions.append(CropAction(
                title="🥔 Conseils Pomme de terre",
                reason="Buttez les plants quand ils atteignent environ 15 cm pour protéger les tubercules de la lumière et surveillez les feuilles.",
                when="Cette semaine si les plants sont assez développés", priority="low",
            ))
        elif profile.name == "Carotte":
            actions.append(CropAction(
                title="🥕 Conseils Carotte",
                reason="Gardez le sol légèrement humide et retirez régulièrement les mauvaises herbes autour des plants.",
                when="Régulièrement", priority="low",
            ))
        elif profile.name == "Laitue":
            actions.append(CropAction(
                title="🥬 Conseils Laitue",
                reason="La laitue supporte mal le plein soleil intense. Donnez-lui un peu d'ombre l'après-midi si possible et arrosez davantage en période chaude.",
                when="Tous les jours si besoin", priority="low",
            ))
        elif profile.name == "Fraise":
            actions.append(CropAction(
                title="🍓 Conseils Fraise",
                reason="Paillez le sol pour conserver l'humidité et éviter l'éclaboussure de terre sur les fruits. Supprimez les stolons non désirés.",
                when="Régulièrement", priority="low",
            ))
        elif profile.name == "Raisin":
            actions.append(CropAction(
                title="🍇 Conseils Vigne",
                reason="Surveillez attentivement le mildiou et l'oïdium. Aérez le feuillage par une taille en vert et traitez préventivement avant les épisodes pluvieux.",
                when="Chaque semaine en période de végétation", priority="low",
            ))
        elif profile.name in ("Pomme", "Poire"):
            actions.append(CropAction(
                title=f"🍎 Conseils {profile.name}",
                reason=f"Surveillez la tavelure après chaque pluie. Retirez les fruits momifiés et pratiquez l'éclaircissage pour obtenir de beaux fruits.",
                when="Après chaque épisode pluvieux", priority="low",
            ))
        elif profile.name in ("Pêche", "Nectarine", "Abricot"):
            actions.append(CropAction(
                title=f"🍑 Conseils {profile.name}",
                reason="Traitez contre la cloque du pêcher dès le gonflement des bourgeons au printemps. Retirez les fruits touchés par la moniliose immédiatement.",
                when="Au stade gonflement des bourgeons", priority="low",
            ))
        elif profile.name == "Courgette":
            actions.append(CropAction(
                title="🥒 Conseils Courgette",
                reason="Récoltez régulièrement pour stimuler la production. Surveillez l'oïdium sur les feuilles et améliorez la circulation d'air.",
                when="Tous les 2-3 jours", priority="low",
            ))
        elif profile.name in ("Melon", "Pastèque"):
            actions.append(CropAction(
                title=f"🍈 Conseils {profile.name}",
                reason="Limitez les arrosages à l'approche de la maturité pour concentrer les sucres. Posez les fruits sur une tuile pour éviter le contact avec la terre humide.",
                when="3 semaines avant récolte", priority="low",
            ))
        elif profile.name == "Mangue":
            actions.append(CropAction(
                title="🥭 Conseils Mangue",
                reason="Traitez préventivement contre l'anthracnose avant la floraison. Évitez l'irrigation par aspersion qui favorise les maladies fongiques.",
                when="Avant floraison", priority="low",
            ))
        elif profile.name == "Avocat":
            actions.append(CropAction(
                title="🥑 Conseils Avocat",
                reason="L'avocat craint les sols gorgés d'eau (phytophthora). Assurez un excellent drainage et évitez les excès d'arrosage.",
                when="En permanence", priority="low",
            ))
        elif profile.name == "Banane":
            actions.append(CropAction(
                title="🍌 Conseils Bananier",
                reason="Retirez les feuilles sèches pour limiter les maladies. Après la récolte, coupez le pseudo-tronc ayant fructifié pour laisser place aux rejets.",
                when="Après la récolte", priority="low",
            ))
        elif profile.name == "Citron" or profile.name in ("Orange", "Mandarine", "Clémentine"):
            actions.append(CropAction(
                title="🍋 Conseils Agrumes",
                reason="Les agrumes apprécient un sol légèrement acide. Apportez un engrais riche en magnésium au printemps et surveillez la cochenille.",
                when="Printemps et été", priority="low",
            ))
        elif profile.name == "Basilic":
            actions.append(CropAction(
                title="🌿 Conseils Basilic",
                reason="Pincez régulièrement les sommités florales pour prolonger la production. Le basilic déteste le froid et les courants d'air.",
                when="Toutes les semaines", priority="low",
            ))
        elif profile.name in ("Haricot", "Haricot vert"):
            actions.append(CropAction(
                title="🫘 Conseils Haricot",
                reason="Récoltez les gousses avant qu'elles ne soient trop grosses pour stimuler la production. Évitez d'arroser le soir pour limiter la rouille.",
                when="Tous les 2 jours en pleine production", priority="low",
            ))
        elif profile.name == "Maïs":
            actions.append(CropAction(
                title="🌽 Conseils Maïs",
                reason="Plantez en bloc plutôt qu'en rangs simples pour assurer une bonne pollinisation par le vent. Buttez les pieds pour améliorer l'ancrage.",
                when="Au stade 30 cm", priority="low",
            ))
        elif profile.name == "Framboise":
            actions.append(CropAction(
                title="🫐 Conseils Framboise",
                reason="Après la récolte, coupez les cannes ayant fructifié au ras du sol. Tuteurez les nouvelles cannes pour l'hiver.",
                when="Après la récolte", priority="low",
            ))
        elif profile.name == "Patate douce":
            actions.append(CropAction(
                title="🍠 Conseils Patate douce",
                reason="La patate douce adore la chaleur. Couvrez le sol d'un paillis sombre pour réchauffer la terre et limiter les adventices.",
                when="Toute la saison", priority="low",
            ))
        elif profile.name == "Ail":
            actions.append(CropAction(
                title="🧄 Conseils Ail",
                reason="Arrêtez d'arroser dès que les feuilles jaunissent : c'est le signe que les bulbes sont prêts. Laissez sécher à l'ombre avant stockage.",
                when="Fin de saison", priority="low",
            ))
        elif profile.name == "Oignon":
            actions.append(CropAction(
                title="🧅 Conseils Oignon",
                reason="Rabattez les feuilles au sol pour hâter la maturation des bulbes. Récoltez par temps sec et laissez ressuer avant stockage.",
                when="Quand les feuilles commencent à tomber", priority="low",
            ))
        elif profile.name == "Épinard":
            actions.append(CropAction(
                title="🥬 Conseils Épinard",
                reason="L'épinard monte vite en graines par forte chaleur. Privilégiez les semis de printemps et d'automne, et récoltez les feuilles extérieures en premier.",
                when="Printemps et automne", priority="low",
            ))
        elif profile.name == "Brocoli":
            actions.append(CropAction(
                title="🥦 Conseils Brocoli",
                reason="Récoltez la pomme principale avant qu'elle ne fleurisse. Des pousses latérales apparaîtront et pourront être récoltées plusieurs semaines de suite.",
                when="Dès que la pomme est formée", priority="low",
            ))
        elif profile.name == "Tomate":
            pass  # Already handled above
        elif profile.name == "Poireau":
            actions.append(CropAction(
                title="🌱 Conseils Poireau",
                reason="Buttez progressivement les poireaux pour blanchir le fût et améliorer la tendreté. Un paillage aide à conserver l'humidité.",
                when="Toutes les 2-3 semaines", priority="low",
            ))
        elif profile.name == "Céleri":
            actions.append(CropAction(
                title="🌿 Conseils Céleri",
                reason="Le céleri est très gourmand en eau. Ne laissez jamais le sol se dessécher et apportez régulièrement un engrais azoté.",
                when="Tout au long de la saison", priority="low",
            ))
        elif profile.name == "Concombre":
            actions.append(CropAction(
                title="🥒 Conseils Concombre",
                reason="Récoltez fréquemment pour maintenir la production. Pincez la tige principale après quelques feuilles pour favoriser les ramifications.",
                when="Tous les 2 jours", priority="low",
            ))
        elif profile.name == "Piment":
            actions.append(CropAction(
                title="🌶️ Conseils Piment",
                reason="Les piments aiment la chaleur et le soleil. Évitez les excès d'azote qui favorisent le feuillage au détriment des fruits.",
                when="Toute la saison", priority="low",
            ))

    # ──────────────────────────────────────────────
    # RÉSUMÉ
    # ──────────────────────────────────────────────
    summary_parts = []

    if max_temp >= 35:
        summary_parts.append(f"Très chaud ({max_temp:.0f}°C)")
    elif max_temp >= 28:
        summary_parts.append(f"Chaud ({max_temp:.0f}°C)")
    elif min_temp <= 5:
        summary_parts.append(f"Froid la nuit ({min_temp:.0f}°C)")
    else:
        summary_parts.append(f"Températures normales ({min_temp:.0f}-{max_temp:.0f}°C)")

    if total_rain == 0:
        summary_parts.append("Pas de pluie")
    elif total_rain < 10:
        summary_parts.append("Peu de pluie")
    else:
        summary_parts.append(f"Pluie ({total_rain:.0f} mm)")

    if max_wind >= 50:
        summary_parts.append(f"Vent fort ({max_wind:.0f} km/h)")

    summary = "Cette semaine : " + " • ".join(summary_parts)

    return CropAdviceResponse(
        crops=[normalize_crop_name(c) for c in cleaned_crops],
        summary=summary,
        actions=actions,
        raw_forecast=forecast,
    )