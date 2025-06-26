## Why use MIDS?
  
The need to rapidly digitize millions of specimens in Natural History Collections has led to a staged approach for data capture being widely adopted. Mass digitization programs have generally started with the creation of skeletal or stub records, which can then be expanded as more funding or support becomes available. When combined with the previous practice of creating relatively complete data records for each specimen, there is currently a significant variation in the level of digitization both within and between collections.

[The Minimum Information about a Digital Specimen (MIDS) specification](https://github.com/tdwg/mids) has been designed to provide a means of measuring and monitoring the level of digitisation of specimens within a collection. It provides guidance for prioritising the data to be captured as well as recommendations for data standards and mapping structures.


Getting started links[](#getting-started)
-----------------------------------
*   [Normative Information Element & Levels List](https://tdwg.github.io/mids/information-elements/index.html)
*   [Mappings](https://tdwg.github.io/mids/mappings/index.html)
*   [Tools](https://tdwg.github.io/mids/tools/index.html)
*   [About](https://tdwg.github.io/mids/about/index.html)
*   Provide feedback through a [github issue](https://github.com/tdwg/mids/issues)

-------------

## How to use MIDS for digitisation planning

The MIDS standard sits at the heart of all aspects of the digitisation process and can be used to build a digitisation strategy and programme. A digitisation strategy normally includes sections covering the vision, the reasons for digitising, the intended users of the digitised specimens, the scope and prioritisation, the strategic objectives and metrics of success and impact (https://dissco.github.io/DigitisationPlanning/DigPlanning.html). It is easy to see that MIDS is critical for the metrics of success. The mapping of data within MIDS is a key part of building the data structure within a digitisation programme, including mapping to Darwin Core or ABCDEFG and publication on international aggregator portals such as GBIF, GeoCASE, MinDat, etc.

The recommendations included in the MIDS elements will help decision-making about the relevant standards to use, including identifiers. This data structure will also help with managing data in an institutional collections management system (CMS) and with ancillary processes such as citizen science portals.

The different levels of MIDS relate to a staged digitisation programme, which may require different funding, equipment, and workflows for each stage of the process. Using MIDS will help identify costs for each stage of digitisation, as each level has a clearly defined minimum set of information. Each MIDS digitisation level has been defined to reflect a broad use case, helping to build a business case for funding. In addition, the information elements within each MIDS level have a definition and a purpose to support communication to encourage buy-in from colleagues or funders.

## How to use MIDS for prioritisation of digitisation

The information elements within each MIDS level have been selected through a process of discussion and deliberation over several years. These elements represent the data that have formed the basis of many large-scale digitisation programmes, and hence have previously been prioritised or have been agreed as being of high importance at each stage of digitisation.

It was recognised that, at higher MIDS levels, there were sufficient differences in the data between Biology, Geology, and Palaeontology to warrant a distinction between the information elements required at MIDS levels 2 and 3.

The MIDS level aimed at within a digitisation programme will depend on many factors, including funding and local priorities. The definition, purpose, recommendations, and mapping provided by MIDS will enable an institution to determine which level of MIDS is to be selected as the goal for the collection.

It is important to keep in mind that MIDS defines the “Minimum” information at each level, and it is strongly encouraged to capture more information if possible.

## How to calculate MIDS

The MIDS score can be calculated for an individual specimen by assessing the information required for each MIDS level and the information present in the digitised specimen. The data can be mapped to [Darwin Core terms](https://www.tdwg.org/standards/dwc/) or the [Access to Biological Collection Data (ABCD) Schema](https://www.tdwg.org/standards/abcd/) and then to the [MIDS information elements](https://tdwg.github.io/mids/information-elements/index.html) using the [mapping examples](https://tdwg.github.io/mids/mappings/index.html) provided.

To make the calculations easier, [tools](https://tdwg.github.io/mids/tools/index.html) are being developed to enable the MIDS score to be calculated for each specimen within large datasets. These tools work on existing datasets in the [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) or the [Distributed System of Scientific Collections](https://www.dissco.eu/) or users can create their own datasets in Darwin Core Archive format ([Guidance](https://ipt.gbif.org/manual/en/ipt/latest/dwca-guide)) or in [ABCD format](https://www.tdwg.org/standards/abcd/). These tools make calculating the MIDS score for large collections possible, as well as providing the results in a format to enable users to understand the data which are impacting the MIDS score.

*Last Updated: 12 June 2025*
