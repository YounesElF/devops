# Python Unit Test Experiment

## 📌 Beschrijving
Dit project bevat een **Python unittest-experiment** waarin een functie wordt getest die **recursief zoekt in JSON-data**.  
De oefening toont hoe **unit testing** wordt gebruikt om code correctheid te verifiëren.

Deze oefening is uitgevoerd in het kader van **DEVASC / DevNet Associate**.

---

## 🎯 Doelstellingen
Met deze oefening toon ik aan dat ik:
- Python **unittests** kan schrijven met het `unittest` framework
- functies kan testen met **verwachte en onverwachte input**
- JSON-data kan verwerken en analyseren
- testbestanden logisch kan structureren

---

## 📂 Bestanden
| Bestand | Beschrijving |
|------|-------------|
| `recursive_json_search.py` | Bevat de functie `json_search()` die recursief zoekt in JSON |
| `test_data.py` | Bevat voorbeeld JSON-data en test keys |
| `test_json_search.py` | Bevat de unit tests voor `json_search()` |

---

## 🧠 Functionaliteit
De functie `json_search(key, data)`:
- doorzoekt geneste JSON-objecten (dicts en lists)
- zoekt naar een opgegeven sleutel (`key`)
- retourneert een **lijst** met gevonden resultaten

---

## 🧪 Unit Tests
De volgende zaken worden getest:

- ✅ Of een bestaande key gevonden wordt
- ❌ Of een niet-bestaande key een lege lijst retourneert
- 📋 Of het resultaat altijd een lijst is

De tests zijn geschreven met het ingebouwde Python `unittest` framework.

---

## ▶️ Tests uitvoeren

Ga naar de map met de bestanden en voer uit:

```bash
python3 test_json_search.py

