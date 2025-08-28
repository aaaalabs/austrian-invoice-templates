# Template 5: B2B Reverse Charge EU - Enhanced Creation Instructions

## Professional Invoice Generation with Strict Compliance Validation

Generate a legally compliant Reverse Charge invoice meeting Austrian UStG requirements and EU VAT Directive standards:

### 1. MANDATORY REVERSE CHARGE VALIDATION:

**Pre-Generation Compliance Checks:**
- ✅ **B2B Status**: Both supplier and customer must have valid VAT IDs
- ✅ **Cross-Border**: Service provider and recipient in different EU countries
- ✅ **Service Nature**: Must be consultation/advisory services (not goods)
- ✅ **Place of Supply**: Determined by §3a UStG recipient location principle
- ❌ **FAIL CONDITIONS**: Generate ERROR message if any check fails

**Validation Protocol:**
```
IF (supplier_country != customer_country) 
   AND (supplier_UID_valid == true) 
   AND (customer_VAT_ID_valid == true) 
   AND (service_type == "consultation" OR "advisory")
THEN apply_reverse_charge = true
ELSE generate_compliance_error
```

### 2. AUSTRIAN LEGAL COMPLIANCE (UStG):

**Mandatory Legal References:**
- **§19 Abs. 1 UStG**: "Steuerschuldnerschaft des Leistungsempfängers"
- **§3a Abs. 6 UStG**: Place of supply determination (recipient location)
- **Art. 196 MwStSystRL**: EU VAT Directive reference
- **Zero VAT Display**: No Austrian VAT charged, explicit Reverse Charge note

**Legal Notice Requirements:**
- German: "Steuerschuldnerschaft des Leistungsempfängers gem. § 19 Abs. 1 UStG"
- English: "Reverse charge - VAT to be paid by recipient according to Art. 196 VAT Directive"

### 3. PROFESSIONAL BUSINESS PRESENTATION:

**Invoice Format Standards:**
- **Sequential Numbering**: EU-YYYY-NNNNN format for international identification
- **Professional Layout**: Conservative business document design
- **Bilingual Content**: German primary, English secondary for international clients
- **Service Description**: Detailed, professional consulting terminology
- **Print Quality**: Black/white compatible for archival requirements

**Service Documentation:**
- Clear project phases and deliverables
- Professional daily rates (€1,200-€1,600 typical for Austrian consulting)
- Separate itemization of travel expenses and materials
- Realistic time allocations and project structure

### 4. VIES VALIDATION DOCUMENTATION:

**Required VIES Check Elements:**
- **Validation Timestamp**: Exact date and time of VIES query
- **VAT ID Verification**: Customer VAT ID confirmed as valid
- **Status Documentation**: "Valid" status with reference date
- **Archive Reference**: Compliance document reference number

**Example Format:**
```
VIES validation performed 28.08.2025 10:34 CET - Status: Valid (DE234567890)
Compliance documentation archived under reference EU-2025-00142-COMP
```

### 5. PLACE OF SUPPLY DETERMINATION:

**§3a UStG Implementation:**
- **Recipient Location Principle**: Service performed where customer is established
- **Legal Explanation**: Clear reference to §3a Abs. 6 UStG
- **Practical Impact**: Determines tax obligation location
- **Documentation**: Both German and English explanation required

**Template Language:**
- DE: "Der Ort der sonstigen Leistung bestimmt sich nach §3a Abs. 6 UStG nach dem Empfängerortprinzip"
- EN: "Place of supply determined according to §3a para. 6 UStG based on recipient location principle"

### 6. BANKING AND PAYMENT COMPLIANCE:

**SEPA Payment Requirements:**
- **Austrian IBAN**: Standard AT format with valid check digits
- **BIC Code**: Correct Austrian bank identifier
- **Payment Reference**: Invoice number as mandatory reference
- **Payment Terms**: 30 days standard for B2B transactions

**International Banking:**
- Same Austrian account for SEPA and international transfers
- Clear currency specification (EUR only)
- Professional bank relationship documentation

### 7. QUALITY ASSURANCE CHECKLIST:

**Pre-Delivery Validation:**
- [ ] All mandatory UStG §11 invoice elements present
- [ ] Reverse Charge legal notices in German and English
- [ ] VIES validation documented with timestamp
- [ ] Place of supply correctly determined and explained
- [ ] Professional service descriptions with bilingual content
- [ ] Correct Austrian business registration details
- [ ] Zero VAT amount with explicit Reverse Charge indication
- [ ] Proper sequential invoice numbering (EU prefix)
- [ ] Compliance documentation archived with reference

### 8. FILE NAMING AND ARCHIVAL:

**Naming Convention:**
```
Format: invoice_EU_[NUMBER]_[CUSTOMER_COUNTRY]_[YYYYMMDD].html
Example: invoice_EU_EU-2025-00142_DE_20250828.html
```

**Archival Requirements:**
- 7-year retention period (Austrian law)
- Compliance documentation package
- VIES validation screenshot/reference
- Service delivery confirmation documents

### 9. ERROR HANDLING AND WARNINGS:

**Critical Errors (Generation Stops):**
- Invalid or missing VAT IDs
- Same country supplier and customer
- Goods delivery instead of services
- Missing legal compliance elements

**Warnings (Generation Continues):**
- Unusual service rates or quantities
- Missing travel expense documentation
- Incomplete project phase descriptions
- Non-standard payment terms

### 10. PROFESSIONAL STANDARDS VALIDATION:

**Business Credibility Requirements:**
- Services must reflect realistic Austrian consulting practices
- Professional terminology and industry-standard rates
- Logical project structure and timeline
- Appropriate Austrian business registration format
- Conservative, authoritative document presentation

**Final Quality Check:**
- Invoice suitable for submission to tax authorities
- Professional presentation matching established consulting firms
- Complete legal compliance for Austrian and EU requirements
- Print-ready format for physical archival storage