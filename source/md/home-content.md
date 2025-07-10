## What is MIDS?

The Minimum Information about a Digital Specimen (MIDS) standard has been designed to provide a means of measuring and monitoring the level of digitization of specimens within a collection. It provides guidance for prioritizing the data to be captured as well as recommendations for data standards and mapping structures.

MIDS specifies the information elements expected to be present when providing access to specimens within a digital framework. Digital specimens are online digital representations of their physical counterparts in natural science collections. The definition of digitization used here is making physical objects digitally available in terms of data and/or media. Several 'levels of digitization' (0-3) represent a simple categorization of the type and depth of digitization achieved by different approaches to digitization. These are defined in detail in the [Information Elements](https://tdwg.github.io/mids/information-elements/index.html) page.

The need to rapidly digitize millions of specimens in Natural History Collections has led to a staged approach for data capture being widely adopted. Mass digitization programs have generally started with the creation of skeletal or stub records, which can then be expanded as more funding or support becomes available. When combined with the previous practice of creating relatively complete data records for each specimen, there is currently a significant variation in the level of digitization both within and between collections.

MIDS defines what information about a specimen should be available but it does not attach specific value to that information because attaching value depends both upon the information itself and the purpose to which that is put.

Getting started links[](#getting-started)
-----------------------------------
*   [Normative Information Element & Levels List](https://tdwg.github.io/mids/information-elements/index.html)
*   [Mappings](https://tdwg.github.io/mids/mappings/index.html)
*   [Tools](https://tdwg.github.io/mids/tools/index.html)
*   [About](https://tdwg.github.io/mids/about/index.html)
*   Provide feedback through a [github issue](https://github.com/tdwg/mids/issues)

-------------
## Aims

- To provide a metric for the digitisation of collections
- To assist in the prioritisation of data to be published to make digital specimen information useful for multiple purposes of research, teaching and learning

Outcomes of these aims include:

- To improve the quality of published data by providing recommendations to collection managers about relevant data standards and ontologies
- To support and contribute towards assessments of fitness for purpose of data (suitability) for feeding specific types of data processing pipelines
- To assist researchers to know what information to include in their publications about specimens they have used in their research
- To enable efficient querying, aggregation and self-contained data processing by computing systems (machine-actionability, de Smedt 2020) based on provision of rich contextual (meta)data in compliance with the FAIR principles (Wilkinson 2016)


## Audience

This document is intended primarily for those who are responsible for digitizing and sharing data publicly (publishing data) about natural science specimens. It can also be useful to those who are developing applications, tools and workflows related to digitization, comparing and evaluating digitization projects, and for those reporting to collection management personnel, and funding agencies. Whilst it may be possible to use the specification for occurrence information that are not physical specimens, it has not been designed for this wider use.

## MIDS levels

The Minimum Information about a Digital Specimen (MIDS) framework offers a clear way to assess and standardise the degree of digitization of specimen data across collections. This ensures consistent data capture and improves its usability for scientific research. There are four progressive levels (0-3), each building on the previous one:

### MIDS Level 0 (Bare):

> A minimal record that links a specimen to an identifier (e.g., a register number or barcode). It confirms the specimen's existence but includes no detailed information, laying the groundwork for further digitization.

### MIDS Level 1 (Basic):

> Adds basic taxonomic details (e.g., species name) and physical information about the specimen. This allows for basic searchability and gives a simple representation of the collection for internal and external users.

### MIDS Level 2 (Regular):

> Expands on Level 1 with more detailed data, such as geographic and temporal information, collection event details, and multimedia like images. This level supports more thorough scientific research.

### MIDS Level 3 (Extended):

> The most detailed level, linking the specimen to external datasets through persistent identifiers (e.g., Publication DOIs). This significantly boosts research potential by connecting the specimen to specialised data across different platforms.

## How to use MIDS for digitization planning

The MIDS standard sits at the heart of all aspects of the digitization process and can be used to build a digitization strategy and programme. A digitization strategy normally includes sections covering the vision, the reasons for digitizing, the intended users of the digitized specimens, the scope and prioritization, the strategic objectives and metrics of success and impact (https://dissco.github.io/DigitisationPlanning/DigPlanning.html). It is easy to see that MIDS is critical for the metrics of success. The mapping of data within MIDS is a key part of building the data structure within a digitization programme, including mapping to Darwin Core or ABCDEFG and publication on international aggregator portals such as GBIF, GeoCASE, MinDat, etc.

The recommendations included in the MIDS elements will help decision-making about the relevant standards to use, including identifiers. This data structure will also help with managing data in an institutional collections management system (CMS) and with ancillary processes such as citizen science portals.

The different levels of MIDS relate to a staged digitization programme, which may require different funding, equipment, and workflows for each stage of the process. Using MIDS will help identify costs for each stage of digitization, as each level has a clearly defined minimum set of information. Each MIDS digitization level has been defined to reflect a broad use case, helping to build a business case for funding. In addition, the information elements within each MIDS level have a definition and a purpose to support communication to encourage buy-in from colleagues or funders.

## How to use MIDS to prioritize digitization

The information elements within each MIDS level have been selected through a process of discussion and deliberation over several years. These elements represent the data that have formed the basis of many large-scale digitization programmes, and hence have previously been prioritized or have been agreed as being of high importance at each stage of digitization.

It was recognized that, at higher MIDS levels, there were sufficient differences in the data between Biology, Geology, and Palaeontology to warrant a distinction between the information elements required at MIDS levels 2 and 3.

The MIDS level aimed at within a digitization programme will depend on many factors, including funding and local priorities. The definition, purpose, recommendations, and mapping provided by MIDS will enable an institution to determine which level of MIDS is to be selected as the goal for the collection.

It is important to keep in mind that MIDS defines the “Minimum” information at each level, and it is strongly encouraged to capture more information if possible.

## How to calculate MIDS

The MIDS score can be calculated for an individual specimen by assessing the information required for each MIDS level and the information present in the digitised specimen. The data can be mapped to [Darwin Core terms](https://www.tdwg.org/standards/dwc/) or the [Access to Biological Collection Data (ABCD) Schema](https://www.tdwg.org/standards/abcd/) and then to the [MIDS information elements](https://tdwg.github.io/mids/information-elements/index.html) using the [mapping examples](https://tdwg.github.io/mids/mappings/index.html) provided.

To make the calculations easier, [tools](https://tdwg.github.io/mids/tools/index.html) are being developed to enable the MIDS score to be calculated for each specimen within large datasets. These tools work on existing datasets in the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) or the [Distributed System of Scientific Collections](https://www.dissco.eu/) or users can create their own datasets in Darwin Core Archive format ([Guidance](https://ipt.gbif.org/manual/en/ipt/latest/dwca-guide)) or in [ABCD format](https://www.tdwg.org/standards/abcd/). These tools make calculating the MIDS score for large collections possible, as well as providing the results in a format to enable users to understand the data which are impacting the MIDS score.

*Last Updated: 12 June 2025*
