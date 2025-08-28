# Immobilienverwaltung - Professional Invoice Creation Instructions

## ÜBERSICHT - ÖSTERREICHISCHE IMMOBILIENVERWALTUNG

Verwende das Immobilienverwaltung-Master-Template und befülle es mit professionellen Daten entsprechend höchster Branchenstandards für österreichische Immobilientreuhandunternehmen.

---

## 1. TEMPLATE-INTEGRATION & DATENAUFBEREITUNG

### Platzhalter-Befüllung ({{feldname}} Format):
- **Verwaltungsunternehmen**: Vollständige Firmenbezeichnung mit "GmbH" oder entsprechender Rechtsform
- **Konzessionsdaten**: "Immobilientreuhänder-Berechtigung Nr. IT-YYYY-XXXX" (nicht "Makler")  
- **ÖVI/WKO Status**: Mitgliedschaftsangaben für Branchenvertrauenswürdigkeit
- **Objekt-Identifikation**: Eindeutige Bezeichnung, Kataster-/EZ-Nummer, WEG-Registernummer
- **Vertragsreferenzen**: Verwaltungsvertrags-Nr., WEG-Beschluss-Referenzen

### Österreichische Währungsformatierung:
- **Standard**: 1.234,56 € (Punkt als Tausender, Komma als Dezimal)
- **Große Beträge**: 12.345,67 € (nicht amerikanisches Format)
- **Tabellen**: Rechtsbündig, einheitliche Dezimalstellen
- **Zusammenfassungen**: Fettschrift für Endsummen

---

## 2. BRANCHENSPEZIFISCHE BERECHNUNGSLOGIK

### Verwaltungsgebühren-Kategorien (2025 Standards):
1. **Hausverwaltung**: 20-40 €/WE/Monat bei 20+ Einheiten (pauschal, nicht umlagefähig)
2. **Betriebskosten**: Heizung, Strom, Wasser, Reinigung, Hausbetreuung (umlagefähig)
3. **Instandhaltung**: Wartungen, Reparaturen, Sanierungen (je nach Art umlagefähig)
4. **Sonderverwaltung**: Eigentümerversammlungen, Projektmanagement (nicht umlagefähig)
5. **Mietmanagement**: 3-5% der Bruttomieteinnahmen (nicht umlagefähig)

### Steuerbehandlung:
- **Regelfall**: 20% USt auf alle Verwaltungsleistungen
- **Kleinunternehmer**: Nur bei Verwaltung unter Kleinunternehmergrenze (€55.000 seit 2025)
- **Reverse Charge**: Bei ausländischen Eigentümergemeinschaften (EU B2B)

### Rücklagen-Management:
- **Erhaltungsrücklage**: Mindestens 0,5% des Gebäudewerts p.a.
- **Verbesserungsrücklage**: Für Modernisierungen und Wertsteigerungen
- **Zuführung/Entnahmen**: Transparent dokumentiert mit WEG-Beschluss-Referenzen

---

## 3. PROFESSIONELLE DATEIBEZEICHNUNG

### Format für Verwaltungsabrechnungen:
```
verwaltung_[objektkuerzel]_[rechnungsnummer]_[periode]_[datum].html
```

### Beispiele:
- `verwaltung_alpenpanorama_VWA-2025-03456_Q2-2025_20250828.html`
- `verwaltung_stadtpark_VWA-2025-03457_jahr-2024_20250131.html`
- `verwaltung_sonnenhof_VWA-2025-03458_Q1-2025_20250331.html`

### Archivierungs-Standards:
- **22-Jahres-Aufbewahrung**: Immobilienrecht-konforme Benennung
- **Sortierbar**: Datum und Periode maschinell erkennbar
- **Eindeutig**: Objektbezug und Abrechnungsart klar ersichtlich

---

## 4. IMMOBILIEN-RECHTLICHE TEXTBAUSTEINE

### Objekt-Identifikation (prominent im Header):
```
Verwaltungsobjekt: [Vollbezeichnung]
Adresse: [Straße, PLZ Ort]
Kataster: KG [Gemeinde], EZ [Einlagezahl]
WEG-Register: WEG-[Ort]-[Jahr]-[Nummer]
Verwaltungsvertrag: VV-[Jahr]-[Nummer] vom [Datum]
```

### Abrechnungsperioden (branchenspezifisch):
- **Quartalsabrechnungen**: Standard für laufende Betriebskosten
- **Jahresabrechnungen**: Vollabrechnung bis 30. Juni des Folgejahres  
- **Sondermassnahmen**: Mit WEG-Beschluss-Referenz und Datum
- **Vorauszahlungen**: Anpassungen dokumentiert und begründet

### Umlagefähigkeits-Kennzeichnung:
- **Umlagefähig**: "Betrag wird gemäß WEG auf Eigentümer umgelegt"
- **Nicht umlagefähig**: "Verwaltungsleistung, Belastung der WEG direkt"
- **Umlageschlüssel**: "Nach Nutzwert/Wohnfläche/Eigentumsanteilen"

---

## 5. CORPORATE DESIGN & VERTRAUENSBILDUNG

### Professional Excellence Standards:
- **Konservativer Stil**: Vertrauen für langfristige Vermögensverwaltung
- **Klare Hierarchie**: Objektdaten → Leistungen → Zusammenfassung → Rechtliches
- **Businesstauglich**: Eigentümerversammlungen, Banken, Behörden akzeptieren Format
- **Print-Optimiert**: Perfekte A4-Darstellung für 22-jährige Archivierung

### Vertrauensbildende Elemente (sichtbar platziert):
- **Konzessions-Nr.**: Immobilientreuhänder-Berechtigung prominent
- **Berufshaftpflicht**: Versicherungsnachweis mit Police-Nummer  
- **Verbandsmitgliedschaft**: ÖVI-Status, WKO Fachgruppe
- **Treuhandkonto**: Separate IBAN für Kautionsverwaltung sichtbar

---

## 6. ÖSTERREICHISCHE COMPLIANCE-VALIDIERUNG

### UStG §11 Pflichtangaben (vollständig prüfen):
1. **Leistungserbringer**: Firmenname, Adresse, UID, Konzessionsnummer
2. **Leistungsempfänger**: WEG-Name, Verwaltungsbeirat, Adresse, UID  
3. **Objektidentifikation**: Eindeutige Immobilienbezeichnung mit Katasterdaten
4. **Leistungsbeschreibung**: Detaillierte Verwaltungstätigkeiten mit Zeitbezug
5. **Leistungszeitraum**: Exakte Periode (von/bis Datum)
6. **Mengen/Einheiten**: Anzahl WE, Stunden, Prozentsätze der Berechnungsgrundlagen
7. **Entgeltangaben**: Nettobetrag je Position
8. **Steuersatz**: 20% USt (Standard für Verwaltungsleistungen)
9. **Steuerbeträge**: USt-Betrag je Position und Gesamtsumme
10. **Rechnungsdatum**: Aktuelles Ausstellungsdatum
11. **Rechnungsnummer**: Fortlaufend, VWA-Format (Verwaltungsabrechnung)

### Zusätzliche Immobilien-Compliance:
- **ITG-Konformität**: Immobilientreuhandgesetz-konforme Geschäftsführung
- **WEG-Rechtsmäßigkeit**: Wohnungseigentumsgesetz-konforme Abrechnung
- **DSGVO**: Datenschutzkonforme Verarbeitung von Mieter-/Eigentümerdaten
- **Kautions-Handling**: 0,125% p.a. Verzinsung (OeNB Basiszinssatz)

---

## 7. ERWEITERTE IMMOBILIEN-SPEZIFIKA

### Rechtliche Hinweise (Footer-Integration):
```
AUFBEWAHRUNGSPFLICHT: 22 Jahre (Immobilienrecht)
RECHTSGRUNDLAGEN: ITG, WEG, MaklerG, UStG §11, DSGVO
EINSPRUCHSFRIST: 30 Tage ab Rechnungsdatum
ZUSTÄNDIGKEIT: [Name], gepr. Immobilientreuhänder
```

### Zahlungskonditionen (Branchenstandard):
- **Zahlungsziel**: 30 Tage netto (nicht 14 wie andere Branchen)
- **Skonto**: Optional 2% bei 14 Tagen (unüblich in Verwaltung)
- **Mahngebühren**: €15 pro Mahnstufe (moderate Ansätze)  
- **Verzugszinsen**: 4% p.a. über Basiszinssatz OeNB

### E-Rechnung 2025 Vorbereitung:
- **Strukturierte Daten**: Maschinenlesbare Formate vorbereitet
- **EU-Standard**: PEPPOL-konforme Metadaten integriert
- **Archivierung**: DSGVO-konforme elektronische Langzeitarchivierung

---

## 8. QUALITÄTSSICHERUNG & PROFESSIONAL STANDARDS

### Business-Akzeptanz Checkpoints:
- ✅ **Eigentümerversammlung**: Vorlage für WEG-Beschlüsse geeignet
- ✅ **Steuerberatung**: Vollständige USt-Abzugsfähigkeit gewährleistet
- ✅ **Banking**: Finanzierungsunterlagen-kompatibel
- ✅ **Behörden**: Finanzamt, BH-Vorlagen akzeptiert
- ✅ **Archivierung**: 22-Jahres-Lesbarkeit sichergestellt

### Print-Performance Standards:
- ✅ **A4-Perfektion**: Keine Seitenumbrüche mitten in Tabellen
- ✅ **S/W-Tauglich**: Alle Informationen auch ohne Farbe lesbar
- ✅ **Schriftgrößen**: Mindestens 10pt für rechtssichere Archivierung
- ✅ **Contrast**: Hoher Kontrast für 22-jährige Lesbarkeit

### Branchenspezifische Validierung:
- ✅ **Terminology**: Ausschließlich Branchenterminologie (kein Laien-Deutsch)
- ✅ **Legal References**: Korrekte Gesetzes- und Verordnungsverweise
- ✅ **Professional Layout**: Ununterscheidbar von etablierten Verwaltungsunternehmen
- ✅ **Cost Structure**: Realistische Gebührenstrukturen für 2025

---

## 9. FINALE IMPLEMENTATION-CHECKLISTE

### Pre-Generation Check:
1. **JSON-Validation**: Alle Pflichtfelder der Immobilienverwaltung befüllt
2. **Legal Compliance**: ITG-, WEG-, UStG-Konformität sichergestellt  
3. **Professional Standards**: ÖVI-/WKO-Standards eingehalten
4. **Print Readiness**: A4-Formatierung, S/W-Kompatibilität geprüft

### Post-Generation Check:  
1. **Visual Inspection**: Professionelle Optik, keine Formatierungsfehler
2. **Content Accuracy**: Alle Berechnungen, Steuersätze, Fristen korrekt
3. **Legal Completeness**: Alle UStG §11 Pflichtangaben vorhanden
4. **Business Suitability**: Suitable für reale Geschäftstätigkeit

**ZIEL**: Generiere eine Verwaltungsabrechnung, die von einem etablierten österreichischen Immobilientreuhandunternehmen stammen könnte und alle rechtlichen, steuerlichen und branchenprofessionellen Standards erfüllt.