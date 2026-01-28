# pv2_deploy – Python Virtual Environment (Deployment & CI/CD)

## Doel
Deze virtual environment wordt gebruikt voor **Pv2 deployment-gerichte labs**
binnen de DevNet Associate cursus.

De focus ligt op:
- Flask webservices
- Docker experiments
- CI/CD voorbereiding
- Jenkins pipeline tests (lokaal)

---

## Waarom een aparte virtual environment?
Pv2 combineert Python met:
- containers
- automatisatie
- deployment tools

Daarom worden hier **andere Python dependencies** gebruikt dan bij Pv1.
Een aparte venv voorkomt conflicten en maakt troubleshooting eenvoudiger.

---

## Gebruik

### Activeren
```bash
source pv2_deploy/bin/activate

