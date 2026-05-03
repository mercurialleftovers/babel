# Babel, GMAO simple et efficace

Faciliter la gestion des intervention, historiques, et documentation, a travers d'un solution personalize et adaptive.

## pilliers

1) fonctions de gestion basiques (CRUD): (forms lies aux base de donnes)
    - adjouter des equipements
    - ajouter des documents et des modeles a suivre (templates)
    - generer des documents d'apres les formules:
        - pdf
        - word
        - json
        - csv
    - ajouter des taches (des interventions)
2) gestion des comptes et des permissions
    - hierarchie et validation (un ingenieur par ex peut valider le demande d'intervention d'un technicien etc)
3) analyses intelligent d'historique a travers des modeles de statistique et possiblement le machine learning
    - quelles sont les equipements les plus probables d'avoir une panne, et dans quelles periodes et circonstances (temperatures, humidites, saison etc.)
4) insertion des donnes exemplaires:
    - un script qui automatise la creation et les insertions des samples, a fin d'avoir une matiere preliminaire qu'on peut analyser, et fair des demos
5) UX
    - interface, dashbord, activites recentes, map des interventions, equipments plus intervenes etc.
6) deployement
    - Creation d'une image Docker pour faciliter l'installtion et le demo du projet

## details techniques:

- backend:
    - serveur:
        - Python (FastAPI)
    - SGBD:
        - SQLite + SQLAlchemy
    - Frontend:
        - Jinja2 templates
        - (un solution websocket pour faire le recherche dynamique instantanne avec la base de donne - fuzzy finding-)
        - htmlx ou react possiblement (pour avoir une interface live et reactive)
    - Analyse de donnes d'hitorique:
        - ?
