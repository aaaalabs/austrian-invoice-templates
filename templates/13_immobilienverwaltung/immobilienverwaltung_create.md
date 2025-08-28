# Immobilienverwaltung - Invoice Creation Prompt

Nimm das Immobilienverwaltung-Master-Template und fülle es mit den Daten aus der JSON-Datei. 
Beachte dabei:

## 1. Template-Befüllung:
- Ersetze alle {{placeholder}} mit den entsprechenden Werten aus dem JSON
- Formatiere alle Währungsbeträge mit österreichischem Format: 1.234,56 €
- Objektreferenzen und Eigentumsanteile korrekt darstellen

## 2. Immobilien-spezifische Berechnungen:
- Einzelne Positionsbeträge nach Verwaltungskategorien
- Steuersätze korrekt zuordnen (Immobilienverwaltung meist 20% USt)
- Netto-Zwischensummen nach Kategorien:
  * Hausverwaltung (pauschale Leistungen)
  * Nebenkostenabrechnungen (Betriebskosten)
  * Sonderverwaltungsleistungen (einmalige Projekte)
  * Service-Leistungen (Betreuung, Begehungen)
- USt-Beträge pro Steuersatz
- Brutto-Endsumme ohne Skonto (in der Branche unüblich)

## 3. Dateinamen-Generierung:
Format: `immobilien_[rechnungsnummer]_[kundenname]_[objekt]_[datum].html`
Beispiel: `immobilien_IV-2025-00089_mueller_sonnenhof_20250215.html`

## 4. Immobilien-spezifische Textbausteine:
- Bei Eigentumsanteilen: Genauer Anteil und Objektbezug
- Bei Nebenkostenabrechnungen: Abrechnungsperiode und Umlageschlüssel
- Bei Sonderumlagen: Verweis auf Eigentümerversammlung/Beschluss
- Verwaltungsvereinbarungsreferenz einbinden
- 22-jährige Aufbewahrungspflicht-Hinweis prominent darstellen

## 5. Professionelle Gestaltung:
- Vertrauensvolle Optik für Immobilieneigentümer
- Objektdaten übersichtlich im Header-Bereich
- Kategorisierte Leistungsdarstellung
- Klare Trennung zwischen laufenden und einmaligen Kosten
- Haftpflichtversicherung und Konzessionsdaten sichtbar

## 6. Compliance-Check:
Validiere dass alle Pflichtangaben gemäß §11 UStG vorhanden sind:
- Firmenname und Adresse des Leistungserbringers
- Name und Adresse des Empfängers  
- Objektadresse und -bezeichnung
- Menge und Bezeichnung der Verwaltungsleistungen
- Leistungszeitraum/Abrechnungsperiode
- Nettobetrag und Steuersatz
- Umsatzsteuerbetrag
- Rechnungsdatum
- Fortlaufende Rechnungsnummer (IV-Format)
- UID-Nummer des Ausstellers
- Gewerbeberechtigung und Konzessionshinweise

## 7. Zusätzliche Immobilien-Compliance:
- Verweis auf 22-jährige Dokumentenaufbewahrung
- DSGVO-Datenschutzhinweis für personenbezogene Daten
- ÖVI-Mitgliedschaft und WKO-Konzession erwähnen
- Haftpflichtversicherungsnachweis integrieren