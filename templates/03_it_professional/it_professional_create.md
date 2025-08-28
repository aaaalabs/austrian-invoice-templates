# IT-Professional Template - Fill-Up Prompt für neue Rechnungen

Erstelle aus dem IT-Professional-Template eine detaillierte Rechnung:

## 1. TECHNISCHE AUFBEREITUNG:
- Parse Ticket-Referenzen und erstelle Hyperlinks zu JIRA
- Gruppiere Stunden nach Technologie-Stack
- Berechne Remote vs. Onsite Ratio
- Generiere Burndown-Chart für Projektstunden

## 2. B2B-SPEZIALBEHANDLUNG:
- Bei EU-Kunde mit UID: Reverse Charge anwenden
- Text: "Steuerschuldnerschaft des Leistungsempfängers"
- Keine USt ausweisen, nur Nettobetrag
- Bei AT-Kunde: normale 20% USt

## 3. CHANGE REQUEST LOGIK:
- CRs als separate Sektion nach Hauptpositionen
- Verweis auf schriftliche Genehmigung
- Zusatzstunden klar kennzeichnen
- Impact auf Timeline dokumentieren

## 4. SLA-ABHÄNGIGE TEXTE:
- Gold: "Priority Support with 2h response time"
- Silver: "Business hours support, 4h response"  
- Bronze: "Next business day response"

## 5. DATEINAME-PATTERN:
Format: `it_invoice_[nummer]_[kunde]_[projekt]_[periode].html`

Beispiel: `it_invoice_IT-2025-00389_innovationhub_PRJ-2025-0142_202508.html`

## 6. AUTOMATISCHE ERGÄNZUNGEN:
- Git-Commit-Summary der Periode (letzte 10 commits)
- Test-Coverage Percentage wenn verfügbar
- Deployment-Status (Dev/Staging/Production)
- Knowledge Transfer Dokumentation Verweis

## 7. ZAHLUNGS-INTELLIGENZ:
- Bei Beträgen >10k€: Ratenzahlung Option
- Crypto-Payment: Aktuellen EUR-Kurs anzeigen
- SEPA-Lastschrift: Mandat-Referenz einfügen