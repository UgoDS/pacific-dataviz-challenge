from dataclasses import dataclass

LIST_FRUITS = ["AIL", "ANANAS", "AUBERGINE", "AUTRES FRUITS", "AUTRES LEGUMES", "AVOCAT", "BANANE DESSERT", "BROCOLI", "CAROTTE", "CELERI", "CHOU DE CHINE", "CHOU FLEUR", "CHOU ROUGE", "CHOU VERT ET BLANC", "CHOUCHOUTE", "CITRON ET LIME", "CONCOMBRE", "COURGETTE", "HARICOT VERT ET BEURRE", "LETCHI", "MAIS DOUX", "MANDARINE", "MANGUE", "MELON", "NAVET", "NECTARINE", "OIGNONS", "OIGNONS VERT", "ORANGE", "PAMPLEMOUSSE ET POMELO", "PAPAYE", "PASTEQUE", "PATATES DOUCES", "PERSIL CHINOIS", "PERSIL FRANCAIS", "POIREAU", "POIVRONS", "POMME CANELLE", "POMME LIANE", "RADIS", "SALADES", "TANGELO"]

@dataclass
class FruitItem:
    annee: str
    mois: str
    regroupement1: str
    regroupement2: str
    poids_enquete_kg: int
    poids_mg_kg: float
    valeur_tot_mg_fr: int
    valeur_moy: float