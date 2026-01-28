# Webex API Experiment (Python)

## 📌 Beschrijving
Dit project is een **Webex API experiment** uitgevoerd in het kader van **DEVASC / DevNet Associate**.  
Het doel van deze oefening is om te tonen hoe je met **Python** en de **Webex REST API**:

- authenticatie uitvoert met een **Bearer token**
- Webex resources ophaalt met **GET**
- Webex resources aanmaakt met **POST**
- JSON responses verwerkt

---

## 🎯 Doelstellingen
Met deze oefening toon ik aan dat ik:
- REST API’s kan gebruiken met Python
- Bearer token authenticatie begrijp
- HTTP methods (GET, POST) correct kan toepassen
- API responses kan lezen en interpreteren

---

## 📂 Bestanden
| Bestand | Beschrijving |
|------|-------------|
| `auth.py` | Bevat de Webex authenticatie (token uit environment variable) |
| `list_rooms.py` | Haalt de lijst van Webex rooms op (GET) |
| `create_rooms.py` | Maakt een nieuwe Webex room aan (POST) |
| `add_members.py` | Voegt een gebruiker toe aan een Webex room |
| `test_token.py` | Test of de Webex token geldig is |

---

## 🔐 Authenticatie
De Webex API gebruikt **Bearer Token Authentication**.

De token wordt **niet hardcoded**, maar via een environment variable ingesteld:

```bash
export WEBEX_TOKEN="JOUW_WEBEX_TOKEN_HIER"

