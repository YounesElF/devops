# J2 – Eigen Pipeline Experiment (Jenkins + Docker)

## Doel
Deze oefening demonstreert een **eigen Jenkins Pipeline experiment**
gebaseerd op DevNet Associate CI/CD-concepten.

De focus ligt op:
- Jenkins Declarative Pipeline
- Docker image build
- Container run + test
- Automatische cleanup

Deze oefening is **bewust eenvoudig** gehouden om de pipeline-logica
duidelijk te maken.

---

## Pipeline Overzicht
De Jenkins pipeline voert volgende stappen uit:

1. **Prepare**
   - Controleert workspace en Docker beschikbaarheid

2. **Build Image**
   - Bouwt een Docker image met een Flask webservice

3. **Run Container**
   - Start de container op een vaste host-poort (bv. 5560)

4. **Test**
   - Test `/health` endpoint met `curl`

5. **Cleanup (altijd)**
   - Stopt container
   - Verwijdert container en image

---

## Bestanden in deze map

- `app.py`  
  Simpele Flask webservice met:
  - `/` → testpagina
  - `/health` → health-check endpoint

- `Dockerfile`  
  Bouwt een Docker image voor de Flask applicatie

- `Jenkinsfile`  
  Declarative Jenkins Pipeline die het volledige proces automatiseert

---

## Vereisten
- Jenkins (Pipeline job)
- Docker geïnstalleerd op Jenkins host
- Jenkins user heeft toegang tot Docker
- Vrije host-poort (standaard: 5560)

---

## Jenkins configuratie
- Job type: **Pipeline**
- Pipeline definitie:
  - *Pipeline script from SCM*  
    of
  - *Pipeline script* (Jenkinsfile plakken)

---

## Lokale test (optioneel, zonder Jenkins)

```bash
docker build -t j2-pipeline-app:1.0 .
docker run -d --rm -p 5560:5555 --name j2-test j2-pipeline-app:1.0
curl http://127.0.0.1:5560/health
docker stop j2-test

