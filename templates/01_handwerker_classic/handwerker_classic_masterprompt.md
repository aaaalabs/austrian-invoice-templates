# Handwerker Classic - Tiroler Tradition - Master Template Prompt

Erstelle eine professionelle HTML-Rechnungsvorlage für einen österreichischen Elektrotechniker-Meisterbetrieb mit folgenden industry-spezifischen Anforderungen basierend auf WKO Tirol Standards und konservativem Geschäftsdokument-Design:

## INDUSTRIE-RESEARCH GRUNDLAGEN:
Basierend auf Analyse professioneller österreichischer Elektroinstallations-Rechnungen von WKO Tirol Mitgliedsbetrieben:
- Konservatives, druckoptimiertes Design ohne dekorative Elemente
- Klare Trennung von Material-, Arbeits- und Fahrtkosten für steuerliche Zwecke
- Professional Business-Korrespondenz-Stil der deutschsprachigen Länder
- Handwerkerbonus-konforme Aufschlüsselung für Privatkundenabsetzbarkeit

## DESIGN SPEZIFIKATIONEN:
**Print-Ready Professional Standards:**
- Klassisches A4-Format (210x297mm) mit 20mm Rändern
- Konservative Farbpalette: Dunkelblau (#003366) und Grautöne
- Schwarzweiß-Druckoptimierung mit hohem Kontrast
- KEINE dekorativen Elemente, Emojis oder Grafiken
- Professionelle Typografie: Arial/Helvetica für Klarheit
- Firmenlogo rechtsbündig (150x60px, druckoptimiert)
- KEIN Wasserzeichen (beeinträchtigt Druckqualität)

## STRUKTUR NACH WKO ELEKTROTECHNIKER-STANDARDS:

**Firmenkopf (Conservative Header):**
- Meisterbetrieb-Status prominent
- Vollständige österreichische Geschäftsadresse
- Kontaktdaten (Telefon, E-Mail, Website)
- UID-Nummer und Firmenbuch-Eintrag

**Rechnungsbereich (Professional Layout):**
- Strukturierte Kundendaten links
- Rechnungsmetadaten rechtsbündig
- Betreff: Spezifikation der Elektroarbeiten

## PFLICHTFELDER gemäß §11 UStG (2025):
1. **Firmendaten:** Vollständiger Name und Adresse des leistenden Unternehmers
2. **Kundendaten:** Name und Adresse des Leistungsempfängers
3. **Rechnungsnummer:** Fortlaufend Format: RE-2025-XXXXX
4. **Rechnungsdatum:** Österreichisches Format (TT.MM.JJJJ)
5. **Leistungszeitraum:** Von/bis Datumsangaben
6. **UID-Nummer:** ATU12345678 Format
7. **Leistungsbeschreibung:** Detailliert und spezifisch
8. **Entgelt:** Nach Steuersätzen aufgeschlüsselt
9. **Steuersatz und -betrag:** Korrekte österreichische USt-Sätze

## MATERIAL-ARBEIT-FAHRT TRENNUNG (Handwerkerbonus-konform):

**Kostenkategorien-Tabelle:**
```
Kategorie | Beschreibung | Menge | Einheit | Einzelpreis | USt% | Netto | USt | Brutto
Material  | [Konkrete Elektromaterialien] | X | Stk/m | XX,XX € | 20% | XX,XX € | XX,XX € | XX,XX €
Arbeit    | [Detaillierte Arbeitsleistung] | X | Std | XX,XX € | 20% | XX,XX € | XX,XX € | XX,XX €
Fahrt     | [Fahrtkosten/Pauschalen] | X | Fahrt | XX,XX € | 20% | XX,XX € | XX,XX € | XX,XX €
```

**Wichtige Trennung für steuerliche Zwecke:**
- Material: Separate Auflistung aller Elektrokomponenten
- Arbeitszeit: Meister-/Gesellen-Stunden getrennt ausweisen
- Fahrtkosten: Pauschalen oder kilometergenaue Abrechnung

## HANDWERKERBONUS 2025 COMPLIANCE:

**Gesetzliche Grundlage:**
- Nur reine Arbeitskosten (ohne Fahrt und Material) förderfähig
- 20% der förderungsfähigen Nettokosten (ohne USt)
- Maximum 1.500 € pro Person für 2025
- Arbeiten an privat genutzten Wohnräumen im Inland

**Pflicht-Hinweise auf Rechnung:**
```
HANDWERKERBONUS 2025:
Die ausgewiesenen Arbeitskosten (Netto: XXX,XX €) sind gem. § 35a EStG als 
Handwerkerleistungen steuerlich absetzbar. Förderfähig sind 20% der Arbeitskosten 
(max. 1.500 € pro Person). Material- und Fahrtkosten sind nicht förderfähig.
```

## GEWÄHRLEISTUNG & RECHTLICHES:

**Standardformulierung:**
```
GEWÄHRLEISTUNG:
Gemäß österreichischem Recht gewähren wir 2 Jahre Gewährleistung auf unsere 
Elektroinstallations-Leistungen (§ 924 ABGB). Bei Verbrauchsgeschäften gelten 
die Bestimmungen des Konsumentenschutzgesetzes.
```

## ZAHLUNGSKONDITIONEN (Branchenüblich):
- Zahlungsziel: 30 Tage netto (gesetzlicher Standard)
- Skonto: 14 Tage 2% Skonto (branchenüblich)
- Bankverbindung: Österreichische IBAN (AT XX XXXX XXXX XXXX XXXX)
- SEPA-Lastschrift-Hinweis bei Vereinbarung

## WKO TIROL FOOTER (Pflichtangaben Meisterbetrieb):
```
[Firmenname] | Geschäftsführer: [Name] | UID: ATU12345678
Firmenbuch: FN 123456a (Landesgericht Innsbruck)
Mitglied der WKO Tirol - Landesinnung der Elektrotechniker
Geprüfter Meisterbetrieb - Qualität durch Kompetenz
```

## QUALITÄTSSTANDARDS:
- **Professional Grade:** Ununterscheidbar von etablierten Elektrobetrieben
- **Druckqualität:** Perfekte A4-Formatierung, schwarzweiß-optimiert
- **Geschäftsglaubwürdigkeit:** Geeignet für Unternehmens- und Behördenkunden
- **Branchenkonformität:** Entspricht WKO Elektrotechniker-Standards
- **Rechtskonformität:** 100% österreichische UStG §11 Compliance

## TEMPLATE-STRUKTUR:
Verwende semantische Platzhalter im Format {{kategorie.feldname}} für:
- {{firma.*}} - Alle Unternehmensdaten
- {{kunde.*}} - Kundenstammdaten
- {{rechnung.*}} - Rechnungsmetadaten
- {{positionen[]}} - Array der Rechnungspositionen mit Typ-Kennzeichnung
- {{zusammenfassung.*}} - Berechnete Summen nach Kategorien
- {{zusatzinfo.*}} - Handwerkerbonus, Gewährleistung, WKO-Mitgliedschaft

Diese Vorlage muss die Anforderungen eines konservativen österreichischen Elektrotechniker-Meisterbetriebs erfüllen und sowohl für Privat- als auch B2B-Kunden professionell wirken.