# Handwerker Classic - Invoice Creation Prompt

Nimm das Handwerker-Master-Template und fülle es mit den Daten aus der JSON-Datei. 
Beachte dabei:

## 1. Template-Befüllung:
- Ersetze alle {{placeholder}} mit den entsprechenden Werten aus dem JSON
- Formatiere alle Währungsbeträge mit österreichischem Format: 1.234,56 €

## 2. Automatische Berechnungen:
- Einzelne Positionsbeträge (Menge × Einzelpreis)
- Steuersätze korrekt zuordnen (Material und Arbeit meist 20%, Lebensmittel 10%)
- Netto-Zwischensummen nach Kategorien
- USt-Beträge pro Steuersatz
- Brutto-Endsumme
- Skontobetrag bei 2% und Endpreis mit Skonto

## 3. Dateinamen-Generierung:
Format: `rechnung_[rechnungsnummer]_[kundenname]_[datum].html`
Beispiel: `rechnung_RE-2025-00142_berger_20250315.html`

## 4. Intelligente Textbausteine:
- Bei Privatpersonen: Handwerkerbonus-Hinweis
- Bei B2B mit UID: "Zahlung ohne Abzug" statt Skonto
- Saisonale Grüße (Weihnachten, Ostern) wenn zutreffend

## 5. Compliance-Check:
Validiere dass alle Pflichtangaben gemäß §11 UStG vorhanden sind:
- Firmenname und Adresse des Leistungserbringers
- Name und Adresse des Empfängers
- Menge und Bezeichnung der Waren/Leistungen
- Lieferdatum
- Nettobetrag und Steuersatz
- Umsatzsteuerbetrag
- Rechnungsdatum
- Fortlaufende Rechnungsnummer
- UID-Nummer des Ausstellers