# Energiegemeinschaft NEU Template - Creation Guide

## Template Beschreibung
Moderne Rechnungsvorlage für österreichische Erneuerbare-Energie-Gemeinschaften (EEG) nach ElWOG 2010, optimiert für nachhaltige Community-Energieversorgung mit Smart Metering Integration.

## Zielgruppe
- Erneuerbare-Energie-Gemeinschaften (EEG)
- Bürgerenergiegemeinschaften
- Regionale Energieversorger
- Community Energy Projekte
- Prosumer-Gemeinschaften

## Kernfeatures

### 🌱 Nachhaltiges Design
- Grünes Farbschema mit natürlichen Elementen
- Community-orientierte Visualisierung
- Organische Formen und Eco-Symbole
- 100% Erneuerbar Zertifikat-Badge

### ⚡ EEG-Spezifische Abrechnungslogik
- Gemeinschaftsenergie vs. Netzbezug Aufschlüsselung
- Eigenverbrauchsquote und lokale Wertschöpfung
- Dynamische Tarife nach Community-Modell
- Transparente Kostenverteilung

### 📊 Smart Metering Integration
- OBIS-Codes und Zählpunkt-IDs
- Echtzeitdaten-Verlinkung
- QR-Codes für Portal-Zugang
- Mobile App Integration

### 🏛️ Rechtskonforme EEG-Abrechnung
- ElWOG 2010 §16a ff konform
- E-Control Registrierungsnummern
- DSGVO-konforme Datenverarbeitung
- Transparente Mitgliederrechte

## JSON-Struktur Highlights

### EEG-Spezifische Felder
```json
{
  "eeg": {
    "registrierung": "EEG-2024-AT-0158",
    "e_control_reg": "EEG-AT-2024-0158-TIR"
  },
  "mitglied": {
    "mitgliedsnummer": "EEG-ALT-2024-0089",
    "kategorie": "Verbraucher|Erzeuger|Prosumer",
    "zahlpunkt_id": "AT003300000000000000123456789012"
  },
  "energiedaten": {
    "eigenverbrauchsquote_prozent": 73.6,
    "gemeinschaftsrabatt_prozent": 25.4,
    "co2_vermieden_kg": 142
  }
}
```

### Community-Transparenz
- Gesamterzeugung und -verbrauch der Gemeinschaft
- Selbstversorgungsgrad in Prozent
- CO2-Vermeidung durch lokale Erzeugung
- Regionale Wertschöpfung in Euro

## Rechtliche Besonderheiten

### ElWOG-Konformität
- Energiegemeinschaften nach §16a ElWOG 2010
- E-Control Registrierung erforderlich
- Transparente Abrechnungsmodalitäten
- Mitgliederrechte und -pflichten

### Steuerliche Behandlung
- Umsatzsteuerpflicht auf Gemeinschaftsenergie
- 20% USt auf alle Energielieferungen
- Korrekte Ausweisung Netz- vs. Community-Bezug

### Datenschutz
- Smart Meter Daten DSGVO-konform
- Einverständniserklärung für Datennutzung
- Transparente Datenverarbeitung

## Design-Elemente

### Farbschema
- **Primär**: Waldgrün (#2D5A32) - Nachhaltigkeit
- **Sekundär**: Energiegelb (#E6B800) - Solarenergie  
- **Akzent**: Wasserblau (#1976D2) - Wasserkraft
- **Basis**: Naturweiß (#FAFAFA) - Reinheit

### Typografie
- **Headers**: Inter Bold - Modern und lesbar
- **Body**: Source Sans Pro - Gut lesbar
- **Data**: Roboto Mono - Präzise Zahlen

### Icons & Symbole
- Erneuerbare-Energie-Symbole (Solar, Wind, Wasser)
- Community-Ikonen (Verbindungen, Sharing)
- Nachhaltigkeits-Badges (CO2, Recycling)
- Smart-Grid Visualisierungen

## Use Cases

### 1. Bürgerenergiegemeinschaft
```json
"eeg": {
  "name": "BEG Sonnendorf",
  "kategorie": "Bürgenenergiegemeinschaft"
}
```

### 2. Regionale EEG
```json
"eeg": {
  "name": "Energieregion Alpental",
  "kategorie": "Regionale Energiegemeinschaft"
}
```

### 3. Genossenschaftsmodell
```json
"eeg": {
  "name": "Energie-Genossenschaft eG",
  "rechtsform": "Genossenschaft"
}
```

## Smart Features

### QR-Code Integration
- EPC-Payment für SEPA-Lastschrift
- Portal-Login für Mitgliederbereich
- App-Download Links
- Community-Dashboard Zugang

### Mobile-First Design
- Responsive Layout für alle Geräte
- Touch-optimierte Elemente
- Schnelle Ladezeiten
- Progressive Web App Kompatibilität

### Community-Services
- Energieberatung Terminbuchung
- Mitgliederversammlung Reminder
- Newsletter-Anmeldung
- Social Community Links

## Compliance Checklist

- ✅ ElWOG 2010 §16a ff konform
- ✅ UStG Pflichtangaben vollständig
- ✅ E-Control Registrierung ausgewiesen
- ✅ Smart Meter OBIS-Codes korrekt
- ✅ DSGVO-konforme Datenverarbeitung
- ✅ Transparente Preisaufschlüsselung
- ✅ Community-Impact dokumentiert

## Performance Metrics

### Nachhaltigkeit
- CO2-Einsparung pro Mitglied/Monat
- Eigenverbrauchsquote der Gemeinschaft
- Anteil erneuerbarer Energien
- Regionale Wertschöpfung

### Community
- Mitgliederzufriedenheit
- Portal-Nutzung und App-Downloads
- Teilnahme an Veranstaltungen
- Weiterempfehlungsrate

Diese Vorlage unterstützt die österreichische Energiewende durch transparente, rechtskonforme und community-orientierte Abrechnungsgestaltung für Erneuerbare-Energie-Gemeinschaften.