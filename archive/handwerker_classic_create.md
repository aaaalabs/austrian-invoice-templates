# Handwerker Classic - Professional Invoice Creation Instructions

Erstelle eine professionelle Handwerker-Rechnung basierend auf dem Master-Template unter Einhaltung aller österreichischen Gesetzesvorgaben und WKO Tirol Standards für 2025.

## 1. TEMPLATE-BEFÜLLUNG (Professional Standards):

**Grundsätzliche Formatierung:**
- Ersetze alle {{placeholder}} mit den entsprechenden JSON-Werten
- Österreichisches Währungsformat: 1.234,56 € (Punkt als Tausendertrennzeichen, Komma als Dezimaltrennzeichen)
- Datumsformat: TT.MM.JJJJ (österreichischer Standard)
- Professionelle Geschäftssprache verwenden

**Qualitätskontrolle:**
- Alle Elektromaterial-Bezeichnungen müssen fachlich korrekt und spezifisch sein
- Arbeitszeiten nach Qualifikation getrennt ausweisen (Meister vs. Fachkraft)
- Professionelle Terminologie der Elektrotechnik-Branche verwenden

## 2. HANDWERKERBONUS 2025 COMPLIANCE:

**Automatische Berechnungen (Pflichtangaben):**
- **Material-Summe:** Alle Material-Positionen (typ: "material") - NICHT förderfähig
- **Arbeits-Summe:** Alle Arbeit-Positionen (typ: "arbeit") - FÖRDERFÄHIG für Handwerkerbonus
- **Fahrt-Summe:** Alle Fahrt-Positionen (typ: "fahrt") - NICHT förderfähig
- **Handwerkerbonus-Berechnung:** 20% der Arbeitskosten (max. 1.500 € pro Person für 2025)

**Pflicht-Hinweise für Privatrechnungen:**
```
HANDWERKERBONUS 2025 - Steuerliche Absetzbarkeit:
- Förderungsfähige Arbeitskosten (Netto): [X.XXX,XX] €
- Fördersatz: 20% der Arbeitskosten (max. 1.500 € pro Person)
- Ihr Vorteil: bis zu [XXX,XX] € steuerliche Entlastung

Hinweis: Gemäß § 35a EStG können die ausgewiesenen Arbeitskosten als 
Handwerkerleistungen steuerlich geltend gemacht werden. Material- und 
Fahrtkosten sind nicht förderfähig. Förderung nur für Arbeiten an 
privat genutzten Wohnräumen im Inland.
```

## 3. STEUERTECHNISCHE BERECHNUNGEN:

**USt-Sätze 2025 (Österreich):**
- Elektromaterial: 20% (Standardsatz)
- Arbeitsleistungen: 20% (Standardsatz)
- Fahrtkosten: 20% (Standardsatz)

**Berechnungsreihenfolge:**
1. Einzelne Positionsbeträge (Menge × Einzelpreis = Netto)
2. Kategorie-Zwischensummen (Material/Arbeit/Fahrt getrennt)
3. Gesamtsumme Netto
4. USt-Beträge (20% auf alle Positionen)
5. Brutto-Endsumme
6. Skonto-Berechnung (2% bei 14-Tage-Zahlung)
7. Handwerkerbonus-Betrag (20% der Arbeitskosten)

## 4. DATEINAMEN-KONVENTION (Professional):

**Format:** `elektro_rechnung_[rechnungsnummer]_[kundenname]_[JJJJMMTT].html`

**Beispiele:**
- `elektro_rechnung_RE-2025-00287_berger_20250318.html`
- `elektro_rechnung_RE-2025-00288_mueller_gmbh_20250319.html`

## 5. KUNDENSPEZIFISCHE ANPASSUNGEN:

**Privatrechnungen (ohne UID):**
- Handwerkerbonus-Sektion vollständig anzeigen
- Skonto-Angebot (14 Tage 2%)
- Gewährleistungshinweis für Verbrauchsgeschäfte
- Persönliche Ansprache ("Sehr geehrte Familie...")

**B2B-Rechnungen (mit UID):**
- Handwerkerbonus-Sektion ausblenden
- "Zahlung ohne Abzug" statt Skonto
- Firmen-Gewährleistung (§ 924 ABGB)
- Geschäftliche Ansprache ("Sehr geehrte Damen und Herren...")

**EU-Geschäfte (B2B mit EU-UID):**
- Reverse Charge Vermerk
- "Steuerschuldnerschaft des Leistungsempfängers"

## 6. COMPLIANCE-CHECK (§11 UStG 2025):

**Pflichtangaben-Validierung:**
✅ Vollständiger Name und Adresse des leistenden Unternehmers
✅ Name und Adresse des Leistungsempfängers  
✅ Menge und handelsübliche Bezeichnung der Leistungen
✅ Tag der Lieferung/Leistung (Leistungszeitraum)
✅ Entgelt und anzuwendender Steuersatz
✅ Auf das Entgelt entfallender Umsatzsteuerbetrag
✅ Ausstellungsdatum der Rechnung
✅ Fortlaufende Rechnungsnummer
✅ UID-Nummer des Ausstellers

**Elektrotechniker-spezifische Prüfungen:**
✅ Fachgerechte Materialbezeichnungen (Typen, Spezifikationen)
✅ Arbeitszeiten nach Qualifikationsebenen getrennt
✅ WKO Tirol Mitgliedschaftsnachweis
✅ Meisterbetrieb-Status ausgewiesen
✅ Gewährleistungshinweise nach österreichischem Recht

## 7. QUALITÄTSSTANDARDS (Professional Grade):

**Design-Anforderungen:**
- Print-optimiert für A4 schwarzweiß-Druck
- Konservatives, geschäftsmäßiges Layout
- Klare Tabellen-Struktur für einfache Nachvollziehbarkeit
- Professionelle Typografie (Arial/Helvetica)

**Inhaltliche Qualität:**
- Branchenübliche Terminologie der Elektrotechnik
- Realistische Preisgestaltung nach Marktstandards
- Vollständige rechtliche Compliance
- Geschäftsmäßige Professionalität

**Validierung vor Ausgabe:**
- Alle Berechnungen mathematisch korrekt
- Handwerkerbonus-Beträge richtig ermittelt
- Rechtschreibung und Grammatik fehlerfrei
- Layout druckoptimiert und geschäftsmäßig

Diese Vorlage erstellt Rechnungen auf dem Qualitätsniveau etablierter österreichischer Elektrotechniker-Meisterbetriebe und erfüllt alle gesetzlichen sowie branchenspezifischen Anforderungen für 2025.