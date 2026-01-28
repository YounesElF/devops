# J1 – Lab 6.3.6 (CI/CD met Docker)

## Doel
Deze oefening demonstreert **Lab 6.3.6** uit de DevNet Associate cursus:
het **manueel bouwen en runnen van een Docker image** als voorbereiding
op automatisatie met Jenkins.

## Inhoud
- Flask webapplicatie
- Dockerfile om een image te bouwen
- Container run + test via curl
- Basis CI/CD-denken (build → run → test)

## Bestanden
- `app.py`  
  Simpele Flask webservice met `/` en `/health`

- `Dockerfile`  
  Bouwt een Docker image voor de Flask applicatie

- (optioneel) `Jenkinsfile`  
  Wordt gebruikt wanneer dit lab in Jenkins wordt uitgevoerd

## Manueel runnen (samenvatting)
```bash
docker build -t j1-sample-app .
docker run -p 5555:5555 j1-sample-app
curl http://127.0.0.1:5555/health

