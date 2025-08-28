# 🇦🇹 Österreichische Rechnungsvorlagen Prompt-Sammlung 2025
## Premium KI-Prompt Collection für Claude & ChatGPT

---

## 📋 Inhaltsverzeichnis

1. [Handwerker Classic - Tiroler Tradition](#1-handwerker-classic---tiroler-tradition)
2. [Solar/PV Modern - Mission Solar Style](#2-solarpv-modern---mission-solar-style)
3. [IT-Dienstleister Professional](#3-it-dienstleister-professional)
4. [Kleinunternehmer Minimal](#4-kleinunternehmer-minimal)
5. [B2B Reverse Charge EU](#5-b2b-reverse-charge-eu)
6. [Beratung Premium](#6-beratung-premium)
7. [Tourismus Dreisprachig](#7-tourismus-dreisprachig)
8. [Bau & VOB Abschlagsrechnung](#8-bau--vob-abschlagsrechnung)
9. [Freelancer Creative](#9-freelancer-creative)
10. [E-Commerce Modern](#10-e-commerce-modern)
11. [Rechtsanwalt Formal](#11-rechtsanwalt-formal)
12. [Gastgewerbe Restaurant](#12-gastgewerbe-restaurant)
13. [Immobilienverwaltung](#13-immobilienverwaltung)
14. [Energiegemeinschaft NEU](#14-energiegemeinschaft-neu)
15. [Startup Minimalist](#15-startup-minimalist)

---

## Template 1: Handwerker Classic - Tiroler Tradition

### 1.1 Initial Master Template Prompt

```
Erstelle eine HTML-Rechnungsvorlage für einen österreichischen Handwerksbetrieb mit folgenden Spezifikationen:

DESIGN:
- Klassisches A4-Format mit konservativem blau-grauem Farbschema
- Firmenlogo oben rechts (150x60px Platzhalter)
- Strukturierte Tabelle mit klarer Material-Arbeitszeit-Trennung
- Tiroler Wappen dezent als Wasserzeichen (10% Opacity)

PFLICHTFELDER gemäß §11 UStG:
- Vollständiger Firmenkopf mit österreichischer Adresse
- Fortlaufende Rechnungsnummer Format: RE-2025-XXXXX
- UID-Nummer Format: ATU12345678
- Leistungsdatum/Zeitraum mit österreichischem Datumsformat (TT.MM.JJJJ)
- Detaillierte Leistungsbeschreibung mit getrennten Spalten für:
  * Materialkosten (10% oder 20% USt)
  * Arbeitskosten (20% USt) - wichtig für steuerliche Absetzbarkeit
  * Fahrtkosten/Pauschalen

SPEZIELLE ELEMENTE:
- Handwerkerbonus-Hinweis für Privatkunden
- Gewährleistungshinweis nach österreichischem Recht (2 Jahre)
- Zahlungsziel: "14 Tage 2% Skonto, 30 Tage netto"
- Bankverbindung mit österreichischer IBAN (AT...)
- Gerichtsstand und Firmenbuchnummer

FOOTER:
- Geschäftsführer-Namen
- Kontaktdaten (Tel, Email, Web)
- "Mitglied der WKO Tirol - Landesinnung [Gewerk]"

Verwende Platzhalter im Format {{feldname}} für alle variablen Daten.
```

### 1.2 Master Template mit Mock-Daten JSON

```json
{
  "firma": {
    "name": "Elektro Huber GmbH",
    "zusatz": "Ihr Meisterbetrieb seit 1985",
    "strasse": "Handwerkerstraße 12",
    "plz": "6020",
    "ort": "Innsbruck",
    "land": "Österreich",
    "telefon": "+43 512 123456",
    "email": "office@elektro-huber.at",
    "web": "www.elektro-huber.at",
    "uid": "ATU12345678",
    "firmenbuch": "FN 123456a",
    "gericht": "Landesgericht Innsbruck",
    "geschaeftsfuehrer": "Johann Huber",
    "bank": "Tiroler Sparkasse",
    "iban": "AT12 2050 3033 0152 3006",
    "bic": "SPIHAT22XXX"
  },
  "kunde": {
    "anrede": "Sehr geehrte",
    "titel": "",
    "vorname": "Maria",
    "nachname": "Berger",
    "firma": "",
    "strasse": "Hauptplatz 7",
    "plz": "6020",
    "ort": "Innsbruck",
    "uid": ""
  },
  "rechnung": {
    "nummer": "RE-2025-00142",
    "datum": "15.03.2025",
    "leistungszeitraum": "01.03.2025 - 14.03.2025",
    "zahlungsziel": "14.04.2025",
    "betreff": "Elektroinstallation Wohnungsrenovierung"
  },
  "positionen": [
    {
      "typ": "material",
      "beschreibung": "Sicherungskasten ABB 3-reihig",
      "menge": 1,
      "einheit": "Stk",
      "einzelpreis": 285.50,
      "steuersatz": 20,
      "gesamt": 285.50
    },
    {
      "typ": "material",
      "beschreibung": "NYM-J 3x1,5 mm² Kabel",
      "menge": 120,
      "einheit": "m",
      "einzelpreis": 1.85,
      "steuersatz": 20,
      "gesamt": 222.00
    },
    {
      "typ": "arbeit",
      "beschreibung": "Elektroinstallation durch Meister",
      "menge": 16,
      "einheit": "Std",
      "einzelpreis": 78.00,
      "steuersatz": 20,
      "gesamt": 1248.00
    },
    {
      "typ": "arbeit",
      "beschreibung": "Elektroinstallation durch Geselle",
      "menge": 24,
      "einheit": "Std",
      "einzelpreis": 62.00,
      "steuersatz": 20,
      "gesamt": 1488.00
    },
    {
      "typ": "fahrt",
      "beschreibung": "Fahrtkostenpauschale Innsbruck",
      "menge": 4,
      "einheit": "Fahrten",
      "einzelpreis": 25.00,
      "steuersatz": 20,
      "gesamt": 100.00
    }
  ],
  "zusammenfassung": {
    "material_netto": 507.50,
    "arbeit_netto": 2736.00,
    "fahrt_netto": 100.00,
    "summe_netto": 3343.50,
    "ust_20": 668.70,
    "summe_brutto": 4012.20,
    "skonto_betrag": 80.24,
    "skonto_endbetrag": 3931.96
  },
  "zusatzinfo": {
    "handwerkerbonus": "Hinweis: Die Arbeitskosten (2.736,00 €) können gemäß § 35a EStG als Handwerkerleistungen steuerlich geltend gemacht werden.",
    "gewaehrleistung": "Auf unsere Leistungen gewähren wir 2 Jahre Gewährleistung gemäß österreichischem Recht.",
    "wko": "Mitglied der WKO Tirol - Landesinnung der Elektrotechniker"
  }
}
```

### 1.3 Fill-Up Prompt für neue Rechnungen

```
Nimm das Handwerker-Master-Template und fülle es mit den Daten aus der JSON-Datei. 
Beachte dabei:

1. Ersetze alle {{placeholder}} mit den entsprechenden Werten aus dem JSON
2. Formatiere alle Währungsbeträge mit österreichischem Format: 1.234,56 €
3. Berechne automatisch:
   - Einzelne Positionsbeträge (Menge × Einzelpreis)
   - Steuersätze korrekt zuordnen (Material und Arbeit meist 20%, Lebensmittel 10%)
   - Netto-Zwischensummen nach Kategorien
   - USt-Beträge pro Steuersatz
   - Brutto-Endsumme
   - Skontobetrag bei 2% und Endpreis mit Skonto

4. Generiere den Dateinamen nach Schema: 
   rechnung_[rechnungsnummer]_[kundenname]_[datum].html
   Beispiel: rechnung_RE-2025-00142_berger_20250315.html

5. Füge automatisch Textbausteine ein:
   - Bei Privatpersonen: Handwerkerbonus-Hinweis
   - Bei B2B mit UID: "Zahlung ohne Abzug" statt Skonto
   - Saisonale Grüße (Weihnachten, Ostern) wenn zutreffend

6. Validiere dass alle Pflichtangaben gemäß §11 UStG vorhanden sind
```

---

## Template 2: Solar/PV Modern - Mission Solar Style

### 2.1 Initial Master Template Prompt

```
Erstelle eine moderne HTML-Rechnungsvorlage für einen österreichischen Solar/PV-Installateur mit innovativem Design:

DESIGN-KONZEPT "Solar Energy":
- Farbschema: Sonnengelb (#FFB800), Tiefblau (#003D7A), Hellgrau (#F5F5F5)
- Header mit Gradient von Gelb zu Blau (Sonnenaufgang-Effekt)
- Minimalistisches Logo-Placement links, Solarpanel-Icon rechts
- Clean Sans-Serif Fonts (Helvetica Neue, Arial)
- Subtle Shadow-Effects für Depth

SPEZIELLE SOLAR-ELEMENTE:
- CO2-Einsparung Berechnung als Highlight-Box
- Förderhinweis-Sektion für österreichische Förderungen
- KJUUBE/NTUITY Produktcodes für Speichersysteme
- Energieertrag-Prognose in kWh/Jahr
- Amortisationszeit-Indikator

PFLICHTANGABEN erweitert um:
- Anlagengröße in kWp
- Module & Wechselrichter Seriennummern (Garantie)
- Netzanschluss-Referenznummer
- Installateur-Konzessionsnummer
- Hinweis auf Photovoltaik-Techniker-Zertifikat

SMART PAYMENT:
- QR-Code für Sofortüberweisung (EPC-Standard)
- Ratenzahlung-Option für Beträge >10.000€
- Förderabwicklungs-Service Hinweis

NACHHALTIGKEIT:
- "Klimaaktiv Partner" Badge
- Recycling-Hinweis für Altmodule
- Lokale Wertschöpfung Tirol Statement

FOOTER erweitert:
- Social Media Icons (LinkedIn, Instagram)
- Google Reviews QR-Code
- Newsletter-Anmeldung Hinweis
- "Powered by renewable energy" Claim

Template mit {{variablen}} für JSON-Befüllung vorbereiten.
```

### 2.2 Master Template mit Mock-Daten JSON

```json
{
  "firma": {
    "name": "Mission Solar GmbH",
    "claim": "Ihre Energiezukunft beginnt heute",
    "strasse": "Solarstraße 24",
    "plz": "6020",
    "ort": "Innsbruck",
    "land": "Österreich",
    "telefon": "+43 512 987654",
    "email": "info@mission-solar.at",
    "web": "www.mission-solar.at",
    "uid": "ATU98765432",
    "firmenbuch": "FN 987654x",
    "gericht": "Landesgericht Innsbruck",
    "geschaeftsfuehrer": "Bernhard Prokes",
    "bank": "Raiffeisenbank Tirol",
    "iban": "AT65 3600 0000 0123 4567",
    "bic": "RZTIAT22",
    "konzession": "PV-TEC-2024-0815",
    "klimaaktiv_nr": "KA-2024-TIR-042"
  },
  "kunde": {
    "anrede": "Sehr geehrte Familie",
    "titel": "",
    "vorname": "",
    "nachname": "Schneider",
    "firma": "",
    "strasse": "Bergweg 15",
    "plz": "6072",
    "ort": "Lans",
    "uid": "",
    "anlagenstandort": "Bergweg 15, 6072 Lans"
  },
  "rechnung": {
    "nummer": "RE-2025-00247",
    "datum": "28.08.2025",
    "leistungszeitraum": "15.08.2025 - 27.08.2025",
    "zahlungsziel": "27.09.2025",
    "betreff": "PV-Anlage 12 kWp mit KJUUBE Speichersystem"
  },
  "anlage": {
    "leistung_kwp": 12.5,
    "module_anzahl": 28,
    "module_typ": "Jinko Tiger Neo 450Wp",
    "wechselrichter": "Fronius Symo Gen24 10.0 Plus",
    "speicher": "KJUUBE Home 15 kWh",
    "monitoring": "NTUITY Energy Manager Pro",
    "jahresertrag_kwh": 13750,
    "co2_einsparung_tonnen": 5.5,
    "amortisation_jahre": 7.8,
    "netzanschluss_ref": "TINETZ-2025-4789"
  },
  "positionen": [
    {
      "kategorie": "module",
      "beschreibung": "PV-Module Jinko Tiger Neo 450Wp, inkl. Montagesystem",
      "menge": 28,
      "einheit": "Stk",
      "einzelpreis": 285.00,
      "steuersatz": 0,
      "gesamt": 7980.00
    },
    {
      "kategorie": "wechselrichter",
      "beschreibung": "Fronius Symo Gen24 10.0 Plus Hybrid-Wechselrichter",
      "menge": 1,
      "einheit": "Stk",
      "einzelpreis": 2850.00,
      "steuersatz": 0,
      "gesamt": 2850.00
    },
    {
      "kategorie": "speicher",
      "beschreibung": "KJUUBE Home 15 kWh Batteriespeicher",
      "menge": 1,
      "einheit": "Set",
      "einzelpreis": 8900.00,
      "steuersatz": 0,
      "gesamt": 8900.00
    },
    {
      "kategorie": "monitoring",
      "beschreibung": "NTUITY Energy Manager Pro inkl. 5 Jahre Service",
      "menge": 1,
      "einheit": "Stk",
      "einzelpreis": 1290.00,
      "steuersatz": 0,
      "gesamt": 1290.00
    },
    {
      "kategorie": "installation",
      "beschreibung": "Montage, Installation und Inbetriebnahme",
      "menge": 32,
      "einheit": "Std",
      "einzelpreis": 85.00,
      "steuersatz": 0,
      "gesamt": 2720.00
    },
    {
      "kategorie": "elektrik",
      "beschreibung": "AC/DC Verkabelung, Sicherungen, Überspannungsschutz",
      "menge": 1,
      "einheit": "pausch",
      "einzelpreis": 1480.00,
      "steuersatz": 0,
      "gesamt": 1480.00
    },
    {
      "kategorie": "netzanschluss",
      "beschreibung": "Netzanschluss-Koordination und Anmeldung OeMAG",
      "menge": 1,
      "einheit": "pausch",
      "einzelpreis": 380.00,
      "steuersatz": 0,
      "gesamt": 380.00
    }
  ],
  "zusammenfassung": {
    "summe_netto": 25600.00,
    "ust_0_hinweis": "Umsatzsteuerfrei gem. § 6 Abs. 1 Z 9 lit. c UStG (PV-Anlagen bis 35 kWp)",
    "summe_brutto": 25600.ようだ,
    "anzahlung_erhalten": 5000.00,
    "restzahlung": 20600.00
  },
  "foerderung": {
    "bundesfoerderung": "EAG-Investitionszuschuss beantragt: ca. 2.850 €",
    "landesfoerderung": "Land Tirol Solarbonus: ca. 1.500 €",
    "gemeindefoerderung": "Gemeinde Lans PV-Förderung: 500 €",
    "gesamt_foerderung": 4850.00,
    "investition_nach_foerderung": 20750.00
  },
  "zusatzinfo": {
    "garantie": "25 Jahre Leistungsgarantie auf Module, 10 Jahre auf Wechselrichter, 10 Jahre auf KJUUBE Speicher",
    "wartung": "Jährliche Wartung empfohlen - Servicevertrag auf Anfrage",
    "versicherung": "PV-Versicherungsschutz über Tiroler Versicherung vermittelbar",
    "qr_payment": "GENERATE_EPC_QR_CODE_HERE",
    "umwelt": "Ihre Anlage spart jährlich 5,5 Tonnen CO2 - das entspricht 275 Bäumen!"
  }
}
```

### 2.3 Fill-Up Prompt für neue Rechnungen

```
Generiere aus dem Solar-Master-Template eine vollständige Rechnung mit folgenden Anweisungen:

1. DATENVERARBEITUNG:
   - Befülle alle {{placeholder}} mit JSON-Werten
   - Berechne Energiekosten-Ersparnis (0,38€/kWh × Jahresertrag)
   - Erstelle Wirtschaftlichkeitsgrafik mit Amortisationskurve
   - Generiere QR-Code mit korrekten Zahlungsdaten

2. FÖRDER-LOGIK:
   - Wenn Anlagenleistung ≤35 kWp: USt-Befreiung anwenden
   - Wenn >35 kWp: 20% USt berechnen
   - Prüfe aktuelle Fördersätze (EAG, Land, Gemeinde)
   - Berechne Nettokosten nach Förderung

3. DYNAMISCHE TEXTBAUSTEINE:
   - Bei KJUUBE: "Modularer Speicher - jederzeit erweiterbar"
   - Bei NTUITY: "KI-optimiertes Energiemanagement"
   - Sommer (Apr-Sep): "Nutzen Sie die starken Sonnenmonate optimal"
   - Winter (Okt-Mär): "Auch im Winter produziert Ihre Anlage wertvollen Strom"

4. DATEINAME-GENERIERUNG:
   Format: solar_rechnung_[nummer]_[kunde]_[kwp]kwp_[datum].html
   Beispiel: solar_rechnung_RE-2025-00247_schneider_12kwp_20250828.html

5. QUALITÄTSCHECKS:
   - Seriennummern für Garantie vorhanden?
   - Netzanschluss-Referenz eingefügt?
   - CO2-Berechnung plausibel? (0,4kg CO2/kWh × Jahresertrag)
   - Förderhinweise aktuell? (Check gegen 2025 Sätze)

6. BONUS-ELEMENTE:
   - Google Review Link personalisiert
   - Empfehlungsprogramm-Hinweis (500€ pro Neukunde)
   - Sonnige Grüße-Signatur ("Sonnige Grüße aus Tirol")
```

---

## Template 3: IT-Dienstleister Professional

### 3.1 Initial Master Template Prompt

```
Erstelle eine professionelle HTML-Rechnungsvorlage für österreichische IT-Dienstleister:

DESIGN "Tech Professional":
- Dark Mode kompatibel: Umschaltbar zwischen Hell/Dunkel
- Farbschema: Anthrazit (#2C3E50), Akzent Cyan (#00BCD4)
- Monospace Font für Code/Technische Details
- Responsive Design mit Print-Optimization
- GitHub-style Markdown Tables für Positionen

SPEZIELLE IT-ELEMENTE:
- Zeiterfassung mit Ticket-Referenzen
- Remote/Onsite Kennzeichnung
- SLA-Level Anzeige (Bronze/Silver/Gold)
- Technologie-Tags (React, Node, AWS, etc.)
- Git-Commit Referenzen bei Entwicklung

COMPLIANCE & SECURITY:
- DSGVO-Hinweis bei Datenverarbeitung
- ISO 27001 Zertifikatsnummer wenn vorhanden
- Verschlüsselungs-Hinweis für sensible Projekte
- NDA-Referenz bei vertraulichen Arbeiten

B2B-SPEZIFIKA:
- Reverse Charge Hinweis bei EU-Geschäften
- Projektphasen-Aufschlüsselung
- Change Request Dokumentation
- Testing/QA Stunden separat

MODERNE ZAHLUNGSOPTIONEN:
- Crypto-Payment akzeptiert (BTC/ETH Adressen)
- SEPA-Lastschrift für Wartungsverträge
- Kreditkarten via Stripe QR-Code

Verwende semantische HTML5 und {{variablen}} für Dateninjection.
```

### 3.2 Master Template mit Mock-Daten JSON

```json
{
  "firma": {
    "name": "CodeCraft Solutions GmbH",
    "tagline": "Enterprise Software Excellence",
    "strasse": "Techpark 42",
    "plz": "1030",
    "ort": "Wien",
    "land": "Österreich",
    "telefon": "+43 1 234 5678",
    "email": "invoice@codecraft.at",
    "web": "www.codecraft.at",
    "uid": "ATU74185296",
    "firmenbuch": "FN 123456b",
    "gericht": "Handelsgericht Wien",
    "geschaeftsfuehrer": "DI Thomas Entwickler",
    "bank": "Erste Bank",
    "iban": "AT61 1904 3002 3457 3201",
    "bic": "GIBAATWWXXX",
    "iso27001": "ISO/IEC 27001:2013 Cert# AT-2024-1847",
    "crypto_btc": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wh",
    "crypto_eth": "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
  },
  "kunde": {
    "firma": "Innovation Hub GmbH",
    "ansprechpartner": "Mag. Sandra Müller",
    "abteilung": "Digital Transformation",
    "strasse": "Zukunftsweg 100",
    "plz": "6020",
    "ort": "Innsbruck",
    "land": "Österreich",
    "uid": "ATU55588844",
    "projekt_ref": "PRJ-2025-0142",
    "kostenstelle": "IT-4200"
  },
  "rechnung": {
    "nummer": "IT-2025-00389",
    "datum": "28.08.2025",
    "leistungszeitraum": "01.08.2025 - 31.08.2025",
    "zahlungsziel": "27.09.2025",
    "betreff": "Entwicklung Customer Portal - Phase 2",
    "sla_level": "Gold",
    "contract_ref": "MSA-2024-1122"
  },
  "positionen": [
    {
      "phase": "Backend Development",
      "tickets": ["JIRA-4521", "JIRA-4522", "JIRA-4545"],
      "beschreibung": "API Development - REST Endpoints für User Management",
      "entwickler": "Senior Developer",
      "stunden": 48,
      "stundensatz": 120.00,
      "remote_onsite": "remote",
      "technologien": ["Node.js", "PostgreSQL", "Docker"],
      "gesamt": 5760.00
    },
    {
      "phase": "Frontend Development",
      "tickets": ["JIRA-4530", "JIRA-4531"],
      "beschreibung": "React Components für Dashboard und Reporting",
      "entwickler": "Senior Developer",
      "stunden": 36,
      "stundensatz": 120.00,
      "remote_onsite": "remote",
      "technologien": ["React", "TypeScript", "TailwindCSS"],
      "gesamt": 4320.00
    },
    {
      "phase": "DevOps",
      "tickets": ["JIRA-4550"],
      "beschreibung": "CI/CD Pipeline Setup mit GitHub Actions",
      "entwickler": "DevOps Engineer",
      "stunden": 16,
      "stundensatz": 130.00,
      "remote_onsite": "remote",
      "technologien": ["GitHub Actions", "Kubernetes", "AWS"],
      "gesamt": 2080.00
    },
    {
      "phase": "Consulting",
      "tickets": ["JIRA-4500"],
      "beschreibung": "Architecture Review und Security Audit",
      "entwickler": "Solution Architect",
      "stunden": 8,
      "stundensatz": 150.00,
      "remote_onsite": "onsite",
      "technologien": ["Security", "Architecture"],
      "gesamt": 1200.00
    },
    {
      "phase": "Project Management",
      "tickets": ["PM-AUG-01"],
      "beschreibung": "Sprint Planning, Daily Standups, Retrospective",
      "entwickler": "Project Manager",
      "stunden": 12,
      "stundensatz": 95.00,
      "remote_onsite": "hybrid",
      "technologien": ["Scrum", "JIRA"],
      "gesamt": 1140.00
    },
    {
      "phase": "Testing/QA",
      "tickets": ["QA-2025-08"],
      "beschreibung": "Automated Testing, E2E Tests, Performance Testing",
      "entwickler": "QA Engineer",
      "stunden": 24,
      "stundensatz": 85.00,
      "remote_onsite": "remote",
      "technologien": ["Jest", "Cypress", "JMeter"],
      "gesamt": 2040.00
    }
  ],
  "zusammenfassung": {
    "stunden_gesamt": 144,
    "stunden_remote": 124,
    "stunden_onsite": 8,
    "stunden_hybrid": 12,
    "summe_netto": 16540.00,
    "reverse_charge": false,
    "ust_satz": 20,
    "ust_betrag": 3308.00,
    "summe_brutto": 19848.00
  },
  "change_requests": [
    {
      "cr_nummer": "CR-2025-018",
      "beschreibung": "Additional OAuth2 Provider Integration",
      "genehmigt_von": "S. Müller",
      "datum": "15.08.2025",
      "zusatz_stunden": 8,
      "status": "completed"
    }
  ],
  "zusatzinfo": {
    "sla_response": "Gold SLA: 2h Response Time, 99.9% Uptime",
    "git_repos": ["github.com/customer/portal-backend", "github.com/customer/portal-frontend"],
    "deployment": "Production deployment scheduled for 05.09.2025",
    "nda": "Covered under NDA-2024-0055",
    "dsgvo": "All data processing according to GDPR/DSGVO requirements",
    "next_sprint": "Sprint 15 starts 01.09.2025"
  }
}
```

### 3.3 Fill-Up Prompt für neue Rechnungen

```
Erstelle aus dem IT-Professional-Template eine detaillierte Rechnung:

1. TECHNISCHE AUFBEREITUNG:
   - Parse Ticket-Referenzen und erstelle Hyperlinks zu JIRA
   - Gruppiere Stunden nach Technologie-Stack
   - Berechne Remote vs. Onsite Ratio
   - Generiere Burndown-Chart für Projektstunden

2. B2B-SPEZIALBEHANDLUNG:
   - Bei EU-Kunde mit UID: Reverse Charge anwenden
   - Text: "Steuerschuldnerschaft des Leistungsempfängers"
   - Keine USt ausweisen, nur Nettobetrag
   - Bei AT-Kunde: normale 20% USt

3. CHANGE REQUEST LOGIK:
   - CRs als separate Sektion nach Hauptpositionen
   - Verweis auf schriftliche Genehmigung
   - Zusatzstunden klar kennzeichnen
   - Impact auf Timeline dokumentieren

4. SLA-ABHÄNGIGE TEXTE:
   - Gold: "Priority Support with 2h response time"
   - Silver: "Business hours support, 4h response"  
   - Bronze: "Next business day response"

5. DATEINAME-PATTERN:
   Format: it_invoice_[nummer]_[kunde]_[projekt]_[periode].html
   Beispiel: it_invoice_IT-2025-00389_innovationhub_PRJ-2025-0142_202508.html

6. AUTOMATISCHE ERGÄNZUNGEN:
   - Git-Commit-Summary der Periode (letzte 10 commits)
   - Test-Coverage Percentage wenn verfügbar
   - Deployment-Status (Dev/Staging/Production)
   - Knowledge Transfer Dokumentation Verweis

7. ZAHLUNGS-INTELLIGENZ:
   - Bei Beträgen >10k€: Ratenzahlung Option
   - Crypto-Payment: Aktuellen EUR-Kurs anzeigen
   - SEPA-Lastschrift: Mandat-Referenz einfügen
```

---

## Template 4: Kleinunternehmer Minimal

### 4.1 Initial Master Template Prompt

```
Erstelle eine minimalistische HTML-Rechnungsvorlage für österreichische Kleinunternehmer (§ 6 Abs. 1 Z 27 UStG):

DESIGN "Clean & Simple":
- Maximaler Weißraum, minimale Ablenkung
- Eine Akzentfarbe nach Wahl (z.B. #6C63FF)
- System Fonts für schnelles Laden
- Mobile-first Approach
- Druckoptimiert auf einer A4-Seite

KLEINUNTERNEHMER-SPEZIFIKA:
- Prominenter Hinweis: "Umsatzsteuerfrei aufgrund der Kleinunternehmerregelung"
- KEINE UID-Nummer (optional wenn vorhanden)
- KEINE Steueraufschlüsselung
- Bruttosumme = Nettosumme
- Neue Grenze 2025: 55.000€ Hinweis

REDUZIERTE PFLICHTANGABEN:
- Name und Anschrift Leistender
- Name und Anschrift Empfänger
- Leistungsbeschreibung
- Entgelt
- Ausstellungsdatum
- Fortlaufende Nummer

FOKUS-ELEMENTE:
- Große, klare Rechnungsnummer
- Hervorgehobener Gesamtbetrag
- Einfache Positionsliste ohne Komplexität
- Klare Zahlungsinformationen

PERSONAL TOUCH:
- Handschriftliche Schrift für Unterschrift
- Persönliche Dankes-Nachricht
- Social Media nur wenn relevant
- Optional: Foto/Avatar für Vertrauen

Halte es SUPER einfach mit {{variablen}}.
```

### 4.2 Master Template mit Mock-Daten JSON

```json
{
  "firma": {
    "name": "Anna Kreativ",
    "bezeichnung": "Grafikdesign & Illustration",
    "strasse": "Künstlergasse 7",
    "plz": "5020",
    "ort": "Salzburg",
    "land": "Österreich",
    "telefon": "+43 664 1234567",
    "email": "hallo@anna-kreativ.at",
    "web": "www.anna-kreativ.at",
    "bank": "Salzburger Sparkasse",
    "iban": "AT98 2040 4000 1234 5678",
    "bic": "SBGSAT2SXXX",
    "kleinunternehmer": true,
    "instagram": "@annakreativ.design"
  },
  "kunde": {
    "firma": "Café Zeitlos",
    "ansprechpartner": "Hr. Michael Bauer",
    "strasse": "Getreidegasse 15",
    "plz": "5020",
    "ort": "Salzburg"
  },
  "rechnung": {
    "nummer": "2025-018",
    "datum": "28.08.2025",
    "zahlungsziel": "11.09.2025",
    "betreff": "Logo-Design und Geschäftsausstattung"
  },
  "positionen": [
    {
      "beschreibung": "Logo-Design inkl. 3 Entwürfe und 2 Überarbeitungsrunden",
      "betrag": 850.00
    },
    {
      "beschreibung": "Visitenkarten-Design (Vorder- und Rückseite)",
      "betrag": 250.00
    },
    {
      "beschreibung": "Briefpapier und Kuvert-Design",
      "betrag": 200.00
    },
    {
      "beschreibung": "Social Media Template-Set (5 Vorlagen)",
      "betrag": 300.00
    },
    {
      "beschreibung": "Farbpalette und Schriftarten-Guide (PDF)",
      "betrag": 150.00
    }
  ],
  "zusammenfassung": {
    "gesamt": 1750.00,
    "kleinunternehmer_hinweis": "Gemäß § 6 Abs. 1 Z 27 UStG enthält der Rechnungsbetrag keine Umsatzsteuer.",
    "zahlungsziel_text": "14 Tage netto"
  },
  "persoenlich": {
    "dankesnachricht": "Vielen Dank für das Vertrauen in meine Arbeit! Es war mir eine Freude, die visuelle Identität für das Café Zeitlos zu gestalten.",
    "unterschrift": "Anna",
    "ps": "P.S. Gerne unterstütze ich Sie auch bei der Druckabwicklung - sprechen Sie mich einfach an!"
  }
}
```

### 4.3 Fill-Up Prompt für neue Rechnungen

```
Fülle das Kleinunternehmer-Template mit maximaler Einfachheit:

1. MINIMALE KOMPLEXITÄT:
   - Nur notwendige Felder befüllen
   - Keine überflüssigen Berechnungen
   - Klare, kurze Beschreibungen
   - Ein Betrag pro Position (kein Mengen × Preis)

2. KLEINUNTERNEHMER-CHECK:
   - IMMER Hinweis auf Umsatzsteuerbefreiung
   - NIE Steuerbeträge ausweisen
   - NIE "zzgl. MwSt" oder "inkl. MwSt" schreiben
   - Betrag ist immer Endpreis

3. PERSÖNLICHE NOTE:
   - Individuelle Dankesnachricht je nach Projekt
   - Kreative Berufe: Lockerer, persönlicher Ton
   - Saisonale Grüße einbauen wenn passend
   - Emoji sparsam aber gezielt (max. 2-3)

4. DATEINAME KISS-PRINZIP:
   Format: rechnung_[jahr]_[nummer].html
   Beispiel: rechnung_2025_018.html

5. RESPONSIVE CHECKS:
   - Auf Smartphone gut lesbar?
   - Druckt auf genau 1 Seite?
   - Zahlungsinformationen prominent?

6. KLEINUNTERNEHMER-SCHWELLE:
   - Info-Box wenn Jahresumsatz sich 55.000€ nähert
   - Hinweis auf mögliche Regelüberschreitung
   - Empfehlung für Steuerberater-Konsultation
```

---

## Template 5: B2B Reverse Charge EU

### 5.1 Initial Master Template Prompt

```
Entwickle eine HTML-Rechnungsvorlage für grenzüberschreitende B2B-Dienstleistungen mit Reverse Charge:

DESIGN "European Business":
- EU-Sternenbanner subtil im Header
- Mehrsprachige Labels (DE/EN)
- Internationale Formatierung
- Currency Converter Widget
- Flaggen-Icons für Länder

REVERSE CHARGE SPEZIFIKA:
- Prominenter Hinweis in DE und EN:
  "Steuerschuldnerschaft des Leistungsempfängers"
  "Reverse charge - VAT to be paid by recipient"
- KEINE Umsatzsteuer-Ausweisung
- Pflicht: Beide UID-Nummern
- Leistungsort-Bestimmung
- Verweis auf EU-Richtlinie

COMPLIANCE ELEMENTE:
- EU-OSS Registrierungsnummer falls relevant
- VIES-Validierung Status
- Dokumentation der UID-Prüfung
- Leistungsdatum exakt
- B2B-Nachweis Dokumentation

INTERNATIONALE FEATURES:
- Währungsumrechnung EUR/CHF/GBP
- IBAN/SWIFT für alle EU-Länder
- Zeitzonenangabe für Services
- Sprache umschaltbar DE/EN/IT

BESONDERE HINWEISE:
- Bauleistungen-Reverse-Charge Inland
- Schrott/Altmetall Sonderregelung
- Grundstücksleistungen
- Telekommunikation B2C Ausnahmen

Templates mit {{variablen}} und Sprachweichen.
```

### 5.2 Master Template mit Mock-Daten JSON

```json
{
  "firma": {
    "name": "Alpine Consulting GmbH",
    "strasse": "Europastraße 1",
    "plz": "6020",
    "ort": "Innsbruck",
    "land": "Österreich / Austria",
    "telefon": "+43 512 123456",
    "email": "office@alpine-consulting.eu",
    "web": "www.alpine-consulting.eu",
    "uid": "ATU12345678",
    "eori": "ATEOS1234567890",
    "firmenbuch": "FN 123456a",
    "gericht": "Landesgericht Innsbruck",
    "bank_name": "UniCredit Bank Austria",
    "iban": "AT12 1200 0123 4567 8901",
    "bic": "BKAUATWW",
    "bank_name_int": "HSBC Continental Europe",
    "iban_int": "FR76 3000 6000 0112 3456 7890 189",
    "bic_int": "HSBCFRPP"
  },
  "kunde": {
    "firma": "TechVentures B.V.",
    "strasse": "Keizersgracht 555",
    "plz": "1017 DR",
    "ort": "Amsterdam",
    "land": "Niederlande / Netherlands",
    "uid": "NL123456789B01",
    "vies_check": "Valid as of 28.08.2025",
    "ansprechpartner": "Ms. Eva van den Berg",
    "email": "eva@techventures.nl"
  },
  "rechnung": {
    "nummer": "EU-2025-00089",
    "datum": "28.08.2025",
    "leistungsdatum": "01.08.2025 - 31.08.2025",
    "leistungsort": "Amsterdam, Netherlands (§3a UStG)",
    "zahlungsziel": "27.09.2025",
    "betreff": "Strategic Consulting Services - August 2025",
    "sprache": "DE/EN"
  },
  "positionen": [
    {
      "beschreibung_de": "Strategieberatung Markteintritt DACH-Region",
      "beschreibung_en": "Strategic consulting market entry DACH region",
      "einheit": "Tage/Days",
      "menge": 8,
      "tagessatz": 1500.00,
      "gesamt": 12000.00
    },
    {
      "beschreibung_de": "Wettbewerbsanalyse und Marktforschung",
      "beschreibung_en": "Competitive analysis and market research",
      "einheit": "Tage/Days",
      "menge": 5,
      "tagessatz": 1500.00,
      "gesamt": 7500.00
    },
    {
      "beschreibung_de": "Workshop Facilitation (vor Ort in Amsterdam)",
      "beschreibung_en": "Workshop Facilitation (on-site Amsterdam)",
      "einheit": "Tage/Days",
      "menge": 2,
      "tagessatz": 1800.00,
      "gesamt": 3600.00
    },
    {
      "beschreibung_de": "Reisekosten (Flug INN-AMS, 2 Übernachtungen)",
      "beschreibung_en": "Travel expenses (Flight INN-AMS, 2 nights)",
      "einheit": "pausch",
      "menge": 1,
      "tagessatz": 850.00,
      "gesamt": 850.00
    }
  ],
  "zusammenfassung": {
    "summe_netto": 23950.00,
    "reverse_charge_text_de": "Steuerschuldnerschaft des Leistungsempfängers gem. Art. 196 MwStSystRL",
    "reverse_charge_text_en": "Reverse charge - VAT to be paid by recipient according to Art. 196 VAT Directive",
    "keine_ust": true,
    "summe_zu_zahlen": 23950.00,
    "waehrung": "EUR"
  },
  "compliance": {
    "vies_validierung": "UID-validation performed via VIES on 28.08.2025 - Status: Valid",
    "leistungsort_erklaerung_de": "Der Ort der sonstigen Leistung bestimmt sich nach § 3a UStG nach dem Empfängerortprinzip.",
    "leistungsort_erklaerung_en": "Place of supply determined according to § 3a UStG based on recipient location principle.",
    "b2b_nachweis": "Business customer status verified through valid VAT ID and commercial register extract.",
    "dokumentation": "All compliance documents archived under reference EU-2025-00089-DOCS"
  },
  "zusatz": {
    "naechste_schritte_de": "Abschlussbericht wird bis 15.09.2025 übermittelt.",
    "naechste_schritte_en": "Final report will be delivered by September 15, 2025.",
    "agb": "Es gelten unsere AGB unter www.alpine-consulting.eu/agb",
    "gerichtsstand": "Gerichtsstand ist Innsbruck, Österreich / Place of jurisdiction is Innsbruck, Austria"
  }
}
```

### 5.3 Fill-Up Prompt für neue Rechnungen

```
Generiere eine konforme Reverse-Charge-Rechnung mit folgenden Prüfungen:

1. REVERSE CHARGE VALIDIERUNG:
   - Check: B2B-Status (beide UIDs vorhanden?)
   - Check: Grenzüberschreitend (verschiedene Länder?)
   - Check: Dienstleistung (nicht Warenlieferung?)
   - Wenn alle JA: Reverse Charge anwenden
   - Wenn NEIN: Warnung ausgeben

2. SPRACHLICHE AUFBEREITUNG:
   - Hauptsprache = Kundenland-Sprache
   - Backup immer Englisch
   - Rechtliche Hinweise IMMER auch Deutsch
   - Beträge in Worten in beiden Sprachen

3. COMPLIANCE-DOKUMENTATION:
   - VIES-Check Timestamp einfügen
   - Screenshot-Referenz zur UID-Validierung
   - Leistungsort-Paragraph zitieren
   - EU-Richtlinie Artikel nennen

4. SPEZIALFÄLLE BEHANDLUNG:
   - Bauleistung Inland AT: Auch Reverse Charge!
   - Grundstücksleistungen: Immer Leistungsort-Land
   - Telekom an Privatpersonen: KEIN Reverse Charge
   - Elektronische Dienstleistungen: OSS prüfen

5. DATEINAME INTERNATIONAL:
   Format: invoice_EU_[nummer]_[kunde_land]_[datum].html
   Beispiel: invoice_EU_EU-2025-00089_NL_20250828.html

6. WÄHRUNGS-INTELLIGENZ:
   - Hauptwährung immer EUR
   - Bei UK-Kunden: GBP Referenz anzeigen
   - Bei CH-Kunden: CHF Referenz anzeigen
   - Tageskurs von EZB API oder fix 

7. ZAHLUNGSWEG-OPTIMIERUNG:
   - SEPA für EU-Länder
   - SWIFT für Non-EU
   - Gebührenteilung OUR/SHA/BEN klären
   - Payment Terms nach Land anpassen
```

---

## Template 6: Beratung Premium

### 6.1 Initial Master Template Prompt

```
Erstelle eine Premium HTML-Rechnungsvorlage für österreichische Unternehmensberater:

DESIGN "Executive Premium":
- Edles Design mit Goldakzenten (#D4AF37)
- Große Typografie, viel Whitespace
- Wasserzeichen-Logo dezent
- Schwere Serifenschrift für Headers
- Feines Papier-Textur-Background

BERATUNGS-SPEZIFIKA:
- Tagessätze und Stundensätze prominent
- Erfolgshonorar-Komponenten separat
- Reisezeiten mit reduziertem Satz
- Spesen detailliert aufgeschlüsselt
- Projektphasen-Darstellung

VERTRAUENSELEMENTE:
- Zertifizierungen (CMC, ISO, etc.)
- Berufshaftpflicht-Versicherungsnummer
- Referenz zu Rahmenvertrag
- Vertraulichkeitshinweis
- WKO Fachgruppe Mitgliedschaft

PREMIUM FEATURES:
- Executive Summary der Leistungen
- Value-Add Berechnung
- ROI-Indikation
- Benchmarking-Referenzen
- Next Steps Empfehlungen

RECHTLICHE BESONDERHEITEN:
- Erfolgshonorar-Klauseln korrekt
- Haftungsbeschränkungen
- Geistiges Eigentum Regelung
- Verwertungsrechte
- Konkurrenzklausel wenn relevant

Erstelle mit semantischem HTML und {{var}} Platzhaltern.
```

### 6.2 Master Template mit Mock-Daten JSON

```json
{
  "firma": {
    "name": "Strategic Excellence Partners GmbH",
    "claim": "Transforming Vision into Value",
    "strasse": "Ringstraße 1",
    "plz": "1010",
    "ort": "Wien",
    "land": "Österreich",
    "telefon": "+43 1 890 1234",
    "email": "office@strategic-excellence.at",
    "web": "www.strategic-excellence.at",
    "uid": "ATU69258147",
    "firmenbuch": "FN 123789x",
    "gericht": "Handelsgericht Wien",
    "geschaeftsfuehrer": "Mag. Dr. Andreas Berater, CMC",
    "bank": "Bank Austria",
    "iban": "AT45 1200 0100 1234 5678",
    "bic": "BKAUATWW",
    "cmc_nummer": "CMC-AT-2020-4567",
    "iso": "ISO 20700:2017 certified",
    "versicherung": "Berufshaftpflicht: Zürich Versicherung, Pol.Nr. BH-2024-789456",
    "wko": "Fachgruppe UBIT - Unternehmensberatung, Buchhaltung und IT"
  },
  "kunde": {
    "firma": "Global Industries AG",
    "vorstand": "Mag. Christina Vorstand",
    "abteilung": "Executive Board",
    "strasse": "Industriezeile 500",
    "plz": "4020",
    "ort": "Linz",
    "land": "Österreich",
    "uid": "ATU58741236",
    "rahmenvertrag": "RV-2024-0089 vom 15.01.2024"
  },
  "rechnung": {
    "nummer": "SEP-2025-00234",
    "datum": "28.08.2025",
    "leistungszeitraum": "01.07.2025 - 31.08.2025",
    "zahlungsziel": "27.09.2025",
    "betreff": "Strategieprojekt 'Future Excellence 2030' - Phase 2",
    "projektleiter": "Dr. Michael Senior Partner"
  },
  "executive_summary": {
    "projektziel": "Entwicklung und Implementierung einer digitalen Transformationsstrategie zur Steigerung der operativen Effizienz um 30% bis 2027",
    "hauptergebnisse": [
      "Digitalisierungs-Roadmap mit 47 priorisierten Initiativen",
      "Organisationsdesign für agile Arbeitsweise",
      "Change Management Konzept für 1.200 Mitarbeiter",
      "Quick-Win Identifikation mit 2.3M€ Einsparpotential"
    ],
    "value_delivered": "Prognostizierter ROI: 450% über 3 Jahre",
    "next_steps": "Implementierungsbegleitung Phase 3 ab Oktober 2025"
  },
  "positionen": [
    {
      "phase": "Analyse & Diagnose",
      "beschreibung": "Ist-Analyse, Prozessaufnahme, Benchmarking",
      "berater": "Senior Partner",
      "tage": 8,
      "tagessatz": 2400.00,
      "gesamt": 19200.00
    },
    {
      "phase": "Strategieentwicklung",
      "beschreibung": "Strategieworkshops, Szenarioplanung, Roadmap-Entwicklung",
      "berater": "Senior Partner",
      "tage": 12,
      "tagessatz": 2400.00,
      "gesamt": 28800.00
    },
    {
      "phase": "Konzeption",
      "beschreibung": "Detailkonzepte, Business Cases, Implementierungsplan",
      "berater": "Principal Consultant",
      "tage": 15,
      "tagessatz": 1800.00,
      "gesamt": 27000.00
    },
    {
      "phase": "Change Management",
      "beschreibung": "Stakeholder-Management, Kommunikationskonzept, Training-Design",
      "berater": "Senior Consultant",
      "tage": 10,
      "tagessatz": 1400.00,
      "gesamt": 14000.00
    },
    {
      "phase": "Projektmanagement",
      "beschreibung": "Projektleitung, Steering Committee, Dokumentation",
      "berater": "Senior Consultant",
      "tage": 8,
      "tagessatz": 1400.00,
      "gesamt": 11200.00
    },
    {
      "phase": "Reisezeiten",
      "beschreibung": "Reisezeiten Wien-Linz (50% des Tagessatzes)",
      "berater": "Verschiedene",
      "tage": 6,
      "tagessatz": 900.00,
      "gesamt": 5400.00
    }
  ],
  "spesen": [
    {
      "beschreibung": "Bahnfahrten Wien-Linz Business Class",
      "anzahl": 18,
      "einzelpreis": 78.00,
      "gesamt": 1404.00
    },
    {
      "beschreibung": "Hotelübernachtungen Linz",
      "anzahl": 12,
      "einzelpreis": 145.00,
      "gesamt": 1740.00
    },
    {
      "beschreibung": "Verpflegungspauschale",
      "anzahl": 12,
      "einzelpreis": 26.40,
      "gesamt": 316.80
    },
    {
      "beschreibung": "Workshopmaterialien und Catering",
      "anzahl": 1,
      "einzelpreis": 1250.00,
      "gesamt": 1250.00
    }
  ],
  "erfolgshonorar": {
    "vereinbart": true,
    "beschreibung": "Erfolgshonorar bei Erreichung der Kosteneinsparung >2M€ im ersten Jahr",
    "prozentsatz": 5,
    "maximalbetrag": 50000.00,
    "faelligkeit": "Nach Nachweis Q2/2026",
    "status": "Noch nicht fällig"
  },
  "zusammenfassung": {
    "beratungshonorare": 105600.00,
    "spesen": 4710.80,
    "zwischensumme": 110310.80,
    "rabatt_prozent": 5,
    "rabatt_betrag": 5515.54,
    "summe_netto": 104795.26,
    "ust_20": 20959.05,
    "summe_brutto": 125754.31
  },
  "zusatzinfo": {
    "vertraulichkeit": "Alle Projektergebnisse unterliegen strengster Vertraulichkeit gemäß NDA vom 10.01.2024",
    "ip_rechte": "Sämtliche Verwertungsrechte an den Arbeitsergebnissen gehen nach vollständiger Zahlung an den Auftraggeber über",
    "haftung": "Die Haftung ist auf die Höhe des Beratungshonorars beschränkt, soweit gesetzlich zulässig",
    "referenzen": "Benchmark-Daten basieren auf unserer Studie 'Digital Excellence 2025' mit n=127 Unternehmen"
  }
}
```

### 6.3 Fill-Up Prompt für neue Rechnungen

```
Erstelle eine Premium-Beratungsrechnung mit Executive-Qualität:

1. WERTDARSTELLUNG:
   - Value Delivered prominent hervorheben
   - ROI-Berechnung visualisieren
   - Benchmark-Vergleiche einbauen
   - Einsparungspotentiale beziffern

2. HONORAR-STRUKTURIERUNG:
   - Tagessätze nach Seniorität staffeln
   - Reisezeiten mit 50% berechnen
   - Spesen detailliert und transparent
   - Erfolgshonorar separat ausweisen

3. EXECUTIVE SUMMARY:
   - Maximal 5 Bullet Points
   - Quantifizierte Ergebnisse
   - Klare Next Steps
   - Investment vs. Return Darstellung

4. PREMIUM-FORMATIERUNG:
   - Seitenzahlen bei Mehrseitern
   - Inhaltsverzeichnis ab 3 Seiten
   - Anhang mit Detaildokumentation
   - Unterschriftenblock für beide Parteien

5. DATEINAME PREMIUM:
   Format: invoice_[firma]_[projekt]_[phase]_[datum].html
   Beispiel: invoice_SEP_futureexcellence_phase2_20250828.html

6. COMPLIANCE-CHECKS:
   - CMC-Ethikrichtlinien beachtet?
   - Erfolgshonorar rechtskonform?
   - Haftungsbeschränkung wirksam?
   - Vertraulichkeit gesichert?

7. PSYCHOLOGIE-ELEMENTE:
   - Investition statt Kosten
   - Partnerschaft statt Dienstleistung
   - Transformation statt Beratung
   - Excellence statt Standard
```

---

## Template 7: Tourismus Dreisprachig

### 7.1 Initial Master Template Prompt

```
Entwickle eine dreisprachige HTML-Rechnungsvorlage für Tiroler Tourismusbetriebe (DE/EN/IT):

DESIGN "Alpine Hospitality":
- Tiroler Berge-Silhouette als Header
- Warme Farben: Holzbraun (#8B4513), Alpenweiß, Himmelblau (#87CEEB)
- Authentische Tirol-Bildsprache
- Edelweiß als Design-Element
- Responsive für Tablet-Nutzung an Rezeption

DREISPRACHIGKEIT:
- Deutsch als Hauptsprache
- English for international guests
- Italiano per ospiti del Sud Tirolo
- Automatische Spracherkennung nach Ländercode
- Flaggen-Icons zur Sprachauswahl

TOURISMUS-SPEZIFIKA:
- Zimmerkategorien mit Bildern
- Pensionspreise (HP, VP, All-Inclusive)
- Ortstaxe/Kurtaxe separat
- Stornogebühren-Hinweis
- Saison-Zuschläge transparent

BESONDERE POSITIONEN:
- Wellness & Spa Leistungen
- Skipass-Vermittlung
- Bergbahn-Tickets
- Restaurant-Konsumationen
- Minibar-Abrechnung
- Parkplatz/Garage

ZAHLUNGSARTEN:
- Kreditkarten-Logos
- Sofortüberweisung QR
- PayPal/Klarna Option
- Anzahlung bereits geleistet
- Restzahlung bei Abreise

Footer mit Gütesiegel und Bewertungen.
```

### 7.2 Master Template mit Mock-Daten JSON

```json
{
  "hotel": {
    "name": "Alpenresort Sonnblick ****S",
    "slogan": {
      "de": "Ihre Auszeit in den Tiroler Bergen",
      "en": "Your retreat in the Tyrolean Alps",
      "it": "Il vostro rifugio nelle Alpi tirolesi"
    },
    "strasse": "Panoramaweg 100",
    "plz": "6100",
    "ort": "Seefeld in Tirol",
    "land": "Österreich",
    "telefon": "+43 5212 12345",
    "email": "info@sonnblick.tirol",
    "web": "www.sonnblick.tirol",
    "uid": "ATU67890123",
    "firmenbuch": "FN 456789b",
    "geschaeftsfuehrer": "Familie Hofer",
    "bank": "Raiffeisen Seefeld",
    "iban": "AT12 3456 7890 1234 5678",
    "bic": "RZTIAT22456",
    "guetesiegel": ["4 Sterne Superior", "Tiroler Wirtshaus", "klimaaktiv"],
    "bewertung": "Booking.com 9.2 | TripAdvisor 4.5★ | Google 4.7★"
  },
  "gast": {
    "anrede": {
      "de": "Sehr geehrte Familie",
      "en": "Dear Family",
      "it": "Gentile Famiglia"
    },
    "nachname": "Rossi",
    "strasse": "Via Roma 25",
    "plz": "39100",
    "ort": "Bozen",
    "land": "Italien / Italy / Italia",
    "email": "marco.rossi@email.it",
    "sprache": "it"
  },
  "rechnung": {
    "nummer": "2025-3847",
    "datum": "28.08.2025",
    "anreise": "21.08.2025",
    "abreise": "28.08.2025",
    "naechte": 7,
    "personen": 4,
    "zimmer": "201 + 203"
  },
  "leistungen": [
    {
      "kategorie": "unterkunft",
      "beschreibung": {
        "de": "Doppelzimmer Superior mit Balkon, Halbpension",
        "en": "Superior double room with balcony, half board",
        "it": "Camera doppia superior con balcone, mezza pensione"
      },
      "einheit": {
        "de": "Nächte",
        "en": "Nights",
        "it": "Notti"
      },
      "menge": 7,
      "einzelpreis": 180.00,
      "gesamt": 1260.00,
      "ust_satz": 13
    },
    {
      "kategorie": "unterkunft",
      "beschreibung": {
        "de": "Familienzimmer mit Bergblick, Halbpension (2 Kinder)",
        "en": "Family room mountain view, half board (2 children)",
        "it": "Camera famigliare vista montagna, mezza pensione (2 bambini)"
      },
      "einheit": {
        "de": "Nächte",
        "en": "Nights",
        "it": "Notti"
      },
      "menge": 7,
      "einzelpreis": 240.00,
      "gesamt": 1680.00,
      "ust_satz": 13
    },
    {
      "kategorie": "verpflegung",
      "beschreibung": {
        "de": "Upgrade All-Inclusive (4 Personen × 7 Tage)",
        "en": "All-Inclusive upgrade (4 persons × 7 days)",
        "it": "Upgrade All-Inclusive (4 persone × 7 giorni)"
      },
      "einheit": {
        "de": "Paket",
        "en": "Package",
        "it": "Pacchetto"
      },
      "menge": 1,
      "einzelpreis": 420.00,
      "gesamt": 420.00,
      "ust_satz": 10
    },
    {
      "kategorie": "wellness",
      "beschreibung": {
        "de": "Alpenkräuter-Massage 50 Min. (2×)",
        "en": "Alpine herbs massage 50 min (2×)",
        "it": "Massaggio alle erbe alpine 50 min (2×)"
      },
      "einheit": {
        "de": "Behandlung",
        "en": "Treatment",
        "it": "Trattamento"
      },
      "menge": 2,
      "einzelpreis": 85.00,
      "gesamt": 170.00,
      "ust_satz": 20
    },
    {
      "kategorie": "sonstiges",
      "beschreibung": {
        "de": "Tages-Skipässe Seefeld (2 Erw. + 2 Kinder)",
        "en": "Day ski passes Seefeld (2 adults + 2 children)",
        "it": "Skipass giornalieri Seefeld (2 adulti + 2 bambini)"
      },
      "einheit": {
        "de": "Tag",
        "en": "Day",
        "it": "Giorno"
      },
      "menge": 3,
      "einzelpreis": 186.00,
      "gesamt": 558.00,
      "ust_satz": 13
    },
    {
      "kategorie": "minibar",
      "beschreibung": {
        "de": "Minibar-Verbrauch",
        "en": "Minibar consumption",
        "it": "Consumo minibar"
      },
      "einheit": {
        "de": "Gesamt",
        "en": "Total",
        "it": "Totale"
      },
      "menge": 1,
      "einzelpreis": 67.50,
      "gesamt": 67.50,
      "ust_satz": 20
    },
    {
      "kategorie": "parken",
      "beschreibung": {
        "de": "Garagenplatz",
        "en": "Garage parking",
        "it": "Posto auto in garage"
      },
      "einheit": {
        "de": "Nächte",
        "en": "Nights",
        "it": "Notti"
      },
      "menge": 7,
      "einzelpreis": 15.00,
      "gesamt": 105.00,
      "ust_satz": 20
    }
  ],
  "ortstaxe": {
    "beschreibung": {
      "de": "Ortstaxe Seefeld (2,50€ pro Person/Nacht ab 15 Jahren)",
      "en": "Local tax Seefeld (€2.50 per person/night from 15 years)",
      "it": "Tassa di soggiorno Seefeld (2,50€ per persona/notte dai 15 anni)"
    },
    "personen": 2,
    "naechte": 7,
    "betrag_pro": 2.50,
    "gesamt": 35.00,
    "ust_frei": true
  },
  "zusammenfassung": {
    "unterkunft_netto": 2940.00,
    "verpflegung_netto": 420.00,
    "sonstiges_netto": 900.50,
    "summe_netto": 4260.50,
    "ust_10": 42.00,
    "ust_13": 499.40,
    "ust_20": 68.50,
    "summe_ust": 609.90,
    "summe_brutto": 4870.40,
    "ortstaxe": 35.00,
    "gesamtbetrag": 4905.40,
    "anzahlung_geleistet": 500.00,
    "zu_zahlen": 4405.40
  },
  "zusatztext": {
    "de": "Vielen Dank für Ihren Aufenthalt! Wir freuen uns auf ein Wiedersehen in den Tiroler Bergen.",
    "en": "Thank you for your stay! We look forward to welcoming you back to the Tyrolean Alps.",
    "it": "Grazie per il vostro soggiorno! Non vediamo l'ora di rivedervi nelle Alpi tirolesi."
  },
  "storno": {
    "de": "Stornobedingungen gemäß ÖHVB: bis 3 Monate vor Anreise kostenlos, bis 1 Monat 40%, bis 1 Woche 70%, danach 90%",
    "en": "Cancellation according to ÖHVB: free until 3 months before arrival, until 1 month 40%, until 1 week 70%, thereafter 90%",
    "it": "Condizioni di cancellazione secondo ÖHVB: gratuito fino a 3 mesi prima, fino a 1 mese 40%, fino a 1 settimana 70%, poi 90%"
  }
}
```

### 7.3 Fill-Up Prompt für neue Rechnungen

```
Erstelle eine dreisprachige Tourismusrechnung mit Tiroler Charme:

1. SPRACHERKENNUNG:
   - Primärsprache nach Gastland wählen
   - IT für Südtirol/Italien
   - EN für UK/USA/International
   - DE für DACH-Region
   - Alle Texte dreisprachig anbieten

2. STEUER-KOMPLEXITÄT:
   - Unterkunft: 13% (reduzierter Tourismussteuersatz)
   - Speisen: 10% (Lebensmittel)
   - Getränke/Wellness: 20% (Normalsteuersatz)
   - Ortstaxe: steuerfrei (durchlaufender Posten)

3. TOURISMUS-SPEZIAL:
   - Hochsaison-Zuschläge transparent
   - Kinderermäßigungen deutlich
   - Inklusivleistungen hervorheben
   - Wellness-Pakete attraktiv darstellen

4. BILDSPRACHE:
   - Zimmerkategorie-Fotos wenn vorhanden
   - Hotel-Logo prominent
   - Gütesiegel sichtbar
   - Social Media QR-Codes

5. DATEINAME MEHRSPRACHIG:
   Format: invoice_[hotel]_[gastnummer]_[sprache]_[datum].html
   Beispiel: invoice_sonnblick_2025-3847_it_20250828.html

6. PAYMENT-FLEXIBILITÄT:
   - Restzahlung Bar/EC/Kreditkarte
   - Währungsangabe EUR prominent
   - Keine Wechselkurse (nur EUR)
   - Anzahlungsbestätigung

7. GASTFREUNDSCHAFT:
   - Persönliche Grüße der Familie
   - Wiederkommen-Rabatt erwähnen
   - Bewertungs-Bitte dezent
   - Saisonale Events ankündigen
```

---

## Template 8: Bau & VOB Abschlagsrechnung

### 8.1 Initial Master Template Prompt

```
Erstelle eine VOB-konforme Abschlagsrechnungsvorlage für österreichische Bauunternehmen:

DESIGN "Construction Professional":
- Robustes Layout mit klaren Linien
- Baustellenfotos im Header möglich
- Warn-Orange (#FF6600) als Akzentfarbe
- Technische Schrift (DIN-ähnlich)
- Wetterfestes Design für Baustellennutzung

VOB/ÖNORM B 2110 SPEZIFIKA:
- Leistungsstand in Prozent
- Bezug zum Hauptauftrag
- Nachweisbare Teilleistungen
- Prüfvermerk-Feld
- Sicherheitseinbehalt-Hinweis

BAUSTELLENDETAILS:
- Bauvorhaben-Bezeichnung
- Baustellen-Adresse
- Bauherr und Architekt
- Baubeginn/Fertigstellung
- Auftragssumme gesamt

ABRECHNUNG NACH LEISTUNGSSTAND:
- Auftragsvolumen gesamt
- Bisher abgerechnet (kumuliert)
- Aktuelle Leistung (Periode)
- Verbleibende Leistung
- Nachträge separat

SICHERHEITEN & EINBEHALTE:
- Haftrücklass 10%
- Deckungsrücklass 2%
- Gewährleistung 3 Jahre
- Bankgarantie-Option
- BUAK-Zuschlag

Strukturierte Vorlage mit {{variablen}}.
```

### 8.2 Master Template mit Mock-Daten JSON

```json
{
  "firma": {
    "name": "Bau-Meister Tirol GmbH",
    "zusatz": "Ihr Partner für nachhaltiges Bauen",
    "strasse": "Gewerbestraße 25",
    "plz": "6060",
    "ort": "Hall in Tirol",
    "land": "Österreich",
    "telefon": "+43 5223 45678",
    "email": "office@baumeister-tirol.at",
    "web": "www.baumeister-tirol.at",
    "uid": "ATU65432109",
    "firmenbuch": "FN 234567m",
    "gericht": "Landesgericht Innsbruck",
    "geschaeftsfuehrer": "Ing. Franz Baumeister",
    "bank": "Volksbank Tirol",
    "iban": "AT77 4239 0000 0123 4567",
    "bic": "VBOEATWWINN",
    "konzession": "Baumeister-Konzession GZ 2020/1234"
  },
  "bauherr": {
    "firma": "Wohnbau Tirol GmbH",
    "vertreter": "DI Maria Planer",
    "strasse": "Südtiroler Platz 8",
    "plz": "6020",
    "ort": "Innsbruck",
    "uid": "ATU12378945"
  },
  "architekt": {
    "buero": "Architektur Alpen ZT GmbH",
    "kontakt": "Arch. DI Johann Modern"
  },
  "projekt": {
    "bezeichnung": "Mehrfamilienhaus 'Sonnengarten' - 12 WE",
    "bauadresse": "Sonnenstraße 45, 6020 Innsbruck",
    "auftragsnummer": "2024-BWH-089",
    "auftragsdatum": "15.03.2024",
    "auftragssumme": 1850000.00,
    "baubeginn": "01.05.2024",
    "fertigstellung_plan": "30.11.2025"
  },
  "abschlagsrechnung": {
    "nummer": "AR-2025-00456",
    "teilrechnung_nr": 8,
    "datum": "28.08.2025",
    "leistungszeitraum": "01.08.2025 - 31.08.2025",
    "leistungsstand_prozent": 42.5,
    "zahlungsziel_tage": 21,
    "zahlungsziel_datum": "18.09.2025",
    "prueffrist": "gem. § 16 Abs 1 Z 1 VOB: 21 Tage"
  },
  "leistungen_aktuell": [
    {
      "position": "02.01",
      "beschreibung": "Erdarbeiten - Baugrube",
      "menge_gesamt": 2400,
      "einheit": "m³",
      "menge_periode": 0,
      "prozent_fertig": 100,
      "einzelpreis": 45.00,
      "gesamtpreis": 108000.00,
      "periode_betrag": 0
    },
    {
      "position": "03.01",
      "beschreibung": "Fundamentplatte Stahlbeton C25/30",
      "menge_gesamt": 450,
      "einheit": "m³",
      "menge_periode": 180,
      "prozent_fertig": 100,
      "einzelpreis": 380.00,
      "gesamtpreis": 171000.00,
      "periode_betrag": 68400.00
    },
    {
      "position": "04.02",
      "beschreibung": "Außenwände Stahlbeton C25/30",
      "menge_gesamt": 820,
      "einheit": "m³",
      "menge_periode": 220,
      "prozent_fertig": 65,
      "einzelpreis": 420.00,
      "gesamtpreis": 344400.00,
      "periode_betrag": 92400.00
    },
    {
      "position": "04.03",
      "beschreibung": "Decken Stahlbeton C25/30",
      "menge_gesamt": 380,
      "einheit": "m³",
      "menge_periode": 95,
      "prozent_fertig": 25,
      "einzelpreis": 450.00,
      "gesamtpreis": 171000.00,
      "periode_betrag": 42750.00
    },
    {
      "position": "05.01",
      "beschreibung": "Mauerwerk Außenwände EG-3.OG",
      "menge_gesamt": 1840,
      "einheit": "m²",
      "menge_periode": 460,
      "prozent_fertig": 25,
      "einzelpreis": 125.00,
      "gesamtpreis": 230000.00,
      "periode_betrag": 57500.00
    },
    {
      "position": "05.02",
      "beschreibung": "Mauerwerk Innenwände tragend",
      "menge_gesamt": 920,
      "einheit": "m²",
      "menge_periode": 184,
      "prozent_fertig": 20,
      "einzelpreis": 95.00,
      "gesamtpreis": 87400.00,
      "periode_betrag": 17480.00
    }
  ],
  "abrechnung_kumuliert": {
    "auftragssumme_netto": 1850000.00,
    "nachtraege_genehmigt": [
      {
        "nr": "N01",
        "beschreibung": "Bodenaustausch wegen Altlasten",
        "betrag": 45000.00
      },
      {
        "nr": "N02",
        "beschreibung": "Zusätzliche Tiefgaragenstellplätze",
        "betrag": 68000.00
      }
    ],
    "nachtraege_summe": 113000.00,
    "auftragssumme_gesamt": 1963000.00,
    "bisherige_abschlaege": [
      {"nr": 1, "betrag": 95000.00},
      {"nr": 2, "betrag": 142000.00},
      {"nr": 3, "betrag": 168000.00},
      {"nr": 4, "betrag": 156000.00},
      {"nr": 5, "betrag": 162000.00},
      {"nr": 6, "betrag": 145000.00},
      {"nr": 7, "betrag": 158000.00}
    ],
    "bisherige_summe": 1026000.00,
    "aktuelle_leistung": 278530.00,
    "gesamt_geleistet": 1304530.00,
    "leistungsstand_prozent": 66.46,
    "verbleibende_leistung": 658470.00
  },
  "einbehalte": {
    "haftrücklass_prozent": 10,
    "haftrücklass_betrag": 27853.00,
    "deckungsrücklass_prozent": 2,
    "deckungsrücklass_betrag": 5570.60,
    "buak_zuschlag_prozent": 1.95,
    "buak_zuschlag_betrag": 5431.34,
    "sicherheitseinbehalt_gesamt": 33423.60
  },
  "zusammenfassung": {
    "leistung_periode_netto": 278530.00,
    "abzgl_sicherheitseinbehalt": 33423.60,
    "zwischensumme": 245106.40,
    "ust_20": 49021.28,
    "abschlagssumme_brutto": 294127.68
  },
  "hinweise": {
    "prueffrist": "Die Prüf- und Zahlungsfrist beträgt gemäß § 16 Abs 1 Z 1 VOB 21 Tage ab Rechnungseingang",
    "vorbehalt": "Alle Maße und Mengen unter Vorbehalt der örtlichen Aufnahme",
    "gewaehrleistung": "Gewährleistungsfrist 3 Jahre gemäß ÖNORM B 2110",
    "sicherstellung": "Sicherheitseinbehalt kann durch Bankgarantie abgelöst werden"
  }
}
```

### 8.3 Fill-Up Prompt für neue Rechnungen

```
Generiere eine VOB-konforme Abschlagsrechnung mit Baustellenpräzision:

1. LEISTUNGSSTAND-BERECHNUNG:
   - Kumulierte Vorleistungen addieren
   - Aktuelle Periode exakt abgrenzen
   - Prozentsatz auf Gesamtauftrag beziehen
   - Nachträge separat ausweisen

2. EINBEHALTE KORREKT:
   - Haftrücklass 10% (oder vereinbart)
   - Deckungsrücklass 2% (Standard)
   - BUAK-Zuschlag aktuell prüfen
   - Nur auf Nettobetrag berechnen

3. MENGEN-DOKUMENTATION:
   - Aufmaß-Protokoll referenzieren
   - Menge gesamt vs. Periode klar
   - Einheiten normgerecht (m³, m², lfm)
   - Vorbehalt örtliche Aufnahme

4. RECHTLICHE PRÜFUNG:
   - VOB/ÖNORM B 2110 konform?
   - Prüffrist korrekt angegeben?
   - Zahlungsziel max. 30 Tage?
   - Skontovereinbarung beachten

5. DATEINAME BAU-STANDARD:
   Format: AR_[projektnr]_[teilrechnung]_[datum].html
   Beispiel: AR_2024-BWH-089_TR08_20250828.html

6. NACHTRAGS-MANAGEMENT:
   - Schriftliche Beauftragung vorhanden?
   - Preisbasis dokumentiert?
   - Auswirkung auf Bauzeit?
   - Separate Kennzeichnung

7. AUTOMATISCHE WARNUNGEN:
   - Bei Verzug: Verzugszinsen-Hinweis
   - Bei Mängeln: Einbehalt-Recht
   - Bei Überschreitung: Budget-Alarm
   - Bei Fristablauf: Prüfvermerk-Erinnerung
```

---

## Template 9: Freelancer Creative

### 9.1 Initial Master Template Prompt

```
Entwickle eine kreative HTML-Rechnungsvorlage für österreichische Freelancer (Designer, Fotografen, Texter):

DESIGN "Creative Mind":
- Asymmetrisches Layout mit Personality
- Farbverlauf oder Duotone-Effekt
- Handlettering-Fonts für Headers
- Portfolio-Teaser Integration
- Instagram-Grid Preview

FREELANCER-ESSENTIALS:
- Projekt-Moodboard Thumbnail
- Creative Brief Referenz
- Nutzungsrechte-Klausel
- Revision Rounds dokumentiert
- Kill-Fee Regelung

FLEXIBLE PREISMODELLE:
- Stundensatz für Konzeption
- Pauschalpreis für Umsetzung
- Usage Rights extra
- Rush-Fee Aufschlag
- Friends & Family Rabatt

PORTFOLIO-INTEGRATION:
- Behance/Dribbble Links
- Instagram Featured Posts
- Case Study QR-Code
- Testimonial Quote
- Awards/Features Badges

KREATIV-SPEZIFISCH:
- Farbprofile (CMYK/RGB/HEX)
- Dateiformate-Liste
- Transfer via WeTransfer Link
- Cloud-Storage Access
- Version Control Info

Personality-driven template mit {{vars}}.
```

### 9.2 Master Template mit Mock-Daten JSON

```json
{
  "freelancer": {
    "name": "Studio Kreativkopf",
    "inhaber": "Lisa Designerin",
    "tagline": "Visual Stories That Matter",
    "strasse": "Kreativquartier 8/15",
    "plz": "4020",
    "ort": "Linz",
    "land": "Österreich",
    "telefon": "+43 699 12345678",
    "email": "hello@kreativkopf.at",
    "web": "www.kreativkopf.at",
    "instagram": "@studio.kreativkopf",
    "behance": "behance.net/kreativkopf",
    "uid": "ATU71234567",
    "bank": "Bank Austria",
    "iban": "AT12 1234 5678 9012 3456",
    "bic": "BKAUATWW",
    "awards": ["Red Dot Winner 2024", "ADC Bronze 2023"]
  },
  "kunde": {
    "firma": "StartUp Heroes GmbH",
    "ansprechpartner": "Tom Founder",
    "strasse": "Innovation Hub 42",
    "plz": "4020",
    "ort": "Linz",
    "email": "tom@startup-heroes.com",
    "projekt": "Brand Identity Relaunch"
  },
  "rechnung": {
    "nummer": "2025-KK-089",
    "datum": "28.08.2025",
    "projekt_zeitraum": "15.07.2025 - 27.08.2025",
    "zahlungsziel": "11.09.2025",
    "brief_referenz": "Creative Brief v2.3 vom 10.07.2025"
  },
  "leistungen": [
    {
      "phase": "Discovery & Strategy",
      "items": [
        {
          "beschreibung": "Brand Workshop & Stakeholder Interviews",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 1200.00,
          "gesamt": 1200.00
        },
        {
          "beschreibung": "Competitor Analysis & Mood Boarding",
          "einheit": "Stunden",
          "menge": 8,
          "einzelpreis": 95.00,
          "gesamt": 760.00
        }
      ]
    },
    {
      "phase": "Design Development",
      "items": [
        {
          "beschreibung": "Logo Design - 3 Konzepte + 2 Überarbeitungsrunden",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 2400.00,
          "gesamt": 2400.00
        },
        {
          "beschreibung": "Color Palette & Typography System",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 800.00,
          "gesamt": 800.00
        },
        {
          "beschreibung": "Brand Pattern & Graphic Elements",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 600.00,
          "gesamt": 600.00
        }
      ]
    },
    {
      "phase": "Application Design",
      "items": [
        {
          "beschreibung": "Business Cards & Stationery",
          "einheit": "Set",
          "menge": 1,
          "einzelpreis": 450.00,
          "gesamt": 450.00
        },
        {
          "beschreibung": "Social Media Templates (12 Designs)",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 960.00,
          "gesamt": 960.00
        },
        {
          "beschreibung": "Website UI Kit (Desktop + Mobile)",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 1800.00,
          "gesamt": 1800.00
        },
        {
          "beschreibung": "Presentation Template (20 Slides)",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 650.00,
          "gesamt": 650.00
        }
      ]
    },
    {
      "phase": "Brand Guidelines",
      "items": [
        {
          "beschreibung": "Brand Manual (40 Pages PDF)",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 1200.00,
          "gesamt": 1200.00
        }
      ]
    },
    {
      "phase": "Extras",
      "items": [
        {
          "beschreibung": "Rush Delivery Surcharge (2 weeks faster)",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 500.00,
          "gesamt": 500.00
        },
        {
          "beschreibung": "Extended Usage Rights (Unlimited, All Media)",
          "einheit": "Pauschale",
          "menge": 1,
          "einzelpreis": 800.00,
          "gesamt": 800.00
        }
      ]
    }
  ],
  "zusammenfassung": {
    "subtotal_discovery": 1960.00,
    "subtotal_design": 3800.00,
    "subtotal_application": 3860.00,
    "subtotal_guidelines": 1200.00,
    "subtotal_extras": 1300.00,
    "rabatt_beschreibung": "Early Bird Discount 10%",
    "rabatt_prozent": 10,
    "rabatt_betrag": 1212.00,
    "summe_netto": 10908.00,
    "ust_20": 2181.60,
    "summe_brutto": 13089.60
  },
  "nutzungsrechte": {
    "umfang": "Exklusive, unbeschränkte Nutzungsrechte für alle Medien und Länder",
    "dauer": "Zeitlich unbegrenzt",
    "bearbeitung": "Bearbeitungsrecht eingeschlossen",
    "weitergabe": "Weitergabe an Tochtergesellschaften erlaubt",
    "archivierung": "Ursprungsdateien verbleiben bei Studio Kreativkopf für Portfolio"
  },
  "lieferung": {
    "methode": "WeTransfer Link + Google Drive Backup",
    "dateien": [
      "Logo (AI, EPS, SVG, PNG, JPG)",
      "Brand Guidelines (PDF, 40 Seiten)",
      "Social Media Templates (PSD, Canva)",
      "UI Kit (Figma, Sketch)",
      "Presentation (PPTX, KEY, Google Slides)",
      "Font Files (OTF, TTF, WOFF2)"
    ],
    "link": "https://we.tl/t-aBcDeF1234",
    "passwort": "StartUp2025!"
  },
  "testimonial": {
    "quote": "Lisa hat unsere Vision perfekt in ein visuelles Konzept übersetzt. Absolut empfehlenswert!",
    "author": "Sarah Chen, CEO TechStart (vorheriges Projekt)"
  }
}
```

### 9.3 Fill-Up Prompt für neue Rechnungen

```
Erstelle eine personality-driven Kreativ-Rechnung:

1. VISUAL HIERARCHY:
   - Wichtigste Info (Betrag, Nummer) prominent
   - Phasen farblich unterscheiden
   - Whitespace gezielt einsetzen
   - Typography als Designelement

2. PROJEKT-STORYTELLING:
   - Brief-Referenz verlinken
   - Moodboard-Preview einbinden
   - Prozess-Timeline visualisieren
   - Ergebnis-Showcase

3. RECHTE-MANAGEMENT:
   - Nutzungsrechte klar definieren
   - Zeitlich/räumlich eingrenzen
   - Exklusivität klären
   - Portfolio-Rechte sichern

4. KREATIV-PRICING:
   - Rush-Jobs mit Aufschlag
   - Friends-Rate transparent
   - Value-Based statt Hours
   - Package Deals hervorheben

5. DATEINAME CREATIVE:
   Format: invoice_[studioinitial]_[projekt]_[kunde]_[datum].html
   Beispiel: invoice_KK_brandidentity_startupheroes_20250828.html

6. PERSONALITY TOUCHES:
   - Emoji strategisch (max 5)
   - Handschrift-Font für Thank You
   - Farbakzent aus Kundenbrand
   - Instagram-Story Teaser

7. POST-PROJECT:
   - Feedback-Request
   - Portfolio-Permission
   - Testimonial-Bitte
   - Follow-up Service Hint
```

---

## Template 10: E-Commerce Modern

### 10.1 Initial Master Template Prompt

```
Erstelle eine moderne E-Commerce HTML-Rechnungsvorlage für österreichische Online-Händler:

DESIGN "Digital Commerce":
- Mobile-first Responsive Design
- One-Click Actions (Download, Print)
- Tracking-Integration visuell
- Return-Label QR-Code
- Newsletter Opt-in Banner

E-COMMERCE SPEZIFIKA:
- Bestellnummer prominent
- Lieferadresse ≠ Rechnungsadresse
- Versandkosten transparent
- Lieferstatus-Tracker
- Retourenhinweis mit Frist

CROSS-BORDER COMMERCE:
- Multi-Currency Display
- EU-OSS Nummer
- Zollhinweise Non-EU
- IOSS für Kleinbeträge
- Incoterms bei B2B

DIGITALE FEATURES:
- Produktbilder inline
- SKU/EAN Codes
- Lagerbestand-Info
- Cross-Selling Suggestions
- Review-Request Link

SUSTAINABILITY:
- CO2-Footprint Berechnung
- Klimaneutraler Versand Badge
- Recycling-Hinweise
- Local Sourcing Info
- Plastic-Free Packaging Icon

Conversion-optimized template mit {{vars}}.
```

### 10.2 Master Template mit Mock-Daten JSON

```json
{
  "shop": {
    "name": "AlpenStyle Online GmbH",
    "claim": "Tiroler Qualität - Direkt zu Ihnen",
    "strasse": "E-Commerce Park 10",
    "plz": "6063",
    "ort": "Rum bei Innsbruck",
    "land": "Österreich",
    "telefon": "+43 512 987654",
    "email": "service@alpenstyle.at",
    "web": "www.alpenstyle.at",
    "uid": "ATU74123698",
    "eori": "ATEOS7412369800",
    "oss_nummer": "EU372012345",
    "firmenbuch": "FN 478965s",
    "bank": "Erste Bank",
    "iban": "AT55 2011 1234 5678 9012",
    "bic": "GIBAATWWXXX",
    "trustpilot": "4.8/5.0 (2,847 Bewertungen)",
    "gütesiegel": ["Österreichisches E-Commerce Gütezeichen", "Trusted Shops"]
  },
  "kunde": {
    "kundennummer": "K-458796",
    "anrede": "Frau",
    "vorname": "Julia",
    "nachname": "Bergmann",
    "email": "julia.bergmann@email.de",
    "telefon": "+49 170 1234567",
    "rechnungsadresse": {
      "strasse": "Hauptstraße 42",
      "plz": "80331",
      "ort": "München",
      "land": "Deutschland"
    },
    "lieferadresse": {
      "empfaenger": "Julia Bergmann",
      "strasse": "Hauptstraße 42",
      "plz": "80331",
      "ort": "München",
      "land": "Deutschland"
    },
    "newsletter": false,
    "kundenkonto": true
  },
  "bestellung": {
    "bestellnummer": "AS-2025-98745",
    "bestelldatum": "26.08.2025 14:23",
    "rechnungsnummer": "RE-2025-45789",
    "rechnungsdatum": "28.08.2025",
    "zahlungsart": "PayPal",
    "zahlungsstatus": "Bezahlt",
    "versandart": "DHL Express",
    "tracking": "12345678901234",
    "voraussichtliche_lieferung": "30.08.2025"
  },
  "artikel": [
    {
      "bild": "product_001_thumb.jpg",
      "artikelnummer": "TRA-425",
      "ean": "9001234567890",
      "bezeichnung": "Tiroler Wanderrucksack 'Gipfelstürmer' 45L",
      "farbe": "Alpingrün",
      "groesse": "L",
      "menge": 1,
      "einzelpreis": 189.90,
      "rabatt_prozent": 20,
      "rabatt_betrag": 37.98,
      "zwischensumme": 151.92,
      "steuersatz": 20,
      "lagerbestand": "Verfügbar",
      "herkunft": "Handgefertigt in Tirol"
    },
    {
      "bild": "product_002_thumb.jpg",
      "artikelnummer": "JAC-782",
      "ean": "9001234567891",
      "bezeichnung": "Merino-Wolljacke 'Alpenwärme'",
      "farbe": "Naturgrau",
      "groesse": "M",
      "menge": 1,
      "einzelpreis": 129.00,
      "rabatt_prozent": 0,
      "rabatt_betrag": 0,
      "zwischensumme": 129.00,
      "steuersatz": 20,
      "lagerbestand": "Nur noch 3 Stück",
      "herkunft": "100% Tiroler Bergschaf-Wolle"
    },
    {
      "bild": "product_003_thumb.jpg",
      "artikelnummer": "SOC-234",
      "ean": "9001234567892",
      "bezeichnung": "Wandersocken 'Bergfex' 3er Pack",
      "farbe": "Anthrazit",
      "groesse": "39-42",
      "menge": 2,
      "einzelpreis": 24.90,
      "rabatt_prozent": 0,
      "rabatt_betrag": 0,
      "zwischensumme": 49.80,
      "steuersatz": 20,
      "lagerbestand": "Verfügbar",
      "herkunft": "Produziert in Österreich"
    },
    {
      "bild": "gift_wrap.jpg",
      "artikelnummer": "GIFT-01",
      "ean": "",
      "bezeichnung": "Geschenkverpackung Premium",
      "farbe": "",
      "groesse": "",
      "menge": 1,
      "einzelpreis": 4.90,
      "rabatt_prozent": 0,
      "rabatt_betrag": 0,
      "zwischensumme": 4.90,
      "steuersatz": 20,
      "lagerbestand": "",
      "herkunft": "Recyceltes Papier"
    }
  ],
  "gutschein": {
    "code": "SOMMER2025",
    "beschreibung": "Sommeraktion -20% auf Wanderrucksäcke",
    "wert": 37.98
  },
  "versand": {
    "bezeichnung": "DHL Express (1-2 Werktage)",
    "kosten": 9.90,
    "steuersatz": 20,
    "kostenlos_ab": 99.00,
    "tracking_url": "https://www.dhl.de/track?trackingNumber=12345678901234"
  },
  "zusammenfassung": {
    "warenwert": 373.70,
    "rabatte_gesamt": 37.98,
    "zwischensumme": 335.72,
    "versandkosten": 9.90,
    "summe_netto": 288.02,
    "ust_20_de": 57.60,
    "summe_brutto": 345.62
  },
  "oss_hinweis": {
    "text": "Die Umsatzsteuer wird gemäß One-Stop-Shop-Verfahren (OSS) für Deutschland (20%) abgeführt.",
    "registrierung": "OSS-Registrierungsnummer: EU372012345"
  },
  "sustainability": {
    "co2_footprint": "2.3 kg CO₂",
    "kompensation": "Klimaneutral durch Aufforstungsprojekt in Tirol",
    "verpackung": "100% recyclebar, plastikfrei",
    "versand": "DHL GoGreen klimaneutraler Versand"
  },
  "retoure": {
    "frist": "30 Tage Rückgaberecht",
    "portal_link": "https://www.alpenstyle.at/retoure",
    "label_qr": "GENERATE_RETURN_QR_HERE",
    "hinweis": "Einfache Rücksendung über unser Online-Portal. QR-Code scannen oder Link nutzen."
  },
  "cross_selling": [
    {
      "artikelnummer": "CAP-567",
      "bezeichnung": "Wanderhut 'Sonnenschutz'",
      "preis": 39.90,
      "rabatt": "Nur für Sie: -15% mit Code KUNDE15"
    },
    {
      "artikelnummer": "FLA-890",
      "bezeichnung": "Edelstahl-Trinkflasche 1L",
      "preis": 29.90,
      "rabatt": "Bundle-Preis: -10% bei Kombination"
    }
  ],
  "kundenservice": {
    "hotline": "+43 512 987654",
    "zeiten": "Mo-Fr 9-18 Uhr, Sa 9-14 Uhr",
    "chat": "Live-Chat auf www.alpenstyle.at",
    "email": "service@alpenstyle.at",
    "bewertung": "Bewerten Sie uns auf Trustpilot!",
    "newsletter_hinweis": "10% Rabatt bei Newsletter-Anmeldung auf Ihre nächste Bestellung"
  }
}
```

### 10.3 Fill-Up Prompt für neue Rechnungen

```
Generiere eine conversion-optimierte E-Commerce-Rechnung:

1. VISUELLE HIERARCHIE:
   - Bestellnummer XXL für Support
   - Tracking-Button prominent
   - Retour-QR above the fold
   - Produktbilder für Recognition

2. CROSS-BORDER INTELLIGENCE:
   - DE-Kunde: 19% dt. MwSt via OSS
   - CH-Kunde: Zollhinweis prominent
   - EU: Versandkosten-Schwelle anpassen
   - Non-EU: IOSS wenn <150€

3. PERSONALISIERUNG:
   - Vorname in Anrede verwenden
   - Purchase History Reference
   - Relevant Cross-Sells (Data-Driven)
   - Birthday Discount wenn Monat passt

4. SUSTAINABILITY SCORING:
   - CO2 pro Artikel berechnen
   - Gesamt-Footprint visualisieren
   - Kompensation hervorheben
   - Öko-Badges prominent

5. DATEINAME E-COM:
   Format: order_[bestellnr]_[kunde]_invoice.html
   Beispiel: order_AS-2025-98745_bergmann_invoice.html

6. CONVERSION ELEMENTS:
   - Review-Request nach 7 Tagen
   - Newsletter 10% if not subscribed
   - Loyalty Points anzeigen
   - Referral Code personalisiert

7. MOBILE OPTIMIZATION:
   - Finger-friendly Buttons
   - Scrollable Produktliste
   - Collapsible Sections
   - One-Tap Actions (Download/Share)
```

---

## Template 11: Rechtsanwalt Formal

### 11.1 Initial Master Template Prompt

```
Erstelle eine formal-elegante HTML-Honorarnote für österreichische Rechtsanwälte:

DESIGN "Legal Excellence":
- Klassisch-konservatives Layout
- Dunkelblau (#003366) und Gold (#B8860B)
- Traditionelle Serifenschrift (Garamond)
- Wappen/Siegel Position für Kanzlei-Logo
- Pergament-Textur subtle

RECHTSANWALTS-SPEZIFIKA:
- Honorarnote statt Rechnung
- RATG/AHK Referenzen
- Leistungsverzeichnis nach TP
- Barauslagen separat
- Verfahrenshilfe-Hinweise

GEBÜHRENORDNUNG:
- Tarifposten nach RATG
- Einheitssatz-Multiplikator
- Streitwert-Bezug
- Pauschalhonorar-Option
- Erfolgshonorar-Komponente (wo zulässig)

VERTRAUENSELEMENTE:
- RAK-Mitgliedsnummer
- Berufshaftpflicht-Details
- Verschwiegenheitsverpflichtung
- Treuhandkonto-Hinweis
- Verjährungshinweise

SPEZIAL-POSITIONEN:
- Gerichtsgebühren
- Sachverständigenkosten
- Übersetzungen/Beglaubigungen
- Reisekosten nach RATG
- Kopien/Porto nach Aufwand

Juristische Präzision mit {{variablen}}.
```

### 11.2 Master Template mit Mock-Daten JSON

```json
{
  "kanzlei": {
    "name": "Dr. Maximilian Recht & Partner",
    "zusatz": "Rechtsanwälte - Attorneys at Law",
    "strasse": "Justizplatz 1",
    "plz": "1010",
    "ort": "Wien",
    "land": "Österreich",
    "telefon": "+43 1 234 5678",
    "fax": "+43 1 234 5679",
    "email": "office@recht-partner.at",
    "web": "www.recht-partner.at",
    "uid": "ATU12345678",
    "rak_nummer": "R 123456",
    "treuhandkonto": {
      "bank": "BAWAG P.S.K.",
      "iban": "AT12 1400 0123 4567 8901",
      "bic": "BAWAATWW",
      "lautend": "RA Dr. Maximilian Recht - Anderkonto"
    },
    "hauptkonto": {
      "bank": "Erste Bank",
      "iban": "AT65 2011 1234 5678 9012",
      "bic": "GIBAATWWXXX"
    },
    "haftpflicht": "HDI Versicherung AG, Pol.Nr. BH-2024-RA-4567"
  },
  "mandant": {
    "anrede": "Sehr geehrter Herr",
    "titel": "Mag.",
    "vorname": "Andreas",
    "nachname": "Unternehmer",
    "firma": "Unternehmer Holding GmbH",
    "position": "Geschäftsführer",
    "strasse": "Businesspark 100",
    "plz": "4020",
    "ort": "Linz",
    "land": "Österreich",
    "uid": "ATU98765432"
  },
  "honorarnote": {
    "nummer": "HN-2025-0789",
    "datum": "28.08.2025",
    "aktenzeichen": "AZ 2024/1234-MR",
    "leistungszeitraum": "01.03.2024 - 31.07.2025",
    "zahlungsziel": "14 Tage",
    "faellig": "11.09.2025",
    "betreff": "Rechtssache Unternehmer GmbH ./. Konkurrent AG"
  },
  "verfahren": {
    "gericht": "Handelsgericht Wien",
    "geschaeftszahl": "56 Cg 123/24",
    "streitwert": 250000.00,
    "verfahrensart": "Zivilprozess",
    "erfolg": "Vollständiger Prozesserfolg - Urteil vom 15.07.2025"
  },
  "leistungen": [
    {
      "kategorie": "Gerichtliche Vertretung",
      "positionen": [
        {
          "tp": "TP 3A",
          "beschreibung": "Klage",
          "basis": 5817.00,
          "einheitssatz": 1.2,
          "betrag": 6980.40
        },
        {
          "tp": "TP 3A",
          "beschreibung": "Klagebeantwortung",
          "basis": 5817.00,
          "einheitssatz": 1.2,
          "betrag": 6980.40
        },
        {
          "tp": "TP 3A",
          "beschreibung": "Vorbereitung Verhandlung (3 Verhandlungen)",
          "basis": 2908.50,
          "einheitssatz": 3.6,
          "betrag": 10470.60
        },
        {
          "tp": "TP 3A",
          "beschreibung": "Streitverhandlung (3 × 4 Stunden)",
          "basis": 1745.10,
          "einheitssatz": 14.4,
          "betrag": 25129.44
        }
      ]
    },
    {
      "kategorie": "Außergerichtliche Vertretung",
      "positionen": [
        {
          "tp": "Pauschale",
          "beschreibung": "Vertragsgestaltung und Verhandlungen",
          "basis": 0,
          "einheitssatz": 0,
          "betrag": 8500.00
        },
        {
          "tp": "TP 5",
          "beschreibung": "Rechtsauskunft und Beratung",
          "basis": 450.00,
          "einheitssatz": 6,
          "betrag": 2700.00
        },
        {
          "tp": "TP 7",
          "beschreibung": "Teilnahme an Besprechungen (8 Stunden)",
          "basis": 120.00,
          "einheitssatz": 8,
          "betrag": 960.00
        }
      ]
    },
    {
      "kategorie": "Barauslagen",
      "positionen": [
        {
          "beschreibung": "Gerichtsgebühren (Pauschalgebühr)",
          "betrag": 5639.00
        },
        {
          "beschreibung": "Sachverständigengebühr Dr. Gutachter",
          "betrag": 3500.00
        },
        {
          "beschreibung": "Zeugengebühren",
          "betrag": 245.60
        },
        {
          "beschreibung": "Beglaubigte Übersetzungen (EN-DE)",
          "betrag": 780.00
        },
        {
          "beschreibung": "Grundbuchs- und Firmenbuchauszüge",
          "betrag": 186.00
        },
        {
          "beschreibung": "ERV-Gebühren",
          "betrag": 48.50
        },
        {
          "beschreibung": "Kopien (2.450 Seiten à € 0,50)",
          "betrag": 1225.00
        },
        {
          "beschreibung": "Porto und Zustellkosten",
          "betrag": 89.30
        }
      ]
    },
    {
      "kategorie": "Reisekosten",
      "positionen": [
        {
          "beschreibung": "Fahrtkosten Wien-Linz (3 × 368 km à € 0,42)",
          "betrag": 463.68
        },
        {
          "beschreibung": "Tagesgebühren (3 Tage à € 35,10)",
          "betrag": 105.30
        }
      ]
    }
  ],
  "zusammenfassung": {
    "honorar_gerichtlich": 49560.84,
    "honorar_aussergerichtlich": 12160.00,
    "zwischensumme_honorar": 61720.84,
    "barauslagen": 11713.40,
    "reisekosten": 568.98,
    "summe_netto": 74003.22,
    "ust_20": 14800.64,
    "summe_brutto": 88803.86,
    "gegnerischer_kostenersatz": 45000.00,
    "vom_mandanten_zu_tragen": 43803.86
  },
  "kostenersatz": {
    "hinweis": "Dem Mandanten wurde vom Gegner ein Kostenersatz in Höhe von EUR 45.000,00 zugesprochen. Dieser Betrag wurde bereits in Abzug gebracht.",
    "zahlungseingang": "Der Kostenersatz wurde am 20.08.2025 auf unserem Treuhandkonto vereinnahmt."
  },
  "hinweise": {
    "faelligkeit": "Wir ersuchen um Überweisung des offenen Betrages binnen 14 Tagen auf unser Hauptkonto.",
    "vorbehalt": "Diese Honorarnote wurde nach bestem Wissen erstellt. Ergänzungen bleiben vorbehalten.",
    "verschwiegenheit": "Sämtliche Informationen unterliegen der anwaltlichen Verschwiegenheitspflicht.",
    "verjaehrung": "Honoraransprüche verjähren nach § 1486 Z 1 ABGB binnen drei Jahren.",
    "beschwerde": "Beschwerden können bei der Rechtsanwaltskammer Wien eingebracht werden."
  }
}
```

### 11.3 Fill-Up Prompt für neue Rechnungen

```
Erstelle eine formal korrekte Anwalts-Honorarnote:

1. GEBÜHREN-KALKULATION:
   - RATG-Tarifposten korrekt anwenden
   - Streitwert-Bemessungsgrundlage
   - Einheitssatz begründet
   - Degression bei Mehrfachleistungen
   - USt auf Honorar, nicht Auslagen

2. BARAUSLAGEN-DETAIL:
   - Gerichtsgebühren exakt
   - Sachverständige mit Beschluss
   - ERV-Eingaben einzeln
   - Kopien mit Seitenanzahl
   - Alles belegbar

3. KOSTENERSATZ-LOGIK:
   - Zugesprochener Betrag klar
   - Bereits vereinnahmt?
   - Differenz für Mandant
   - Treuhandkonto-Verwaltung

4. FORMALE PRÄZISION:
   - Aktenzeichen konsistent
   - Geschäftszahl korrekt
   - Leistungszeitraum exakt
   - Verjährungshinweise

5. DATEINAME KANZLEI:
   Format: HN_[jahr]_[nummer]_[mandant]_[az].html
   Beispiel: HN_2025_0789_unternehmer_2024-1234.html

6. ETHIK-CHECKS:
   - Erfolgshonorar nur wo zulässig
   - Interessenkonflikt geprüft?
   - Verschwiegenheit gewahrt?
   - Treuhandgelder korrekt?

7. ZAHLUNGS-MODALITÄTEN:
   - Hauptkonto für Honorar
   - Treuhandkonto für Fremdgelder
   - Ratenzahlung bei hohen Beträgen
   - Verfahrenshilfe-Abrechnung separat
```

---

## Template 12: Gastgewerbe Restaurant

### 12.1 Initial Master Template Prompt

```
Entwickle eine HTML-Rechnungsvorlage für österreichische Gastronomiebetriebe:

DESIGN "Culinary Excellence":
- Appetitliche Farbgebung (Weinrot #722F37, Créme #FFF8DC)
- Menu-Card inspiriertes Layout
- Handschrift-Fonts für Specials
- Wasserzeichen mit Restaurant-Logo
- Mobile-optimiert für Kellner-Tablets

GASTRO-SPEZIFIKA:
- Registrierkassen-Nummer
- Bewirtungsbeleg-konform
- Getränke/Speisen getrennt
- Happy Hour Preise
- Trinkgeld-Zeile optional

STEUER-KOMPLEXITÄT:
-