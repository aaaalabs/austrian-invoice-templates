# Energiegemeinschaft NEU Template - Professional Creation Guide

## Template Beschreibung
Professionelle HTML-Rechnungsvorlage für österreichische Erneuerbare-Energie-Gemeinschaften (EEG) nach höchsten Industriestandards der Energiewirtschaft. Vollständige Compliance mit ElWOG 2010, E-Control Anforderungen und technischen Standards für business-grade Energieabrechnung.

## Zielgruppe
- **Erneuerbare-Energie-Gemeinschaften (EEG)** nach §16a ElWOG 2010
- **Bürgerenergiegemeinschaften (BEG)** mit Österreich-weiter Ausrichtung  
- **Regionale Energieversorger** mit Community-Fokus
- **Professional Service Provider** für EEG-Administration
- **Energy Consultants** mit EEG-Spezialisierung

## Professional Design Standards

### 🎯 Energy Sector Documentation Design
- **Minimales Farbschema**: Energieblau (#003366), Neutralgrau, Papierweiß
- **Professional Typografie**: Arial/Helvetica für maximale Print-Kompatibilität
- **Technical Layout**: ISO 14001/50001 Energiemanagement-Standards
- **Print-Optimiert**: Perfekte A4-Darstellung in Schwarz-Weiß
- **Business Credibility**: Indistinguishable von etablierten Energieversorgern

### ⚖️ Austrian Legal Compliance (ElWOG 2010)
- **§16a ff EEG-Bestimmungen**: Vollständige regulatorische Konformität
- **§16e Abs 3 Transparenzpflicht**: Separate Ausweisung EEG/Netzbezug
- **E-Control Registrierung**: Korrekte Formatierung EEG-AT-YYYY-NNNN-LLL
- **DSO-Integration**: Smart Meter Pflichten und Datenbereitstellung
- **UStG §11 Compliance**: Alle 9 Pflichtangaben vollständig implementiert

## Technical Data Structure

### Enhanced EEG-Specific Fields
```json
{
  "eeg": {
    "name": "Erneuerbare-Energie-Gemeinschaft Alpental",
    "registrierung": "EEG-AT-2024-0158-TIR",
    "econtrol_nummer": "EEG-AT-2024-0158-TIR",
    "rechtsform": "Verein",
    "konzessionsgebiet": "Innsbrucker Kommunalbetriebe AG"
  },
  "mitglied": {
    "nummer": "EEG-ALT-2024-0089",
    "zahlpunkt_id": "AT003300000000000000123456789012",
    "smart_meter_nummer": "EDLA2024TIR567890123",
    "anlagentyp": "Verbraucher|Erzeuger|Prosumer"
  },
  "energieabrechnung": {
    "autarkiegrad_prozent": 70.6,
    "netzentgelt_reduzierung_prozent": 28.5,
    "energielenkungsabgabe_befreiung": true,
    "oekostromfoerder_befreiung": true
  }
}
```

### Professional Administrative Documentation
- **Technische Details**: OBIS-Codes, Smart Meter Nummern, MID-Konformität
- **Regulatory Compliance**: E-Control Meldepflichten, DSO-Pflichten
- **Financial Transparency**: Separate Netzentgelte, reduzierte Abgaben
- **Technical Integration**: DLMS/COSEM Protokolle, Viertelstundenwerte

## Austrian Energy Law Compliance Framework

### ElWOG 2010 Implementation Requirements
- **§16a EEG-Gründung**: Mindestens 2 Teilnehmer im DSO-Konzessionsgebiet
- **§16b Rechtsform**: Verein, Genossenschaft oder Gesellschaft mit Rechtspersönlichkeit
- **§16c Teilnahmekriterien**: Natürliche/juristische Personen, Gemeinden, KMU
- **§16e Energiebilanz**: DSO-Pflicht für separate EEG/Netzbezug-Ausweisung
- **§16f Administrative Pflichten**: E-Control Registrierung und jährliche Bestätigung

### Energy Community Incentive System (2025 Updates)
- **Netzentgelt-Reduktion**: 28.5% für lokalen EEG-Anteil
- **Ökostromförderbeitrag**: Kompletter Wegfall für EEG-Energie
- **Elektrizitätsabgabe**: Befreiung für PV-Anlagen unter 25 kWp
- **Systemnutzungstarif**: Reduzierte Tarife für lokale Energienutzung

### Professional Invoice Structure Requirements
- **Header Section**: Vollständige EEG-Bezeichnung mit E-Control Registrierung
- **Member Information**: Eindeutige IDs, Zählpunkt-Referenzen, Anlagentyp
- **Energy Balance Table**: Separierte EEG/Netzbezug-Darstellung nach §16e
- **Technical Details**: Smart Meter Integration, OBIS-Codes, Messintervalle
- **Legal Compliance**: UStG §11 vollständig, ElWOG-Referenzen, Datenschutz

## Business-Grade Implementation Guidelines

### Industry-Standard Terminology Usage
- **E-Control Austria**: Offizielle Regulierungsautorität-Terminologie
- **DSO Integration**: Distribution System Operator Fachbegriffe
- **Smart Metering**: OBIS-Code Standards und MID-Konformität  
- **Energy Management**: Lastprofil, Viertelstundenwerte, Energiebilanzierung
- **Legal References**: Exakte ElWOG/EAG Paragraphen-Zitierung

### Professional Print Standards
- **A4 Format**: 210x297mm mit 20mm Rändern für Businessdokumentation
- **Monochrome Design**: Optimiert für kosteneffektives Schwarz-Weiß-Drucken
- **Typography Hierarchy**: 16pt Überschriften, 11pt Body, 9pt Details
- **Table Structure**: Klare Linien für technische Energiedaten-Darstellung
- **Business Presentation**: Suitable for enterprise und government submissions

## Quality Assurance Standards

### Austrian Energy Sector Compliance
- ✅ **ElWOG 2010 §16a ff**: Vollständige EEG-Gesetzeskonformität
- ✅ **E-Control Standards**: Registrierung, Meldepflichten, Datenformate  
- ✅ **UStG §11 Requirements**: Alle 9 Pflichtangaben business-konform
- ✅ **Smart Meter Integration**: OBIS-Codes, MID-Konformität, DLMS/COSEM
- ✅ **DSGVO Compliance**: Sichere Verarbeitung von Energiedaten
- ✅ **Professional Presentation**: Energy sector business documentation standards
- ✅ **Print Quality**: Perfect A4 formatting für alle Geschäftszwecke

## Technical Implementation Notes

### Smart Meter Data Integration
- **OBIS-Codes**: 1.8.0 (Wirkenergie Bezug), 2.8.0 (Lieferung), 16.7.0 (Momentanleistung)
- **Data Intervals**: 15-Minuten Viertelstundenwerte für Energiemanagement
- **Communication**: DLMS/COSEM Protocol für standardkonforme Datenübertragung
- **Availability**: T+1 (24 Stunden) Abrechnungsdatenbereitstellung durch DSO

### Regulatory Data Requirements
- **E-Control Format**: EEG-AT-YYYY-NNNN-LLL Registrierungsnummern-Standard
- **Austrian IBAN**: AT + 2 Prüfziffern + 5-stellige Bankleitzahl + 11 Kontonummer
- **Tax Compliance**: 20% Regelsteuersatz, reduzierte Sätze wo gesetzlich möglich
- **Documentation**: 7 Jahre Aufbewahrungspflicht nach österreichischer BAO

## Professional Use Case Implementation

### Enterprise EEG Administration
```json
"eeg": {
  "name": "EEG Industrie-Campus Salzburg",
  "rechtsform": "GmbH & Co KG",
  "geschaeftsbereich": "Industrial Energy Community"
}
```

### Municipal Energy Communities
```json
"eeg": {
  "name": "Gemeinde-Energiegemeinschaft Grüntal",
  "rechtsform": "Kommunalbetrieb",
  "konzessionsgebiet": "Salzburg Netz GmbH"
}
```

### Cooperative Energy Models
```json
"eeg": {
  "name": "Energiegenossenschaft Renewable Austria eGen",
  "rechtsform": "Genossenschaft",
  "mitgliederanzahl": 450
}
```

Diese professionelle Vorlage erfüllt höchste österreichische Energiewirtschaftsstandards und ist für reale Geschäftstransaktionen zwischen EEGs, Mitgliedern und Behörden vollständig geeignet.