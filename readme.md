# Babel, effective CMMS made simple

## pillars [todo]

1) basic CRUD:
    - add devices
    - add document templates
    - generate documents
        - pdf
        - word
        - json
        - csv (from sql table to csv might be an easy task)
    - add tasks (interventions)
2) accounts and permissions managements:
    - hierarchy and validation (engineer validates technician etc)
3) trend analysis (statistics and possibly machine learning)
    - what device is more likely to break at a certain time of the year or given certain atmosphere readings (temperature, humidity etc)
4) data samples for demo purposes
    - zombie script to poupulate the db: add devices and simulate user interactions to get enough data for trend analysis (fakerpy might help)
5) UX
    - UI, dashboard, recent activities, interventions heatmap (which device has been repaired/maintained the most) etc.
6) deployment
    - Docker image setup
