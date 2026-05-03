# Babel, effective CMMS made simple

Streamlining interventions, history and documentation management, a tailor-made solution.

## pillars [todo]

1) basic CRUD: (forms, tied to db models, simply speaking)
    - add devices
    - add document templates (intervention documents, work permits etc.)
    - generate documents
        - pdf
        - word
        - json
        - csv (from sql table to csv might be an easy pipeline)
    - add tasks (interventions)
2) accounts and permissions management:
    - hierarchy and validation (engineer validates technician i.e: who gets to intervene and in which department/device etc)
3) trend analysis (history analysis through, a statistics and possibly machine learning approach)
    - what device is more likely to break at a certain time of the year or given certain atmosphere readings (temperature, humidity etc)
4) data samples for demo purposes (FakerPy, or external datasets)
    - zombie script to poupulate the db: add devices and simulate user interactions to get enough data for trend analysis (fakerpy might help)
5) UX
    - UI, dashboard, recent activities, interventions heatmap (which device has been repaired/maintained the most) etc.
6) deployment
    - Docker image setup

## technical details

- backend:
    - server:
        - Python (FastAPI)
    - DBMS:
        - SQLITE + SQLAlchemy
    - Frontend:
        - Jinja2 templates
        - (a websocket solution to add fuzzy db search)
        - possibly htmlx or react (or any solution to take care of AJAX and reactivity)
    - Data analysis:
        - ?
