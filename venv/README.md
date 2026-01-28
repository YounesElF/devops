# Python Virtual Environments (venv)

## Doel
Deze map bevat **Python virtual environments** die gebruikt worden
voor DevNet / DevOps / CI-CD oefeningen.

Elke submap is een **afzonderlijke virtual environment** met
zijn eigen Python interpreter en packages.

---

## Waarom virtual environments?
- Scheiding van dependencies per project
- Geen conflicten tussen Python libraries
- Reproduceerbare labs en oefeningen
- Best practice binnen DevNet & DevOps

---

## Structuur
- `pv1_venv/`  
  Virtual environment voor Pv1 labs

- `pv2_deploy/`  
  Virtual environment voor Pv2 deployment-oefeningen

---

## Activeren van een venv
```bash
source <venv_naam>/bin/activate

