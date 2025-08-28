# Austrian Invoice Templates - Complete File Structure Guide

*Was macht welche Datei und wie hängt alles zusammen*

---

## 🏗️ Projekt-Übersicht

### **Hauptzweck des Projekts:**
LinkedIn Lead-Funnel für österreichische Rechnungsvorlagen mit Freemium DIY-Ansatz und Premium-Service-Upsells.

---

## 📁 Root-Directory Files

### **🌐 index.html** - Die Hauptseite
**Zweck**: Template-Galerie für LinkedIn-Leads nach AI Audits  
**Inhalt**: 15 Template-Vorschauen + Claude Code DIY Tutorial (als 16. Box)  
**Features**: 
- Professional Banking-Design (basierend auf Erste Bank/Raiffeisen Research)
- iframe Template-Browser für seamless Navigation
- Service-Upsell-Integration zu Libra Innovation FlexCo
- Mobile-responsive, keine Emojis, konservative Ästhetik

### **📖 claude_code_diy_tutorial.html** - DIY-Anleitung  
**Zweck**: Schritt-für-Schritt Tutorial für Selbst-Anpassung
**Inhalt**: 3-Schritte SLC-Prinzip mit konkretem IT-Consultant Beispiel
**Integration**: Lädt im iframe der Hauptseite
**Business**: Freemium-Content mit Service-Upsells am Ende

---

## 📚 Documentation Files

### **📋 CLAUDE.md** - Claude Code Entwickler-Guidelines
**Zweck**: Instruktionen für Claude Code bei der Arbeit am Projekt
**Wichtig**: Definiert Template-Struktur (master vs example), Media-Asset-Workflow
**Enthält**: 
- Template-Struktur (placeholders vs media folders)
- Austrian business context und legal requirements
- Git automation workflows

### **⚖️ TEMPLATEIMAGE_PROMPTS.md** - AI Bildgenerierung
**Zweck**: Prompts für OpenAI gpt-image-1 zur Logo/Icon-Generierung  
**Inhalt**: 15 Template-spezifische Styleguides mit Hex-Farben
**Output**: 720×480px Logos, 512×512px Icons, 480×720px Watermarks

### **🖼️ MEDIA_ASSETS_README.md** - Asset-Spezifikationen  
**Zweck**: Technische Anforderungen für Template-Medien
**Definitionen**: Bildgrößen, Formate, Integration in HTML
**Updated**: Neue hochauflösende Dimensionen (4x Original-Spezifikation)

### **💰 STRATEGIC_VALUE_AMPLIFICATION.md** - Business-Strategie
**Zweck**: Alex Hormozi $100M Framework für Value-Creation
**Inhalt**: €47.000+ Value Stack, Pricing €4.997, Revenue-Modelle €15M+
**Zielgruppe**: Strategic planning für Projekt-Skalierung

### **🎯 LINKEDIN_LEAD_STRATEGY.md** - Marketing-Roadmap
**Zweck**: KISS-Strategie für LinkedIn Lead-Generation
**Timeline**: 90 Tage zu €150.000+ Annual Revenue
**Workflow**: LinkedIn Content → AI Audits → Freemium → Upsells

### **🏦 professional-banking-instructions.md** - Design-Research
**Zweck**: Österreichische Banking-Ästhetik basierend auf Erste Bank/Raiffeisen
**Forschung**: Playwright-basierte Website-Analyse mit Screenshots
**Anwendung**: Konservative Farben, Arial-Font, keine Emojis

---

## 🛠️ image_generation/ Subfolder

### **🤖 generate_template_images.py** - AI Bildgenerierung (500+ Zeilen)
**Zweck**: Generiert professionelle Logos/Icons mit OpenAI gpt-image-1
**Input**: TEMPLATEIMAGE_PROMPTS.md  
**Output**: Nur 4 benötigte Assets (Templates 01, 11, 12, 13)
**Optimiert**: 720×480px Logos, native OpenAI aspect ratios, kein stretching

### **📄 generate_example_pdfs.py** - PDF-Generation (DEAKTIVIERT)
**Zweck**: Playwright-basierte A4 PDF-Erstellung aus HTML
**Status**: Deaktiviert wegen Seitenumbruch-Problemen
**Ersetzt**: Durch iframe-Viewing-System in index.html

### **📸 generate_thumbnails.py** - Screenshot-Generator  
**Zweck**: Professionelle Thumbnails für Template-Galerie
**Output**: 15 Screenshots à 1920×1080px in /templates/screenshots/
**Features**: Top-aligned cropping (Header-Bereiche sichtbar)

### **🏦 research_austrian_banks.py** - Design-Research-Tool
**Zweck**: Playwright-basierte Analyse österreichischer Bank-Websites  
**Output**: professional-banking-instructions.md + Screenshots
**Analysiert**: Erste Bank, Raiffeisen (Bank Austria failed)

### **🧪 test_setup.py** - Setup-Validation
**Zweck**: Überprüft Dependencies, API-Keys, File-Struktur
**Verwendung**: Vor image_generation ausführen

### **📦 requirements.txt** - Python Dependencies
**Inhalt**: OpenAI, Playwright, Pillow, python-dotenv
**Setup**: `pip install -r requirements.txt`

### **🔐 .env** - API-Konfiguration (SENSIBEL)
**Inhalt**: OpenAI API Key + Organization ID  
**Security**: In .gitignore excluded

---

## 📂 templates/ Directory Structure

### **Template-Ordner Aufbau (Beispiel: 01_handwerker_classic/)**

#### **📝 handwerker_classic_masterprompt.md**
**Zweck**: AI-Prompt für Template-Generierung
**Inhalt**: Komplette Anweisungen für AI-Systeme
**Verwendung**: Wenn neue Templates erstellt werden sollen

#### **🎨 handwerker_classic_master.html**  
**Zweck**: Template mit Platzhaltern für AI-Generierung
**Referenzen**: `placeholders/` folder für generische Bilder
**Variablen**: {{firma.name}}, {{kunde.name}}, etc.

#### **📊 handwerker_classic_data.json**
**Zweck**: Mock-Daten Beispiel für Template-Population  
**Inhalt**: Realistische österreichische Firmendaten
**Verwendung**: Zeigt Datenstruktur für AI-Anpassung

#### **📋 handwerker_classic_create.md**
**Zweck**: Anleitung für neue Rechnungs-Erstellung
**Inhalt**: Fill-Up Prompt für echte Kundendaten

#### **🖥️ handwerker_classic_example.html**
**Zweck**: Fertige Beispiel-Rechnung mit Mock-Company-Daten
**Referenzen**: `media/` folder für AI-generierte Firmen-Assets
**Verwendung**: Zeigt Endkunden wie ihr Ergebnis aussehen könnte

### **📁 Unterordner:**

#### **📷 screenshots/**  
**Zweck**: Thumbnails für Template-Galerie
**Inhalt**: 15 Template-Screenshots (1920×1080px → top-aligned)
**Generiert**: Mit generate_thumbnails.py

#### **🖼️ media/ (pro Template)**
**Zweck**: AI-generierte Mock-Company Assets
**Inhalt**: 
- `logo_rectangle.png` (720×480px) - Firmen-Logos
- `icon_square.png` (512×512px) - Business-Icons  
- `watermark.png` (480×720px) - Hintergrund-Wasserzeichen
**Generiert**: Mit generate_template_images.py + gpt-image-1

#### **🔲 placeholders/ (pro Template)**  
**Zweck**: Generische Platzhalter für Master-Templates
**Inhalt**: Standard-Placeholder-Bilder
**Referenz**: Von master.html verwendet

---

## 🔄 Workflow-Integration

### **LinkedIn Lead → Template Delivery:**
1. **LinkedIn Content** → Engagement
2. **AI Audit Buchung** → https://libralab.ai/?utm_source=linkedin  
3. **Post-Audit Follow-up** → Diese Template-Galerie als Wertlieferung
4. **DIY Tutorial** → Selbständige Nutzung möglich
5. **Service Upsells** → €497 - €9.997+ Professional Services

### **Template-Anpassung Workflow:**
1. **Master Template** (placeholders) → AI-Prompt-Generierung für neue Kunden
2. **Example Template** (media assets) → Shows realistic company implementation  
3. **DIY Tutorial** → Kunden können selbst anpassen mit Claude Code
4. **Professional Service** → Libra macht Full-Service-Anpassung

### **Media Asset Pipeline:**
1. **Styleguide Definition** → TEMPLATEIMAGE_PROMPTS.md
2. **AI-Generierung** → generate_template_images.py mit gpt-image-1  
3. **Template Integration** → Automatische Speicherung in media/ folders
4. **Example Implementation** → Zeigt realistic company branding

---

## 🎯 File Dependencies

### **Kritische Abhängigkeiten:**
- **index.html** ← screenshots/, claude_code_diy_tutorial.html
- **generate_template_images.py** ← TEMPLATEIMAGE_PROMPTS.md, .env
- **Templates** ← media/ folders (generated), placeholders/ folders  
- **Screenshots** ← generate_thumbnails.py ← template example.html files

### **Business Flow:**
```
LinkedIn → AI Audit → index.html → DIY Tutorial → Service Upsells
```

### **Technical Flow:**  
```
Prompts → AI Generation → Media Assets → Templates → Gallery → Lead Conversion
```

---

## 📊 Current Project Status

### **✅ Completed Systems:**
- **15 Professional Templates** - UStG §11 konform, branchenspezifisch
- **AI Image Generation** - 4 needed assets mit gpt-image-1 optimiert  
- **Professional Gallery** - Banking-Grade Design, iframe-Navigation
- **DIY Tutorial** - SLC-Prinzip, konkretes IT-Consultant Beispiel
- **Service Integration** - Libra Innovation FlexCo Upsells

### **💰 Business Value:**
- **LinkedIn Authority** - Zeigt AI/Automation-Expertise
- **Lead Qualification** - Trennt DIY von Service-Interessenten  
- **Revenue Streams** - €497 - €9.997+ Service-Pakete
- **Scalable** - Templates beliebig wiederverwendbar

### **🎯 Ready for:**
- LinkedIn Lead-Follow-ups nach AI Audits
- Freemium Template-Distribution  
- Professional Service-Upsells
- Austrian Business Authority Building

**Das komplette System ist ein professioneller LinkedIn Lead-Converter mit österreichischer Banking-Grade-Qualität!**