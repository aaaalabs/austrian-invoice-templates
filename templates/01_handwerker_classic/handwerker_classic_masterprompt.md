# Handwerker Classic - Master Template Prompt

Erstelle eine HTML-Rechnungsvorlage für einen österreichischen Handwerksbetrieb mit folgenden Spezifikationen:

## DESIGN:
- Klassisches A4-Format mit konservativem blau-grauem Farbschema
- Firmenlogo oben rechts (150x60px Platzhalter)
- Strukturierte Tabelle mit klarer Material-Arbeitszeit-Trennung
- Tiroler Wappen dezent als Wasserzeichen (10% Opacity)

## PFLICHTFELDER gemäß §11 UStG:
- Vollständiger Firmenkopf mit österreichischer Adresse
- Fortlaufende Rechnungsnummer Format: RE-2025-XXXXX
- UID-Nummer Format: ATU12345678
- Leistungsdatum/Zeitraum mit österreichischem Datumsformat (TT.MM.JJJJ)
- Detaillierte Leistungsbeschreibung mit getrennten Spalten für:
  * Materialkosten (10% oder 20% USt)
  * Arbeitskosten (20% USt) - wichtig für steuerliche Absetzbarkeit
  * Fahrtkosten/Pauschalen

## SPEZIELLE ELEMENTE:
- Handwerkerbonus-Hinweis für Privatkunden
- Gewährleistungshinweis nach österreichischem Recht (2 Jahre)
- Zahlungsziel: "14 Tage 2% Skonto, 30 Tage netto"
- Bankverbindung mit österreichischer IBAN (AT...)
- Gerichtsstand und Firmenbuchnummer

## FOOTER:
- Geschäftsführer-Namen
- Kontaktdaten (Tel, Email, Web)
- "Mitglied der WKO Tirol - Landesinnung [Gewerk]"

Verwende Platzhalter im Format {{feldname}} für alle variablen Daten.