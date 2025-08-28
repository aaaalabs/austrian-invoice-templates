# Solar/PV Modern Template - Fill-Up Prompt für neue Rechnungen

Generiere aus dem Solar-Master-Template eine vollständige Rechnung mit folgenden Anweisungen:

## 1. DATENVERARBEITUNG:
- Befülle alle {{placeholder}} mit JSON-Werten
- Berechne Energiekosten-Ersparnis (0,38€/kWh × Jahresertrag)
- Erstelle Wirtschaftlichkeitsgrafik mit Amortisationskurve
- Generiere QR-Code mit korrekten Zahlungsdaten

## 2. FÖRDER-LOGIK:
- Wenn Anlagenleistung ≤35 kWp: USt-Befreiung anwenden
- Wenn >35 kWp: 20% USt berechnen
- Prüfe aktuelle Fördersätze (EAG, Land, Gemeinde)
- Berechne Nettokosten nach Förderung

## 3. DYNAMISCHE TEXTBAUSTEINE:
- Bei KJUUBE: "Modularer Speicher - jederzeit erweiterbar"
- Bei NTUITY: "KI-optimiertes Energiemanagement"
- Sommer (Apr-Sep): "Nutzen Sie die starken Sonnenmonate optimal"
- Winter (Okt-Mär): "Auch im Winter produziert Ihre Anlage wertvollen Strom"

## 4. DATEINAME-GENERIERUNG:
Format: solar_rechnung_[nummer]_[kunde]_[kwp]kwp_[datum].html
Beispiel: solar_rechnung_RE-2025-00247_schneider_12kwp_20250828.html

## 5. QUALITÄTSCHECKS:
- Seriennummern für Garantie vorhanden?
- Netzanschluss-Referenz eingefügt?
- CO2-Berechnung plausibel? (0,4kg CO2/kWh × Jahresertrag)
- Förderhinweise aktuell? (Check gegen 2025 Sätze)

## 6. BONUS-ELEMENTE:
- Google Review Link personalisiert
- Empfehlungsprogramm-Hinweis (500€ pro Neukunde)
- Sonnige Grüße-Signatur ("Sonnige Grüße aus Tirol")