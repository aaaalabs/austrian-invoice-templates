# Template 5: B2B Reverse Charge EU - Fill-Up Prompt

## Fill-Up Prompt für neue Rechnungen

Generiere eine konforme Reverse-Charge-Rechnung mit folgenden Prüfungen:

### 1. REVERSE CHARGE VALIDIERUNG:
- Check: B2B-Status (beide UIDs vorhanden?)
- Check: Grenzüberschreitend (verschiedene Länder?)
- Check: Dienstleistung (nicht Warenlieferung?)
- Wenn alle JA: Reverse Charge anwenden
- Wenn NEIN: Warnung ausgeben

### 2. SPRACHLICHE AUFBEREITUNG:
- Hauptsprache = Kundenland-Sprache
- Backup immer Englisch
- Rechtliche Hinweise IMMER auch Deutsch
- Beträge in Worten in beiden Sprachen

### 3. COMPLIANCE-DOKUMENTATION:
- VIES-Check Timestamp einfügen
- Screenshot-Referenz zur UID-Validierung
- Leistungsort-Paragraph zitieren
- EU-Richtlinie Artikel nennen

### 4. SPEZIALFÄLLE BEHANDLUNG:
- Bauleistung Inland AT: Auch Reverse Charge!
- Grundstücksleistungen: Immer Leistungsort-Land
- Telekom an Privatpersonen: KEIN Reverse Charge
- Elektronische Dienstleistungen: OSS prüfen

### 5. DATEINAME INTERNATIONAL:
Format: invoice_EU_[nummer]_[kunde_land]_[datum].html
Beispiel: invoice_EU_EU-2025-00089_NL_20250828.html

### 6. WÄHRUNGS-INTELLIGENZ:
- Hauptwährung immer EUR
- Bei UK-Kunden: GBP Referenz anzeigen
- Bei CH-Kunden: CHF Referenz anzeigen
- Tageskurs von EZB API oder fix 

### 7. ZAHLUNGSWEG-OPTIMIERUNG:
- SEPA für EU-Länder
- SWIFT für Non-EU
- Gebührenteilung OUR/SHA/BEN klären
- Payment Terms nach Land anpassen