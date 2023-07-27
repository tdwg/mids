
<p style="font-size:24px;font-weight:700">
Version history
</p>

| Version | Date | Author(s) | Changes |
| --- | --- | --- | --- |
| v0.17 | 13-Jul-2023 | Elspeth Haston, Cat Chapman, Alex R Hardisty, Wouter Addink, Mathias Dillen, Falko Glöckler, Quentin Groom, Deborah Paul, Mareike Petersen, Hannu Saarenmaa, Anton Güntsch, Ben Norton, Anke Penzlin, Claus Weiland, Eirik Rindal, Dagmar Triebel, Rachel Walcott | updated from v0.16 (22-Jun-2022) |
|  |  |  |  |

<!--  Title page. -->
<div style="page-break-before: always">
<p style="font-size:24px;font-weight:700">
Title: Minimum Information about a Digital Specimen (MIDS) - MIDS-1
</p>
</div>

Date version issued: _2023-07-13_

Date created: 2022-06-01

This version: _V0.17_

Abstract: Minimum Information about a Digital Specimen (MIDS) is a specification defining the information elements expected to be present when publishing digitised specimen information at various levels of digitisation. Digital Specimens are online digital representations of their physical counterparts in natural science collections. The definition of digitisation used here is the process of making physical objects digitally available. Levels of digitisation represent a simple categorisation of the type and depth of digitisation achieved by different approaches.

Contributors: Elspeth Haston, Cat Chapman, Alex R Hardisty, Wouter Addink, Mathias Dillen, Falko Glöckler, Quentin Groom, Deborah Paul, Mareike Petersen, Hannu Saarenmaa, Anton Güntsch, Ben Norton, Anke Penzlin, Claus Weiland, Eirik Rindal, Dagmar Triebel [to be completed and confirmed]

Creator: _&lt;to be completed>_

Bibliographic citation: _&lt;to be completed>_

Change history: &lt;_to be completed. begins with version 1.0_>

<!--  End of title page. -->

<!--  Table of contents -->
<div style="page-break-before: always">
<p style="color:blue;font-size:18px;font-weight:700">
Table of contents
</p>
</div>

- [1 Introduction](#1-introduction)
  - [1.1 Audience](#11-audience)
  - [1.2 RFC 2119 key words](#12-rfc-2119-key-words)
  - [1.3 Content](#13-content)
  - [1.4 Definitions](#14-definitions)
  - [1.5 Acknowledgements](#15-acknowledgements)
- [2 Background (informative)](#2-background-informative)
  - [2.1 Processes of digitization (informative)](#21-processes-of-digitization-informative)
  - [2.2 Stages of digitization (informative)](#22-stages-of-digitization-informative)
  - [2.3 Harmonising the approach (informative)](#23-harmonising-the-approach-informative)
  - [2.4 Accommodating variability in details of the process (informative)](#24-accommodating-variability-in-details-of-the-process-informative)
- [3 Principles of MIDS levels of digitization (normative)](#3-principles-of-mids-levels-of-digitization-normative)
  - [3.1 Authoritative data and variations in digitization](#31-authoritative-data-and-variations-in-digitization)
  - [3.2 Other data present or known about a specimen](#32-other-data-present-or-known-about-a-specimen)
  - [3.3 Prior to digitization](#33-prior-to-digitization)
  - [3.4 Assigning persistent identifiers to digitized specimen data](#34-assigning-persistent-identifiers-to-digitized-specimen-data)
  - [3.5 MIDS levels of minimum information](#35-mids-levels-of-minimum-information)
  - [3.6 Information elements expected and expansion beyond the minimum](#36-information-elements-expected-and-expansion-beyond-the-minimum)
- [4 Information content and element mappings for each MIDS level (normative)](#4-information-content-and-element-mappings-for-each-mids-level-normative)
  - [4.1 Information elements expected at MIDS level 1](#41-information-elements-expected-at-mids-level-1)
  - [4.2 Information elements expected at MIDS level 2](#42-information-elements-expected-at-mids-level-2)
  - [4.3 Information elements expected at MIDS level 3](#43-information-elements-expected-at-mids-level-3)
  - [4.4 Information elements expected at MIDS level 0](#44-information-elements-expected-at-mids-level-0)
  - [4.5 Information element definitions](#45-information-element-definitions)
    - [4.6.1 MIDS element - Modified](#461-mids-element---modified)
    - [4.6.2 MIDS element - MIDSLevel](#462-mids-element---midslevel)
    - [4.6.3 MIDS element - PhysicalSpecimenId](#463-mids-element---physicalspecimenid)
    - [4.6.4 MIDS element - Institution](#464-mids-element---institution)
    - [4.6.5 MIDS element - ObjectType](#465-mids-element---objecttype)
    - [4.6.6 MIDS element - MaterialType](#466-mids-element---materialtype)
    - [4.6.7 MIDS element - PreparationType](#467-mids-element---preparationtype)
    - [4.6.8 MIDS element - Name](#468-mids-element---name)
  - [4.5 Handling of unknown and incomplete data](#45-handling-of-unknown-and-incomplete-data)
    - [4.5.1 Unknown datetime in CreatedON/ModifiedON information elements](#451-unknown-datetime-in-createdonmodifiedon-information-elements)
    - [4.5.2 Geographical data information elements](#452-geographical-data-information-elements)
    - [4.5.3 Unknown values for other information elements](#453-unknown-values-for-other-information-elements)
- [5 Images and other media types (normative)](#5-images-and-other-media-types-normative)
- [6 Guidelines for machine-actionability (normative)](#6-guidelines-for-machine-actionability-normative)
- [7 Recommendations for collection-holding institutions](#7-recommendations-for-collection-holding-institutions)
- [8 Guarding against publication of junk data](#8-guarding-against-publication-of-junk-data)
- [9 Conformance (normative)](#9-conformance-normative)
  - [9.1 Principle means of conformance](#91-principle-means-of-conformance)
  - [9.2 Implementation Conformance Statement (ICS)](#92-implementation-conformance-statement-ics)
- [10 Illustrative use cases and guidelines for use (informative)](#10-illustrative-use-cases-and-guidelines-for-use-informative)
- [11 References](#11-references)

<!--  Main text begins. -->
# 1 Introduction

Minimum Information about a Digital Specimen (MIDS) specifies the information elements expected to be present when providing access to specimens within a digital framework. Digital Specimens are online digital representations of their physical counterparts in natural science collections. The definition of digitisation used here is the process of making physical objects digitally available in terms of data and/or images. Several 'levels of digitisation' (0-3) represent a simple categorisation of the type and depth of digitisation achieved by heterogeneous approaches to digitisation. This document currently defines and describes MIDS Levels 0, 1 and 2. Level 3 will be included in a future version of the specification.

MIDS has multiple aims:

1. To assist the global effort to digitise natural science collections, estimated to be between 1.2 and 2.1 billion specimens worldwide by providing a structured framework that clarifies the outcomes of digitisation and quantifies the level of digitisation achieved, and assists prioritisation of the remaining work;
2. To improve the quality of published data by providing clarity to collection managers about the minimum quantity and quality of information they should be publishing to make digital specimen information useful for multiple purposes of research, teaching and learning, etc.;
3. To support and contribute towards assessments of fitness for purpose of data (suitability) for feeding specific types of data processing pipelines;
4. To assist researchers to know what information to include in their publications about specimens they have used in their research, and,
5. To enable efficient querying, aggregation and self-contained data processing by computing systems (machine-actionability, de Smedt 2020) based on provision of rich contextual (meta)data in compliance with the FAIR principles (Wilkinson 2016).

MIDS defines what information about a specimen should be available but it does not attach specific value to that information because attaching value depends both upon the information itself and the purpose to which that is put.

The levels of digitisation and their expected information content defined herein, and named as Minimum Information about a Digital Specimen (MIDS) are based on major research and curation requirements put forward by national museums and herbaria.


## 1.1 Audience

This document is intended primarily for those who are responsible for digitising and sharing data publicly (publishing data) about natural science specimens. It can also be useful to those who are developing applications, tools and workflows related to digitisation, comparing and evaluating digitisation projects, and for those reporting to collection management personnel, and funding agencies.


## 1.2 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119. [RFC-2119]

## 1.3 Content

This document is concerned with the specification of Minimum Information about a Digital Specimen (MIDS). Sections are designated as either ‘informative’ or ‘normative’. This document first explains the rationale, principles of MIDS and the MIDS 1 level of digitisation, then details the information elements to be expected at this MIDS level. A normative definition of each MIDS-1 information element is provided, including constraints and mappings to Darwin Core (DwC) [terms](https://dwc.tdwg.org/terms/) and Access to Biological Collection Data (ABCD) [terms](https://abcd.tdwg.org/terms/). An implementation conformance statement (ICS) proforma is provided to allow declarations of conformance to be made. Illustrative use cases and guidelines for use are also provided.

## 1.4 Definitions

**bare record** – the association between an identifier of a physical specimen and its initial digital representation, allowing for subsequent unambiguous attachment of all other information (cf. basic record, regular record and extended record).

**basic record** – a limited set of information about the specimen; for example, physical specimen identifier and barcode details, and details of the collection it belongs to (cf. bare record, regular record and extended record).

**data (also known as content data)** – data relating directly to describing physical specimens, such as images of those specimens, information from specimen labels (scientific name, location where collected, date collected, collector name, etc.), links to third-party semantic resources, or measurements and other analyses of specimens.

**digital specimen** – a digital representation on the Internet (digital twin) corresponding to a physical specimen in a natural science collection.

**digitisation** – the process of converting analog information about physical specimens (e.g. in natural science collections) to digital form, which therefore includes electronic text, images and other representations; and making that publicly available.

**extended record** – a comprehensive set of elements describing the specimen; for example: all label data, annotations and determination history (cf. bare record, basic record and regular record).

**levels of digitisation** – a simple categorisation of the type and depth of digitisation achieved by different approaches to digitisation.

**natural science collection** – a collection of natural science objects, such as preserved plants and animals, fossils, rocks and minerals, gems, etc. curated and maintained by an institution such as a museum or a university.

**persistent identifier (PID)** – a persistent identifier is a string (functioning as a symbol) that uniquely identifies a thing. The identifier can be persistently resolved to digitally actionable meaningful information about the identified thing.

**regular record** – a set of information describing the specimen; for example, physical specimen identifier, barcode details, taxon name, collection date and place, collector, etc. (cf. bare record, basic record and extended record).

## 1.5 Acknowledgements

This minimum information specification is the result of work carried out jointly with contributions from multiple funded projects that include:

*   CETAF Digitisation Working Group;
*   European Union Horizon 2020-funded ICEDIG project (grant agreement no. 777483);
*   European Union Horizon 2020-funded SYNTHESYS+ project (grant agreement no. 823827);
*   European Union Horizon 2020-funded DiSSCo Prepare project (grant agreement no. 871043);
*   European Union COST Action CA17106 MOBILISE; and,
*   US National Science Foundation (NSF) Advancing Digitization of Biodiversity Collections Program DBI-1547229 (2016-2021), iDigBio.

# 2 Background (informative)

## 2.1 Processes of digitisation (informative)

About 2 billion physical objects cared for, organised and catalogued in thousands of natural science collections around the world represent an important data resource in botany, zoology, geology and other disciplines for research addressing scientific and societal questions. In common with most other contemporary scientific endeavours, when scientists working with such objects find themselves able to access data resources electronically without leaving their desks, they quickly find that they want to access further resources that are sometimes not so advanced in terms of ‘digital transformation’ [Meyer 2015]. An important component of digital transformation in natural sciences is the process of making data about collections and the physical objects in those collections digitally available, findable, and accessible by acquiring data from the physical objects themselves (i.e., by digitisation), through curation and further processing of that data, to open data publication and use.

Digitisation can lead to digital data for collections as a whole, for sub-parts of collections (inventories of trays of insects, boxes of herbarium sheets, for example) and for individual specimens. The first two categories contribute towards providing coverage and access information about the holdings of a collection-holding institution, in terms of scope and extent and are the subject of a companion [Collection Descriptions standard](https://github.com/tdwg/cd). Digitisation of specimens, which is the focus of the present specification provides explicit and precise data about each object curated in a collection. Capturing and presenting such data in standard formats is essential so that they can be easily understood, compared, analysed and communicated. Similarly, ensuring that enough data are captured, curated and published is essential so that they are useful for the widest possible range of purposes. Finally, ensuring that such data are consistently indexed and identified, such that they can be found, accessed and used is critical. The transition to mass digitisation has increased the use of staged processes of digitisation, with the introduction of earlier stages which capture fewer data elements. This is the rationale for minimum information specifications such as the present one.

## 2.2 Stages of digitisation (informative)

At the level of specimens, digitisation can be characterised generally as consisting of several activities, with data created as a result of each activity:

*   Attaching an identifier to a physical specimen and creating a digital catalogue record, perhaps with its own digital identifier. This can include attaching collection-level data (from cabinets, boxes, folders, trays, etc.) to a group of specimens;
*   Specimen data capture, which can include:
    *   Making one or more images of the specimen and/or its labels; and,
    *   Extracting, processing and encoding information from those labels and images into a digital record;
*   Enriching the digital record with supplementary information that can include determinations, annotations, and/or information from a wide variety of third-party sources (references to published literature, genetic sequences, etc.).

These stages are often implemented as workflows, which can vary in their details from one institution or project to another. Nevertheless, the heterogeneity of approaches and the variations are understood [Nelson 2015]. These and other differences of approach are accommodated by MIDS.

## 2.3 Harmonising the approach (informative)

Multiple digitisation initiatives around the world capture digital data about specimens. An important concern in digitisation is how much detail to digitise from each physical specimen. While a photographic image can often be made quickly, transcribing and interpreting all the details from labels, enriching the data with external information, and making specific measurements of the specimen take more time and resources. Often, digitisation projects have been conceived to support specific scientific needs leading to variable outcomes in terms of what data are captured and how they are presented. The idea of ‘Minimum Information about a Digital Specimen’ (MIDS) has been conceived to structure this complexity.

Mobilising, unifying and delivering natural science (bio- and geo-diversity) information at the scale, form and precision required by the scientific communities can be accomplished in part by harmonising policy into guidelines about practical levels of digitisation to apply and also in part by harmonising the information to be expected from each level of digitisation. The present specification addresses the latter.
Harmonisation of information provides clarity about the minimum information that collection-holding institutions should be publishing in the future to make collections and digital specimens useful for multiple purposes of research, teaching and learning, etc. Similarly, by harmonising a framework that clarifies what is meant by different levels of digitisation it becomes easier to consistently measure the extent of digitisation achieved over time (e.g., via a collection digitisation dashboard) and to set priorities for the remaining work.

The notions of extended specimens [Webster 2017] and Next Generation Collections [Schindel 2018], together with work of initiatives such as Integrated digitised Biocollections (iDigBio), Distributed System of Scientific Collections (DiSSCo), National Research Collections Australia (NRCA) Digital, SpeciesLink, National Science & Technology Infrastructure (NSII), the Biodiversity Collections Network (BCoN) and the One World Collection project further drive the need for data harmonisation. Collections-based science is global in nature and increasingly digital. In this context, barriers to interoperability and re-use must be lowered and eventually removed and global solutions are highly desirable.

The Minimum Information about a Digital Specimen (MIDS) specification, and its companion specification for information about collections – the Collection Description (CD) standard – aims to address these problems. Adoption and use of MIDS (and CD) contributes to making natural sciences specimen data more compliant with the guiding principles of FAIR (‘Findable, Accessible, Interoperable, Reusable’) [Wilkinson 2016, Mons 2017] and is a step towards enabling repeatability in research studies with FAIR specimen-based digital objects [Harjes 2020].

## 2.4 Accommodating variability in details of the process (informative)

Heterogeneous approaches to digitisation are accommodated in MIDS via a simple categorisation based on the form and depth of digitisation achieved. 

MIDS is divided into several levels that represent a progression through the stages of digitisation. Not all digitisation programmes can publish all the information right from the beginning, and it is useful when collections owners publish lesser quantities at the earliest stages. Indeed, it is likely that many digitisation programmes cannot or do not publish all the information at all. Only through subsequent processes of research, annotation and interpretation, and extension can specimen information become increasingly enriched and more (but never) complete. Such processes ebb and flow with the tide of scientific enquiry, contributing to and building up an ever-richer corpus of information associated with digitised artefacts. Since we can never know all there is to know about a specimen, the processes never finish and thus there can be no notion of maximum or complete information. The highest ‘gold standard’ MIDS level 3 is open-ended to account for this.

In support of the generalised digitisation workflow, MIDS defines the information elements expected at each level of digitisation and strongly encourages that data resulting from digitisation should be made openly available online on the Internet. Thus, in the context of MIDS, “digitised” means not only existing in digital form but also existing as “online representations that are publicly available i.e., openly findable and accessible”. Note here that ‘accessible’ means to the extent that access is not restricted based on objective criteria defined by national security, legislation or other regulatory compliance, sensitivity of collection information, and third-party rights (such as personal privacy).

MIDS is a 'minimum specification'. This means that at any specific MIDS level a defined set of expected information elements should be the minimum amount of information made digitally and openly available online following each of the major stages of digitisation identified in the generalised workflow (2.2 above). Because MIDS is a minimum specification, publishing more extensive sets of information elements is not precluded and is, in fact, strongly recommended.

Specific practices of digitisation and data publication vary widely among institutions, meaning that different elements of information can become available as the result of specific detailed workflows steps, the order of which can vary from one institution to another. Similarly, the way in which different elements of information are mapped to standard terms also varies. MIDS accommodates this variability and always allows the presence of information elements additional to the expected elements at any MIDS level. These can include elements listed at higher MIDS levels, as well as other elements beyond those listed; for example, institution or collection specific elements. As a general principle, institutions should publish the fullest available data about their collections and individual specimens at the earliest opportunity, expecting that such data is likely to become enriched and annotated over time.

# 3 Principles of the MIDS-1 level of digitisation (normative)

## 3.1 Authoritative data and variations in digitisation

MIDS must focus on the primary, curated scientific information denoted as being authoritative in relation to the specimen. This generally includes the ‘what, when, where, and who’ of the specimen i.e., What is it? When was it collected? Where was it collected? And who by? Apart from management information such as accession numbers, barcodes and catalogue numbers, ‘what, when, where, who’ is the minimum information usually curated in natural science collections. It is also normally a principal product of digitisation processes, alongside capturing photographic images of specimens. Thus, establishing this quartet of ‘what, when, where, and who’ as the standard to be achieved as the regular level of information to be expected, is completely rational. Nevertheless, digitisation processes vary from one specimen category to another and between institutions. Different levels of information – some less comprehensive, some more so – become available at different points in digitisation processes. Thus, MIDS offers several levels of minimum information to be expected or achieved as the output of various stages of what is quite a variable process in the way it is conducted from one institution or collection to another.  

## 3.2 Other data present or known about a specimen

In contrast to the authoritative data about a specimen, a wide variety of secondary or supplementary data may also be associated with a specimen. This can include references in literature, the results of various kinds of analysis such as (bio)chemical analysis, DNA sequencing or radiocarbon dating, links to audio and video recordings, habitat information, etc. Such data can be held with the specimen or its catalogue record, or they can be held in other institutes and databases beyond the institution holding the physical specimen. They are data that can become associated with a specimen.

Supplementary data can either be directly related to the physical specimen, as in the case of a database record of a DNA sequence taken from a tissue sample cut from the specimen; or such data can be related only indirectly. An audio recording of the birdsong of a species that the specimen represents is an example of the latter i.e., the recording is not of that specific individual but of another in the same taxon. Indirect relations are characterised as conceptual relations rather than direct or actual relations.

MIDS optionally allows for the minimum information about a specimen to be extended by making provision to capture and publish related data.


## 3.3 Prior to digitisation

In different cases, and to support processes in collection-holding institutions including accession processes and ‘digital by default’ processes, the need to create a digital record of a specimen can arise at a very early stage in the life cycle of an acquired specimen, even before digitisation processes have been initiated.

In some instances, a photographic image can also be made or be already available at such a moment. Or data related to other actions, such as DNA or chemical analysis and publication can become available. Actions like taking a photograph or carrying out an analysis can take place before accession to a collection and digitisation. They can occur even without a physical specimen ending up as preserved material in a collection. Such actions represent the very beginning of a digitisation process and can be precursive to further digitisation steps later.

When needed at such moments, a bare catalogue record may be created to associate a specimen with a catalogue entry or database record. This should normally be via the specimen’s identifier, associating a bare minimum of digital data (a catalogue number and, ideally a persistent identifier – see 3.4 below) with a physical specimen.

> Note 2:	MIDS supports early stage digital bare catalogue record creation by providing a pre-level of minimum information about a digital specimen, level zero (0) that is precursive to later steps.

## 3.4 Assigning persistent identifiers to digitised specimen data

As part of the minimum information required to make digital specimen data publicly available, a persistent identifier (PID) should be assigned to a specimen and its digital data as early as possible in the digitisation process; even prior to digitisation commencing (see 3.3 above). If a PID is available for the digital specimen, this should be published alongside the MIDS information.

> Note 3:	Persistent and global unique identification is an important step towards making digitised specimen data publicly available online so that they can be referred to unambiguously, for example in a journal article, or so that its data can be easily found, used and updated whenever necessary. With the advent of innovative services making greater use of PIDs in the future, persistently identified specimen data is expected to become more valuable over time. 

> Note 4:	By combining a generated suffix with a prefix from the Handle system i.e., &lt;prefix>/&lt;suffix> an unambiguous, persistent (long-lasting) resolvable reference to the digital specimen’s information can be created. A Digital Object Identifier (DOI™) is an example of such a persistent identifier.

> Note 5:	Beyond the recommendation above, the topic of persistent identification of specimen data is outside the scope of the present document.

## 3.5 MIDS-1 Level of minimum information

As outlined in Table 1, MIDS specifies three levels of ‘minimum information’, together with a pre-level, level zero (0). Except for level 0, each MIDS level of minimum information is a superset of the preceding level.

**Table 1: MIDS levels of minimum information**

<table>
  <tr>
   <th><strong>MIDS level</strong>
   </th>
   <th><strong>Record extent</strong>
   </th>
   <th><strong>Purpose</strong>
   </th>
  </tr>
  <tr>
   <td>1
   </td>
   <td>Basic
   </td>
   <td>A basic record of specimen information.
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>Regular
   </td>
   <td>Key information fields that have been agreed over time as essential for most scientific purposes.
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>Extended
   </td>
   <td>Other data present or information known about the specimen, including links to third-party sources.
   </td>
  </tr>
  <tr>
   <td><em>0 (Note)</em>
   </td>
   <td><em>Bare</em>
   </td>
   <td><em>A bare or skeletal record making the association between an identifier of a physical specimen and its digital representation, allowing for unambiguous attachment of all other information.</em>
   </td>
  </tr>
  <tfoot>
   <tr>
    <th style="font-weight:400;text-align:left" colspan="3" >
     Note:	Level 0 is equivalent to creating a simple catalogue record containing a physical specimen identifier, such as a barcode number. Level 0 often precedes fuller digitisation steps that yield more detailed information. Hence, level 0 is termed a pre-level. Nevertheless, level 0 data is useful minimum information for advertising or knowing about the existence of specimens.
    </th>
   </tr>
  <tfoot>
</table>

**<span style="text-decoration:underline;">MIDS level 1</span>** is a basic level of information about a specimen. The creation of a basic digital record with an identifier enables all other information (including images and/or other media types) to be associated with a single physical specimen. Two elements to define the scope of a physical specimen and to provide some information about the kind of object, as well as the institution in which the specimen is held, are included to create a virtual representation of the physical collections, enabling similar search and browsing capabilities online as researchers and curators would have at the cabinets of physical specimens. Two metadata elements are included to provide information about when the record was last updated as well as how the user is permitted to use the information.

**<span style="text-decoration:underline;">MIDS level 0</span>** (usually being established prior to any formal digitization and hence considered a pre-level) is a bare level of information that exists to make an association between a physical specimen with its identifier (barcode, for example) and an entry in a catalogue or database. One early action in a digitisation process is the creation of a database record that acknowledges or coincides with the existence or accession of a physical specimen into a collection, but not necessarily with any other information digitised at that stage. Note, however that image(s) can be generated and referenced at this early stage.

## 3.6 Information elements expected and expansion beyond the minimum

At each level, MIDS defines the information elements that must be present. This is specified in section 4 below

In addition to the information elements expected to be present as a minimum, MIDS must always allow the presence of other information elements beyond the minimum, including institutional and collection specific elements.

> Note 6:	It is not precluded and is encouraged that institutions publish information beyond the minimum. However, information does not qualify as meeting a specific MIDS level unless all the information elements expected at that level are available with actual values.

# 4 Information content and element mappings for each MIDS Level (normative)

Sections 4.1 & 4.2 summarise in tables the information elements expected to be present at MIDS levels 1 and 0 respectively. Full definitions of each information element, their mappings to other standards, constraints and examples are specified in tables in section 4.5.

Section 4.3 specifies additional requirements for handling of unknown or incomplete data that must be applied in conjunction with the relevant information elements.

## 4.1 Information elements expected at MIDS level 0

The information elements expected to be present in digital specimen data published at MIDS level 0 are listed in Table 1 below. The terms being developed for the information elements can be found in the TDWG MIDS GitHub site under [MIDS-0](https://github.com/tdwg/mids/issues?q=is%3Aissue+is%3Aopen+label%3AMIDS-0).

**Table 1: MIDS Level 0: Expected elements, mappings and recommendations for a bare record**

<table>
  <tr><th></th>
   <th>MIDS information element
   </th>
   <th>Definition
   </th>
   <th>Purpose
   </th>
   <th>Required (Bio/Geo/Paelaeo)
   </th>
  </tr>

  <tr><td>3</td>
   <td> PhysicalSpecimenID <br>
   </td>
   <td>A unique identity for the specimen within the curating institution. Whatever the institution uses to uniquely identify the item. For example: DOI, stable identifier, catalogue number, barcode, etc.
   </td>
   <td>To allow the curator/researcher to identify the physical specimen the data refer to. To allow citation of the specimen. To enable the attachment of additional information to the specimen record.
   </td>
   <td>Yes (all)
   </td>
  </tr>

  <tr><td>4</td>
   <td>Organization<br>
  </td>
   <td>A term to indicate in which institution the specimen is held. This may include an institution code and an institution identifier.
   </td>
   <td>To allow a user to locate the physical location of the specimen.
   </td>
   <td>Yes (all)
   </td>
  </tr>

</table>

An image and/or other multimedia may be present.


## 4.2 Information elements expected at MIDS level 1

The information elements expected to be present in digital specimen data published at MIDS level 1 are listed in Table 2 below. The terms being developed for the information elements can be found in the TDWG MIDS GitHub site under [MIDS-1](https://github.com/tdwg/mids/issues?q=is%3Aissue+is%3Aopen+label%3AMIDS-1).

**Table 2: MIDS Level 1: Expected elements, mappings and recommendations for a basic record**

<table>
  <tr><th></th>
   <th>MIDS information element
   </th>
   <th>Definition
   </th>
   <th>Purpose
   </th>
   <th>Required (Bio/Geo/Paelaeo)
   </th>
  </tr>

  <tr><td>3</td>
   <td> PhysicalSpecimenID <br>
   </td>
   <td>A unique identity for the specimen within the curating institution. Whatever the institution uses to uniquely identify the item. For example: DOI, stable identifier, catalogue number, barcode, etc.
   </td>
   <td>To allow the curator/researcher to identify the physical specimen the data refer to. To allow citation of the specimen. To enable the attachment of additional information to the specimen record.
   </td>
   <td>Yes (all)
   </td>
  </tr>

  <tr><td>4</td>
   <td>Organization<br>
  </td>
   <td>A term to indicate in which institution the specimen is held. This may include an institution code and an institution identifier.
   </td>
   <td>To allow a user to locate the physical location of the specimen.
   </td>
   <td>Yes (all)
   </td>
  </tr>

  <tr><th></th>
   <th>Name
   </th>
   <th>A name given to the object. Any string of characters and/or numbers by which the object is referenced within a collection. For example, the name the specimen is stored under, its scientific or taxonomic name if known, how it is labelled, etc. This name is not necessarily its name according to an accepted scientific classification, identification, or taxonomic determination (i.e., scientific name) but it often can be the same as that.
   </th>
   <th>Information to aid the discoverability of specimens by users and the ability to retrieve them within a collection.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>SpecimenType
   </th>
   <th>High-level term to delimit and define specimens. For example: preserved specimen, fossil specimen, as opposed to observation.
   </th>
   <th>To delimit the specimens to which the MIDS specification refers.
   </th>
   <th>Required (Biological/Geological/Paelaeontological)
   </th>
  </tr>

  <tr><th></th>
   <th>MIDS information element
   </th>
   <th>Definition
   </th>
   <th>Purpose
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>ObjectType
   </th>
   <th>General term to describe the kind of specimen. In combination with SpecimenType - hierarchical; a more specific classification than described by SpecimenType. For example: microscope slide, pinned insect, herbarium sheet.
   </th>
   <th>To enable curators to determine equipment/method/cost of imaging the specimen, to enable researchers to determine equipment/method required for viewing/analysing the specimen, to enable curators/researchers to know in which collection/location within the institution the specimen is held.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>License
   </th>
   <th>License under which the specimen data are published.
   </th>
   <th>To enable all users to determine how they can use the specimen data.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><td>1</td>
  <td>Modified<br>
   </td>
   <td>UTC date/time of first creation or subsequent modification, if any
   </td>
   <td>To enable users (humans/machines) to determine if there have been any changes to the record since it was last viewed.
   </td>
   <td>Yes (all)
   </td>
  </tr>


</table>

An image and/or other multimedia may be present.

## 4.3 Information elements expected at MIDS level 2

The information elements expected to be present in digital specimen data published at MIDS level 2 are listed in Table 3 below. The terms being developed for the information elements can be found in the TDWG MIDS GitHub site under [MIDS-1](https://github.com/tdwg/mids/issues?q=is%3Aissue+is%3Aopen+label%3AMIDS-1).

**Table 3: MIDS Level 2: Expected elements, mappings and recommendations for a regular record**

<table>
  <tr><th></th>
   <th>MIDS information element
   </th>
   <th>Definition
   </th>
   <th>Purpose
   </th>
   <th>Required (Bio/Geo/Paelaeo)
   </th>
  </tr>

  <tr><td>3</td>
   <td> PhysicalSpecimenID <br>
   </td>
   <td>A unique identity for the specimen within the curating institution. Whatever the institution uses to uniquely identify the item. For example: DOI, stable identifier, catalogue number, barcode, etc.
   </td>
   <td>To allow the curator/researcher to identify the physical specimen the data refer to. To allow citation of the specimen. To enable the attachment of additional information to the specimen record.
   </td>
   <td>Yes (all)
   </td>
  </tr>

  <tr><td>4</td>
   <td>Organization<br>
  </td>
   <td>A term to indicate in which institution the specimen is held. This may include an institution code and an institution identifier.
   </td>
   <td>To allow a user to locate the physical location of the specimen.
   </td>
   <td>Yes (all)
   </td>
  </tr>

  <tr><th></th>
   <th>Name
   </th>
   <th>A name given to the object. Any string of characters and/or numbers by which the object is referenced within a collection. For example, the name the specimen is stored under, its scientific or taxonomic name if known, how it is labelled, etc. This name is not necessarily its name according to an accepted scientific classification, identification, or taxonomic determination (i.e., scientific name) but it often can be the same as that.
   </th>
   <th>Information to aid the discoverability of specimens by users and the ability to retrieve them within a collection.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>SpecimenType
   </th>
   <th>High-level term to delimit and define specimens. For example: preserved specimen, fossil specimen, as opposed to observation.
   </th>
   <th>To delimit the specimens to which the MIDS specification refers.
   </th>
   <th>Required (Biological/Geological/Paelaeontological)
   </th>
  </tr>

  <tr><th></th>
   <th>MIDS information element
   </th>
   <th>Definition
   </th>
   <th>Purpose
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>ObjectType
   </th>
   <th>General term to describe the kind of specimen. In combination with SpecimenType - hierarchical; a more specific classification than described by SpecimenType. For example: microscope slide, pinned insect, herbarium sheet.
   </th>
   <th>To enable curators to determine equipment/method/cost of imaging the specimen, to enable researchers to determine equipment/method required for viewing/analysing the specimen, to enable curators/researchers to know in which collection/location within the institution the specimen is held.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>License
   </th>
   <th>License under which the specimen data are published.
   </th>
   <th>To enable all users to determine how they can use the specimen data.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><td>1</td>
  <td>Modified<br>
   </td>
   <td>UTC date/time of first creation or subsequent modification, if any
   </td>
   <td>To enable users (humans/machines) to determine if there have been any changes to the record since it was last viewed.
   </td>
   <td>Yes (all)
   </td>
  </tr>

  <tr><th></th>
   <th>qualitativeLocation
   </th>
   <th>A term to describe where the specimen was collected. In combination with quantitativeLocation; should capture textual geographic information.
   </th>
   <th>A human readable location. Can also be used to help identify the quantitativeLocation.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>quantitativeLocation
   </th>
   <th>A term to describe where the specimen was collected. A quantitative measure that would include coordinate or shape data, an identifier, or data that can be easily converted into a quantitative measure. In combination with the qualitative term, Locality.
   </th>
   <th>To enable a person or machine to identify and/or map the geographical location in which the collection was made.
   </th>
   <th>Yes (all)
   </th>
  </tr>

  <tr><th></th>
   <th>GeologicalAge
   </th>
   <th>Terms denoting the names of strata and/or their age from which a specimen is derived.
   </th>
   <th>To provide geological context to the specimen
   </th>
   <th>Yes (Geological)
   </th>
  </tr>


  <tr><th></th>
   <th>collectingAgent
   </th>
   <th>A list (concatenated and separated) of names of people, groups, or organizations responsible for recording the original Occurrence. The primary collector or observer, especially one who applies a collecting identifier (recordNumber), should be listed first.
   </th>
   <th>For many biological collections this information has been used as an identifier for the specimen in literature. It also helps in the identification and validation of the collecting location.
   </th>
   <th>Yes (Biological)
   </th>
  </tr>

  <tr><th></th>
   <th>dateCollected
   </th>
   <th>The date/time at which a gathering event occurred. For specimen gathering, this is the date/time when the event was recorded.
   </th>
   <th>
   </th>
   <th>Yes (Biological)
   </th>
  </tr>

  <tr><th></th>
   <th>collectingNumber
   </th>
   <th>An identifier given to the specimen at the time it was recorded. Often serves as a link between field notes and a specimen record.
   </th>
   <th>For many biological collections the collector in combination with collectingNumber has been used as an identifier for the specimen in literature. It also helps in the identification and validation of the collecting location.
   </th>
   <th>Yes (Biological)
   </th>
  </tr>

  <tr><th></th>
   <th>Type status
   </th>
   <th>A list (concatenated and separated) of nomenclatural types (type status, typified scientific name, publication) applied to the subject.
   </th>
   <th>Purpose
   </th>
   <th>
   </th>
  </tr>

  <tr><th></th>
   <th>Media
   </th>
   <th>A list (concatenated and separated) of identifiers (publication, global unique identifier, URI) of media associated with the Occurrence.
   </th>
   <th>Purpose
   </th>
   <th>Yes (Biological)
   </th>
  </tr>

</table>

An image and/or other multimedia may be present.




## 4.3 Information element definitions
The following subsections specify the details of the individual MIDS Level 1 information elements.

*28 May 2022: MIDS elements beyond MIDS level 0 and 1 are not yet discussed and agreed. Additional documents will be added for each as they are agreed.*

### 4.3.1 MIDS element - Modified
| <!-- --> | <!-- --> |
| ---- | ---- |
| **MIDS information element** | Modified |
| **Definition** | UTC date/time of date/time of first creation or subsequent modification, if any |
| **DwC term (latest, 2014-11-08)** | [modified](https://dwc.tdwg.org/terms/#dcterms:modified) (*note, is an imported dcterm*) |
| **ABCD term name(3.0)** | [hasDateModified](http://rs.tdwg.org/abcd/terms/hasDateModified) |
| **Applicable standard(s)/recommendation(s)** | Use [ISO 8601](https://www.iso.org/standard/70907.html). UTC date/time, extended format (for human readability) |
| **Element identifier** |  |
| **Required** | Yes |
| **Repeatable** | No |
| **Constraints** |  |
| **Examples** | 2021-01-20T10:54:18Z |
| ***Element specification status*** | *agreed; accepted in specification* |
| ***Notes*** | *...* |

### 4.3.2 MIDS element - MIDSLevel


### 4.3.3 MIDS element - PhysicalSpecimenId
| <!-- --> | <!-- --> |
| ---- | ---- |
| **MIDS information element** | PhysicalSpecimenId |
| **Definition** | A unique identity for the specimen within the curating institution. Whatever the institution uses to uniquely identify the item, for example: specimen identifier, barcode, catalogue number, etc. |
| **DwC term (latest, 2014-11-08)** | [catalogNumber](http://rs.tdwg.org/dwc/terms/catalogNumber) (*note, term used by GBIF is catalogNumber*) |
| **ABCD term name(3.0)** | [physicalObjectID](http://rs.tdwg.org/abcd/terms/physicalObjectID) |
| **Applicable standard(s)/recommendation(s)** | Cardinality 1..n |
| **Element identifier** |  |
| **Required** | Yes |
| **Repeatable** | Yes. An object can have several identifiers.  |
| **Constraints** | The physical specimen identifier, when given back to the organization indicated by the Institution information element must be sufficient to allow the organization to locate the object(s) the user is interested in. In cases where a single identifier identifies multiple objects (as is possible in some collections) information such as objectType, materialType and preparationType may also need to be given. |
| **Examples** | *To be added*  |
| ***Element specification status*** | *agreed* |
| ***Notes*** | *...* |

### 4.3.4 MIDS element - Institution
| <!-- --> | <!-- --> |
| ---- | ---- |
| **MIDS information element** | **Institution [Code, Referent]** |
| **Definition** | Identifier(s) of the institution. Has two parts: i) Code: The name (or acronym) in use by the institution having custody of the object(s) or information referred to; and ii) Referent:  An identifier of the organisation signified by Code. |
| **DwC term (latest, 2014-11-08)** | i) [institutionCode](http://rs.tdwg.org/dwc/terms/institutionCode), ii) No equivalent |
| **ABCD term name(3.0)** | i) [sourceInstitutionID](http://rs.tdwg.org/abcd/terms/sourceInstitutionID), ii) No equivalent |
| **Applicable standard(s)/recommendation(s)** | Acronyms (namestrings) for Code will typically come from the [GBIF Registry of Scientific Collections (nee GrSciColl)](https://www.gbif.org/grscicoll); else ‘unknown’. Unique identifiers for Referent should come from either [ROR](https://ror.org/) or [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page); else ‘unknown’. |
| **Element identifier** |  |
| **Required** | Yes |
| **Repeatable** | Yes. Multiple organisation identifiers are likely for the same organisation. Multiple name acronyms are also possible. See constraints |
| **Constraints** | When there are multiple identifiers for the organisation represented by Code, the Referent part can be repeated as necessary i.e., *Institution [Code, Referent1, Referent2, ... ReferentN]*. <br>When an organisation is known by multiple Codes (e.g., due to historical reasons) the information element must be repeated for each Code with all of the Referents i.e., *Institution [Code1, Referent1, Referent2, ... ReferentN]*, *Institution [Code2, Referent1, Referent2, ... ReferentN]*.  |
| **Examples** | *To be added*  |
| ***Element specification status*** | *agreed; accepted in specification* |
| ***Notes*** | *...* |

### 4.3.5 MIDS element - MaterialSample
| <!-- --> | <!-- --> |
| ---- | ---- |
| **MIDS information element** | MaterialSample |
| **Definition** | High-level term for the classification of curated objects. |
| **DwC term (latest, 2014-11-08)** | proposed:  |
| **ABCD term name (3.0)** |  |
| **Applicable standard(s)/recommendation(s)** | |
| **Element identifier** |  |
| **Required** | No |
| **Repeatable** | No |
| **Constraints** |  |
| **Examples** | *To be added* |
| ***Element specification status*** | *agreed; accepted in specification. Created following TG mtg no. 7.* |
| ***Notes*** |  |

### 4.6.6 MIDS element - PreparationType
| <!-- --> | <!-- --> |
| ---- | ---- |
| **MIDS information element** | PreparationType |
| **Definition** | General terms for the classification of curated objects according to the way they have been prepared.  In combination with ObjectType - hierarchical; a more specific classification than described by ObjectType. |
| **DwC term (latest, 2014-11-08)** | preparations |
| **ABCD term name (3.0)** | Unit/SpecimenUnit/Preparations/Preparation/PreparationType |
| **Applicable standard(s)/recommendation(s)** | |
| **Element identifier** |  |
| **Required** | Yes |
| **Repeatable** | No |
| **Constraints** | Controlled vocabulary. Preparation Type should be set in conjunction with MaterialSample, as each MaterialSample has specific Preparation Types. |
| **Examples** | *To be added* |
| ***Element specification status*** | *proposed alteration* |
| ***Notes*** | *Same interpretation as [cd:preparationType](https://github.com/tdwg/cd/issues/64). Must not be used for classifying objects by taxon. Definition of the controlled vocabulary is still needed.* |


### 4.3.7 MIDS element - Name
| <!-- --> | <!-- --> |
| ---- | ---- |
| **MIDS information element** | Name |
| **Definition** | A name given to the object. Equivalent to the Dublin Core term [dc:title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/title). Any string of characters and/or numbers by which the object is referenced within a collection. For example, the name the specimen is stored under, it’s scientific or taxonomic name if known, how it is labelled, etc. This name is not necessarily its name according to an accepted scientific classification, identification, or taxonomic determination (i.e., scientific name) but it often can be the same as that. |
| **DwC equivalent term (latest, 2014-11-08)** | [scientificName](http://rs.tdwg.org/dwc/terms/scientificName), [organismName](https://dwc.tdwg.org/list/#dwc_organismName), [vernacularName](https://dwc.tdwg.org/list/#dwc_vernacularName), etc. |
| **ABCD equivalent term (3.0)** | [name](http://rs.tdwg.org/abcd/terms/name), [fullScientificName](http://rs.tdwg.org/abcd/terms/fullScientificName), [informalName](http://rs.tdwg.org/abcd/terms/informalName), etc. |
| **Applicable standard(s)/recommendation(s)** | |
| **Element identifier** | name |
| **Required** | Yes |
| **Repeatable** | No |
| **Constraints** | None |
| **Examples** | *Colias croceus* (Geoffroy, 1785), Ophthalmosaurus, Australian Baobab, Scottish rock, etc. |
| ***Element specification status*** | *agreed; accepted in specification* |
| ***Notes*** | *...* |
 
### 4.3.8 MIDS element - Licence
| <!-- --> | <!-- --> |
| ---- | ---- |
| **MIDS information element** | Licence |
| **Definition** | The licence under which the information is published. |
| **DwC equivalent term (latest, 2014-11-08)** | |
| **ABCD equivalent term (3.0)** |  |
| **Applicable standard(s)/recommendation(s)** | |
| **Element identifier** | name |
| **Required** | Yes |
| **Repeatable** | No |
| **Constraints** | None |
| **Examples** | *CC-0* |
| ***Element specification status*** | *proposed* |
| ***Notes*** | *...* |

## 4.4 Handling of unknown and incomplete data

Best practice dictates that wherever possible data should not be published with empty field values as this is misleading for both human users and machines. There are many reasons why data can be missing, unknown, incomplete or explicitly withheld [Groom 2019] and various tactics have been used in the past to deal with such situations. However, with the increasing use of machines to interpret and act upon data, variable past practices should be deprecated, and new, more consistent practices promoted. In the interest of presenting more meaningful corpora of minimum specimen information in the future, the present specification (4.5.1 - 4.5.3 below) recommends harmonising an approach for presenting minimum information fields where the content of those fields can be unknown or incomplete for a variety of reasons.

### 4.4.1 Unknown datetime in CreatedON/ModifiedON information elements

If the creation and/or modification date/time of a specimen data record is not known, the standard form for unspecified date/time, as specified in ISO 8601-2:2019 should be used for the createdON and/or modifiedON information element(s) i.e., “X*” or “XXXX-XX-XX”.

### 4.4.3 Unknown values for other information elements

Table 4 lists the terms that should be used in lieu of any of the information elements listed in Table 2 & 3 above being left empty.

**Table 4: Terms for missing data values in lieu of empty information elements**

Based on [Groom 2019], Table 1. [CC BY](https://creativecommons.org/licenses/by/4.0/).

<table>
  <tr>
   <th>Missing data term
   </th>
   <th>Definition
   </th>
   <th>Example
   </th>
  </tr>

  <tr>
   <td>unknown<br>(Note 1)
   </td>
   <td>The information is not digitally available.
   </td>
   <td>Empty value in a digital record of unknown provenance.
   </td>
  </tr>

  <tr>
   <td>unknown:undigitized<br>(Note 1, Note 2)
   </td>
   <td>The information is not digitally available. No attempt has been made to digitize it.
   </td>
   <td>Empty value in a skeletal record to which data still need to be added from the label.
   </td>
  </tr>

  <tr>
   <td>unknown:missing<br>(Note 1, Note 2)
   </td>
   <td>The information is not digitally available. It appeared to be absent during digitization.
   </td>
   <td>A value of S.D. (<em>sine dato</em>) used by transcription platforms to indicate the absence of a date value.
   </td>
  </tr>

  <tr>
   <td>unknown:indecipherable<br>(Note 1, Note 2)
   </td>
   <td>The information is not digitally available. It appeared to be present during digitization but failed to be captured.
   </td>
   <td>An indication made by a transcriber that they failed to transcribe the information.
   </td>
  </tr>

  <tr>
   <td>known:withheld<br>(Note 3)
   </td>
   <td>The information is digitally available, but it has been withheld by the provider.
   </td>
   <td>A georeferenced record for which coordinate data are available but withheld for conservation reasons.
   </td>
  </tr>

  <tr>
   <td>known:undigitized
   </td>
   <td>The information is known but has not been digitized (i.e., it is not digitally available).
   </td>
   <td>Label information that has not been transcribed because the digitization request/purpose does not require it.
   </td>
  </tr>

  <tr>
   <td>Not applicable
   </td>
   <td>The information element is not applicable
   </td>
   <td>One or more of the information elements 23 onwards in Table 4 may not be applicable. Some information elements are not applicable for some kinds of collection.
   </td>
  </tr>

  <tfoot>
   <tr>
    <th style="font-weight:400;text-align:left" colspan="3">
    Note 1:	The generic unknown indicates that the information is indeed not available.
    <br>
    Note 2:	The additives undigitized, missing and indecipherable allow elaboration as to why the data are unavailable, if this reason is known.
    <br>
    Note 3:	known:withheld indicates that the data are digitally available (e.g., in a primary source) and could potentially be retrieved after contacting the data provider.
    </th>
   </tr>
  </tfoot> 
</table>

# 5 Images and other media types (normative)

Many but not all digitization projects and programmes produce images of specimens and their accompanying label(s). It is helpful to users and machines, when searching for available digital specimens to know if images are available. Thus, a MIDS level information element (2) may be supplemented with one or both the designators specified in Table 7. 

As part of the minimum information about a specimen, digital specimens should (if possible) include at least one image of the complete specimen and its accompanying label(s). If images are present, the MIDS level of the digital specimen must be supplemented with the indicator ‘i’ indicating the availability of image(s).

Digital specimens may include multiple images of different types and/or other types of media. If other media type(s) are present, the MIDS level of the digital specimen must be supplemented with the indicator ‘m’ to indicate the availability of other media type(s).

**Table 5: Media elements of MIDS record types**

<table>
  <tr>
   <td><strong>MIDS level</strong>
   </td>
   <td><strong>Object image type</strong>
   </td>
   <td><strong>Recommendation</strong>
   </td>
  </tr>
  <tr>
   <td>i
   </td>
   <td>Object image with label
   </td>
   <td>Image should include the whole specimen where possible. Original label(s) should be included either in the same image or as separate images.
   </td>
  </tr>
  <tr>
   <td>m
   </td>
   <td>Other multimedia present
   </td>
   <td>No specific recommendation.
   </td>
  </tr>
</table>

Specimens can require more than one image to properly display all features of interest. Thus, multiple images can be present for a specimen. However, characterising the number and nature of image and other multimedia types available as outputs of digitization processes is outside the scope of the present specification.

# 6 Guidelines for machine-actionability (normative)

<div style="color:red">To do: &lt;insert text. This is the publishing/sharing aspect that is often treated separate from and after digitization. Publicly available means not only to humans but also for machines to find/access as well. FAIR statement of how MIDS supports each of the 15 principles.>
</div>

# 7 Recommendations for collection-holding institutions

MIDS is a minimum standard. As a general principle, institutions should aim to publish the fullest available data about their collections and individual specimens at the earliest opportunity. This means as soon as practically possible after digitisation, verification and curation activities have been carried out, expecting that such data can and will be enriched and annotated over time by exposure to a broad expert audience.

The minimum amount of information to be made available (published) must be the expected information elements at MIDS Level 1.

The information elements expected by MIDS Level 1 are the minimum amount of information to be published. As the gold standard, collection-holding institutions are encouraged to publish beyond the minimum where possible.

# 8 Data quality

Concerns about publishing junk data are not solved by MIDS. Collection-holding institutions should operate adequate quality controls during digitisation processes to ensure that published data are valid data, to the best of knowledge. Attention to prevention of digitization errors, simple (automated) checks and basic rules, such as avoiding unfilled information fields (i.e., use specific ‘unknown’ or ‘not specified’ values instead of leaving fields blank) each contribute to ensuring valid data.


# 9 Conformance (normative)

## 9.1 Principle means of conformance

*28 May 2022: ICS proforma tables to be revised - not presently uptodate. See current proposal under issue [#50](https://github.com/tdwg/mids/issues/50)*.

The principle means of conformance with the present specification must be through implementation of its requirements in workflows and processes of specimen digitisation and data management.

> Note 7:	Tools for automated verification of MIDS levels may become available in the future. 

## 9.2 Implementation Conformance Statement (ICS)

The Implementation Conformance Statement (ICS) proforma in Table 8 – Table 11 is a checklist collection-holding institutions and others can use to check and self-declare their conformance with the requirements of the present specification.

In the support column for each item, an assessor must answer the status questions with “yes” or “no” by ticking/unticking the checkboxes. Status values have the following meanings:

        m	mandatory to support the item/provide the information.

        o	optional to support the item/provide the information.

        m.N	mandatory to support at least one of the items/provide the information in the group N.

        o.N	optional to support one or more of the items/provide the information in the group N.

        c.N	conditional on item N. Answering the items in the table is conditional on the answer for item N.
<p style="color:red">
    _Editor’s note: On completion of proforma rows, numbering and cross-referencing to be checked/completed._
</p>

**Table 8: ICS proforma for MIDS conformance (general)**

<table>
  <tr>
   <th>Item
   </th>
   <th>Requirement
   </th>
   <th>Reference
   </th>
   <th>Status
   </th>
   <th>Support
   </th>
  </tr>

  <tr>
   <td>1
   </td>
   <td>Focus on the primary, curated scientific information denoted as being authoritative for the specimen
   </td>
   <td>§3.1
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>Publish specimen data at MIDS level 0
   </td>
   <td>§3.5
   </td>
   <td>m.1
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>Publish specimen data at MIDS level 1
   </td>
   <td>§3.5
   </td>
   <td>m.1
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>PID assigned to digital specimen data
   </td>
   <td>§3.4
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td>PID published alongside MIDS information
   </td>
   <td>§3.4
   </td>
   <td>c6:o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>8
   </td>
   <td>Unknown / unspecified datetime form supported i.e., “X*” or “XXXX-XX-XX”
   </td>
   <td>§4.5.1
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>9
   </td>
   <td> ?????Issue: remainder of ICS items need to be re-number and cross-references need to be checked and corrected. Need to look into autonumbering to solve this.?????
   </td>
   <td>§4.5.2
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>

    m.1: It is mandatory to support at least one of these items 2 – 5.

**Table 9: ICS proforma for MIDS level 0 conformance**

<table>
  <tr>
   <td colspan="3" >c.2: yes, no, n/a* (select according to answer in Table 8). If yes, complete this table.
   </td>
   <td colspan="2" >Choose an item.
   </td>
  </tr>
  <tr>
   <th>Item
   </th>
   <th>Requirement
   </th>
   <th>Reference
   </th>
   <th>Status
   </th>
   <th>Support
   </th>
  </tr>

  <tr>
   <td>6
   </td>
   <td>CreatedOn
   </td>
   <td>Table 5 1.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td>ModifiedOn
   </td>
   <td>Table 5 2.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>8
   </td>
   <td>RecordCreator<br>i) Name<br>ii) Referent
   </td>
   <td>Table 5 3.
   </td>
   <td><br>m<br>o
   </td>
   <td><br>☐<br>☐
   </td>
  </tr>
  <tr>
   <td>9
   </td>
   <td>MidsLevel
   </td>
   <td>Table 5 4.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td>PhysicalSpecimenId
   </td>
   <td>Table 5 5.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11
   </td>
   <td>Institution<br>i) Code<br>ii) Referent
   </td>
   <td>Table 5 6.
   </td>
   <td><br>m<br>o
   </td>
   <td><br>☐<br>☐
   </td>
  </tr>
  <tr>
   <td>12
   </td>
   <td>MaterialType
   </td>
   <td>Table 5 7.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13
   </td>
   <td>ScientificName<br>i) Name appropriate to the specimen<br>ii) Referent
   </td>
   <td>Table 5 8.
   </td>
   <td><br>m<br>o
   </td>
   <td><br>☐<br>☐
   </td>
  </tr>
  <tr>
   <td>14
   </td>
   <td>Has image(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>15
   </td>
   <td>Has other media type(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>

**Table 10: ICS proforma for MIDS level 1 conformance**

<table>
  <tr>
   <td colspan="3" >c.3: yes, no, n/a* (select according to answer in Table 8). If yes, complete this table.
   </td>
   <td colspan="3" >Choose an item.
   </td>
  </tr>
   <tr>
   <th>Item
   </th>
   <th>Requirement
   </th>
   <th>Reference
   </th>
   <th>Status
   </th>
   <th>Support
   </th>
  </tr>

  <tr>
   <td>16
   </td>
   <td>CreatedOn
   </td>
   <td>Table 2 1.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>17
   </td>
   <td>ModifiedOn
   </td>
   <td>Table 2 2.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>18
   </td>
   <td>RecordCreator<br>i) Name<br>ii) Referent
   </td>
   <td>Table 2 3.
   </td>
   <td><br>m<br>o
   </td>
   <td><br>☐<br>☐
   </td>
  </tr>
  <tr>
   <td>19
   </td>
   <td>MIDSLevel
   </td>
   <td>Table 2 4.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>20
   </td>
   <td>PhysicalSpecimenId
   </td>
   <td>Table 2 5.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>21
   </td>
   <td>Institution<br>i) Code<br>ii) Referent
   </td>
   <td>Table 2 6.
   </td>
   <td><br>m<br>o
   </td>
   <td><br>☐<br>☐
   </td>
  </tr>
  <tr>
   <td>22
   </td>
   <td>MaterialType
   </td>
   <td>Table 2 7.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>23
   </td>
   <td>ScientificName<br>i) Name appropriate to the specimen<br>ii) Referent
   </td>
   <td>Table 2 8.
   </td>
   <td><br>m<br>o
   </td>
   <td><br>☐<br>☐
   </td>
  </tr>
  <tr>
   <td>24
   </td>
   <td>Has image(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>25
   </td>
   <td>Has other media type(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>


**Table 11: ICS proforma for handling of unknown or incomplete data**

<table>
  <tr>
   <th>Item
   </th>
   <th>Requirement
   </th>
   <th>Reference
   </th>
   <th>Status
   </th>
   <th>Support
   </th>
  </tr>

  <tr>
   <td>11.1
   </td>
   <td>Unknown / unspecified datetime “X*” form (ISO 8601-2)
   </td>
   <td>§4.5.1
   </td>
   <td>o.2
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.2
   </td>
   <td>Unknown / unspecified datetime “XXXX-XX-XX” form (ISO 8601-2)
   </td>
   <td>§4.5.1
   </td>
   <td>o.2
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.3
   </td>
   <td>… ...
   </td>
   <td>§4.5.2
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.4
   </td>
   <td>Unknown data term “unknown”
   </td>
   <td>§4.5.3
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.5
   </td>
   <td>
    Unknown data term “unknown:undigitized”
   </td>
   <td>§4.5.3
   </td>
   <td>c11.3:o.3
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.6
   </td>
   <td>
    Unknown data term “unknown:missing”
   </td>
   <td>§4.5.3
   </td>
   <td>c13.3:o.3
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.7
   </td>
   <td>
    Unknown data term “unknown:indecipherable”
   </td>
   <td>§4.5.3
   </td>
   <td>c11.3:o.3
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.8
   </td>
   <td>Withheld data term “known:withheld”
   </td>
   <td>§4.5.3
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11.9
   </td>
   <td>Information element not applicable
   </td>
   <td>§4.5.3
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>

    o.2: It is optional to support one of these items 11.1 and 11.2. \
o.3: IF c11.4, optional to support items 11.5 - 11.7 but all items must be supported.

# 10 Illustrative use cases and guidelines for use (informative)

<div style="color:red">
_To do>> include some illustrative use cases here, drawn from real practice to show what information would typically be published for that use case when complying with, for example MIDS level 2._

_Still to do>>_

*   _Levels need to link to user stories: A certain level should be able to serve some specific stories. Analyse MIDS against DiSSCo user stories – see which levels are needed by which user stories to see what this tells us. Cross-refer to Niels article on user stories._
*   _Review levels against ICEDIG Hannu's MS37/D6.5 proposals to ensure we align._
</div>

# 11 References

[Brummitt 2001]	Brummitt, R.K. (2001). World Geographical Scheme for Recording Plant Distributions, Edition 2. Biodiversity Information Standards (TDWG). [http://www.tdwg.org/standards/109](http://www.tdwg.org/standards/109).

[FMI 2018]	Flanders Marine Institute (2018). IHO Sea Areas, version 3. Available online at [http://www.marineregions.org/](http://www.marineregions.org/). doi: [10.14284/323](https://doi.org/10.14284/323).

[Groom 2019]	Groom G, Dillen M, Hardy H, Phillips S, Willemse L, Wu Z. (2019). Improved standardization of transcribed digital specimen data. Database, Volume 2019, baz129. doi: [10.1093/database/baz129](https://doi.org/10.1093/database/baz129).

[ISO 3166]	International Standards Organisation (ISO) (2013). ISO 3166. Codes for the Representation of Names of Countries and Their Subdivisions. Part 1: Country codes; Part 2: Country subdivision code; and Part 3: Code for formerly used names of countries. [www.iso.org](http://www.iso.org). 

[ISO 8601]	International Standards Organisation (ISO) (2019). ISO 8601. Date and Time — Representations for Information Interchange. Part 1: Basic Rules; and Part 2: Extensions. [www.iso.org](http://www.iso.org).  

[Meyer 2015]	Meyer, Eric T., and Ralph Schroeder. Knowledge machines: digital transformations of the sciences and humanities. MIT Press, 2015.

[Mons 2017]	Mons B, Neylon CD, Velterop J, Dumontier M, da Silva Santos LOB, Wilkinson M (2017) Cloudy, increasingly FAIR; revisiting the FAIR Data guiding principles for the European Open Science Cloud. Information Services and Use, vol. 37, no. 1, pp. 49-56, 2017. doi: [10.3233/ISU-170824](https://doi.org/10.3233/ISU-170824).

[Nelson 2015]	Nelson, G., Sweeney, P., Wallace, L. E., Rabeler, R. K., Allard, D., Brown, H., ... & Gilbert, E. (2015). Digitization workflows for flat sheets and packets of plants, algae, and fungi. Applications in Plant Sciences, 3(9), 1500065. doi: [10.3732/apps.1500065](https://doi.org/10.3732/apps.1500065). 

[RFC 2119]	IETF RFC 2119. (1997).  Key words for use in RFCs to Indicate Requirement Levels. url: [https://www.ietf.org/rfc/rfc2119.txt](https://www.ietf.org/rfc/rfc2119.txt). 

[Schindel 2018] Schindel DE, Cook JA. The next generation of natural history collections. PLoS Biology. 2018 Jul 16;16(7):e2006125. doi: [10.1371/journal.pbio.2006125](https://doi.org/10.1371/journal.pbio.2006125).

[Webster 2017] Webster, MS (ed). The Extended Specimen: Emerging Frontiers in Collections-based Ornithological Research. CRC Press, 2017. ISBN 978-1-315-12045-4.

[Wilkinson 2016]	Wilkinson MD, Dumontier M, Aalbersberg IJ, Appleton G, Axton M, Baak A, Blomberg N, Boiten JW, da Silva Santos LB, Bourne PE, Bouwman J (2016) The FAIR Guiding Principles for scientific data management and stewardship. Scientific data, 3. doi: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18).

END.

 
