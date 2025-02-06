# MIDS List of Information Elements

**Title**
: MIDS List of Information Elements

**Date version issued**
: yyyy-mm-dd

**Date created**
: yyyy-mm-dd

**Part of TDWG Standard**
: DRAFT

**This version**
: DRAFT

**Latest version**
: DRAFT

**Abstract**
: Minimum Information about a Digital Specimen (MIDS) is a specification defining the information elements expected to be present when publishing digitised specimen information at various levels of digitisation. Digital Specimens are online digital representations of their physical counterparts in natural science collections. The definition of digitisation used here is the process of making physical objects digitally available. Levels of digitisation represent a simple categorisation of the type and depth of digitisation achieved by different approaches.

This document contains a list of attributes of each MIDS Information Element, including a documentation name, a specified URI, a recommended English label for user interfaces, a definition, and some ancillary notes.

**Contributors**
: Elspeth Haston (https://orcid.org/0000-0001-9144-2848) (Royal Botanic Garden Edinburgh, UK), Cat Chapman (https://orcid.org/0000-0002-0681-2515) (Northern Arizona University & iDigBio, USA), Alex Hardisty (Cardiff University), Wouter Addink (Naturalis, NL), Mathias Dillen (https://orcid.org/0000-0002-3973-1252) (Meise Botanic Garden, BE), (Quentin Groom (Meise Botanic Garden, BE), (Falko Glöckler (Museum für Naturkunde Berlin, DE), Deborah Paul (iDigBio, USA), Mareike Petersen (Museum für Naturkunde Berlin, DE), Hannu Saarenmaa (Bioshare Digitization, FI), (Anton Güntsch - Botanic Garden and Botanical Museum Berlin, DE), Ben Norton, Anke Penzlin (https://orcid.org/0000-0003-2183-893X) (Senckenberg – Leibniz Institution for Biodiversity and Earth System Research) , Claus Weiland (https://orcid.org/0000-0003-0351-6523) (Senckenberg – Leibniz Institution for Biodiversity and Earth System Research), Eirik Rindal (https://orcid.org/0000-0003-1568-6386) (Natural History Museum, University of Oslo), Dagmar Triebel (https://orcid.org/0000-0003-1980-3148) (Bavarian Natural History Collections), Rachel Walcott (https://orcid.org/0000-0002-0488-6393) (National Museums Scotland), Donat Agosti (https://orcid.org/0000-0001-9286-1200) (Plazi), Felipe Simoes (https://orcid.org/0000-0002-1218-2839) (Plazi), Josh Humphries (https://orcid.org/0000-0001-5493-9804) Natural History Museum, London. Alex Hardisty created the foundation for this work.

**Creator**
: TDWG MIDS Task Group

**Bibliographic citation**
: MIDS Task Group. 2025. MIDS List of Information Elements. Biodiversity Information Standards (TDWG). DRAFT


## 1 Introduction

This document contains information elements that are part of the most recent version of the Minimum Information about a Digital Specimen specification.

### 1.1 Status of the content of this document
DRAFT
In Section 5, the Element Name, Element URI, Definition, Required are normative. The status of the SKOS mappings are to be decided. Labels and the values of all other properties (such as Usage, Recommendations and Examples) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.3 Categories of information elements
DRAFT

## 2 Borrowed Vocabulary
MIDS does not borrow terms from other vocabularies, but instead maps to those terms. When terms are mapped, MIDS uses the IRIs, common abbreviations, and namespace prefixes in use in those vocabularies. The IRIs are normative, but abbreviations and namespace prefixes have no impact except as an aid to reading the documentation.

Table 1. Vocabularies from which terms have been borrowed (non-normative)

Note: URIs for terms in most of these namespaces do not dereference to anything.  The authoritative documentation can be obtained by clicking on the vocabulary names in the table.

| Vocabulary                                                     | Abbreviation  | Namespaces and abbreviations                                                   |
|----------------------------------------------------------------|---------------|--------------------------------------------------------------------------------|
| [Darwin Core](https://dwc.tdwg.org/terms/)                     | DwC           | `dwc: = http://rs.tdwg.org/dwc/terms/`                                         |
| [Dublin Core](http://dublincore.org/documents/dcmi-terms/)     | DC            | `dc: = http://purl.org/dc/elements/1.1/, dcterms: = http://purl.org/dc/terms/` |
| [Schema.org](https://schema.org/)                              | Schema        | `schema: =  https://schema.org/version/latest/schemaorg-current-https.rdf`     |
| [Resource Description Framework](https://www.w3.org/RDF/)      | RDF           | `rdf: = http://www.w3.org/1999/02/22-rdf-syntax-ns#`                           |
| [Access to Biological Collection Data](https://abcd.tdwg.org/) | ABCD          | `abcd: = https://abcd.tdwg.org/terms/`                                         |

## 3 Namespaces, Prefixes and Term Names

The namespace of MIDS information elements may be (http://rs.tdwg.org/mids/elements/xxxx) but this is yet to be confirmed. In the table of terms, each information element entry has a row with the information element name. This information element name is generally an “unqualified name” preceded by a widely accepted prefix designating an abbreviation for the namespace. It is RECOMMENDED that implementers who need a namespace prefix for the MIDS namespace use mids. In this web document, hovering over a term in the Index By Information Element Name list below will reveal a complete URL that can be used in other web documents to link to this document’s treatment of that element.

Please note that the names of the information elements are still in draft and have not yet been ratified. They may therefore be subject to change.

***Pending***
