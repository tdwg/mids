# Use cases for MIDS <!-- omit in toc -->

This document describes many (but probably not all) of the use cases foreseen for MIDS. These are described in a functional manner i.e., what must be made possible by the MIDS specification when it has been implemented in processes, workflows and systems (software).

Each use case is supported by one or more collected user stories of the form:

> As a *role* I want to *perform some activity* So that *I can achieve some outcome*. For this I need *something*.

A few of the use cases (8, 10, 11) imply coverage and characteristics of the MIDS specification that are of a non-functional nature i.e., features and characteristics that ultimately affect the end-user experience and which contribute to achieving the functional capabilities but which are elements of the specification rather than its implementation. These are informed, for example by user stories that ask for unambiguity in the specification. Such requirements are marked "NFR".

<p style="color:blue">
Status (04 Nov 2020): User stories collected during the inaugural meeting of the TG (23 September 2020) have been inserted here as evidence for the relevant use case.
<br>i) A further step is needed to review each use case to ensure it adequately captures the nuances of each user story.
<br>ii) There are several groups of expressed user stories from which functional use cases can be derived but where further work is needed (use cases 8 - 13), for example to consider the meaning of completeness and to consider what is in/out of scope in respect of image metadata.
<br>iii) There is a large body of user stories relating to completeness but it is not clear what is meant by 'complete'. Clearly it's an important need that needs to be further teased apart.
</p>

- [Use case 1: Automatically calculate MIDS level](#use-case-1-automatically-calculate-mids-level)
- [Use case 2: Crowdsourcing specimen data from transcription](#use-case-2-crowdsourcing-specimen-data-from-transcription)
- [Use case 3: Assess level of digitization](#use-case-3-assess-level-of-digitization)
- [Use case 4: Count/identify items needing digitization](#use-case-4-countidentify-items-needing-digitization)
- [Use case 5: Create a bare description of a specimen](#use-case-5-create-a-bare-description-of-a-specimen)
- [Use case 6: Assign persistent identifier](#use-case-6-assign-persistent-identifier)
- [Use case 7: Information elements for specific purposes](#use-case-7-information-elements-for-specific-purposes)
- [Use case 8: ...Avoid ambiguity, close off options, making information comparable ... (NFR)](#use-case-8-avoid-ambiguity-close-off-options-making-information-comparable--nfr)
- [Use case 9: ... something to do with completeness - words to be worked out ...](#use-case-9--something-to-do-with-completeness---words-to-be-worked-out-)
- [Use case 10: ... something to do with image characteristics ... (probably NFR)](#use-case-10--something-to-do-with-image-characteristics--probably-nfr)
- [Use case 11: ... something to do with data quality ... (probably NFR)](#use-case-11--something-to-do-with-data-quality--probably-nfr)
- [Use case 12: ... something to do with being able to identify missing values or empty fields ...](#use-case-12--something-to-do-with-being-able-to-identify-missing-values-or-empty-fields-)
- [Use case 13: ... something to do with helping with project management ...](#use-case-13--something-to-do-with-helping-with-project-management-)

## Use case 1: Automatically calculate MIDS level

Automatically calculate the MIDS level from information fields in a specimen data record in an institutional collection management system (CMS) according to a logical, deterministic algorithm. This is needed per record and as an average for a collection.

> As a curator or collections manager I want to view the MIDS profile of my collection So that I can prioritize digitization. For this I need a MIDS level calculation for each specimen.
> 
> As a funder I want verifiable information about the level to which specimens in projects I fund have been digitized So that I can verify whether the project was successful. For this I need clearly defined and verifiable (in an automated way) digitization levels.
> 
> As a programmer I want to calculate MIDS for a dataset (specimen data record(s)) So that I can provide a service. For this I need a totally unambiguous logical standard that I can apply programmatically.
> 
> As an IT manager I want to create KPIs (Key Performance Indicators) for my boss So that they see I do something. For this I need some value that reflects the enrichment of data.
> 
> As a museum administrator I want to know what are the MIDS levels for each of the collections in my institution So that I can decide how to partition funds. For this I need bravery(!).
> 
> As a Policy Maker I want to assess the digitization level of a collection So that funding can be (re )allocated.
>
> As a public relations/principal investigator I want to report on the digitization progress So that I can inform the public/funders. *Also appears under use case 1.*
> 
> As a museums director I want to know the development of digitization process in the different collections and the MIDS level So that I can see progress. *Also appears under use case 1.*

## Use case 2: Crowdsourcing specimen data from transcription

*To be reviewed.*
Mapping MIDS level 2 information elements into (for example) a Zooniverse project for specimen label data transcription. 

> As a citizen scientist tool author/manager I want to find level 0 specimens So that I can distribute them for citizen scientist digitization.

## Use case 3: Assess level of digitization

Use MIDS definition to assist assessment(s) of the completeness or comprehensiveness of digitization across collections of specimens e.g., for collection digitization dashboard purposes. 

*To be considered: Does this use case fulfil the needs of the 'completeness' user stories below?*

## Use case 4: Count/identify items needing digitization

Count/identify the specimens needing digitization e.g., because they only have a skeletal catalogue record in a Collection Management System.

> As a curator I want to compare the digitization levels of my different collections So that I can prioritize digitization. For this I need just the average MIDS level.
> 
> As an IT manager I want to create KPIs (Key Performance Indicators) for my boss So that they see I do something. For this I need some value that reflects the enrichment of data.

## Use case 5: Create a bare description of a specimen

Create a bare description (skeletal catalogue record) of a specimen e.g., physical specimen identifier such as barcode or catalogue number, institution where the specimen is kept, short description of the specimen (not necessarily its scientific name/identification).

## Use case 6: Assign persistent identifier

Assign a persistent identifier (PID) to a specimen and its digital data as early as possible in the digitization process (even prior to digitization commencing) to support the open data goal of making digital specimen data publicly available without ambiguity.

> As a (journal, book) Publisher I want to point explicitly to individual digital objects So that authors can specify exactly which objects they are referring to. For this I need something like a DOI /PID.
> 
> As a Herbarium database manager I would like to avail as much data as possible to the public for research and posterity. 

## Use case 7: Information elements for specific purposes

Publish information in specified information elements to be available as part of the minimum information.

*Too vague - the user story examples below are just a few. There are probably lots more involving all kinds of information elements. However, knowing things like the materialtype/preparation and the disposition of a specimen can be important. Tighten up the use case name and description.* 

*[DwC definition of preparations](http://rs.tdwg.org/dwc/terms/preparations)*
*[DwC definition of disposition](http://rs.tdwg.org/dwc/terms/disposition)*
*Identifiable as fossil records, georeference, Chronostrat (Period, Age), Lithostrat.*
*Accession date, how did it come into museum's hands, was it a 'sensible' accession for the time.*
*Taxon, stratigraphy, geography, etc.*

> As a collection manager I want to know what proportion of the collections are stored in Ethanol So that I can make a plan to meet the fire safety requirements. For this I need to know the material type of items in my collections, and where it is stored.
> 
> As a paleontologist I want to look at geographic distributions of Ordovician fossils So that I can see how they have changed through the Ordovician (a time of heightened diversification and extinction). For this I need fossil records (identified at a minimum to genus level), georeference, Chronostrat (Period, Age), Lithostrat.
> 
> As a scientist or curator or museums director I want to obtain information about how this object came to the museum So that I can evaluate if it came in a now sensible way. For this I need the date it came in, how it came in (collected, purchased, stolen, etc.) and a field with a possible context saying sensible. 
> 
> As a collections manager/curator I want to locate a specimen/group of specimens based on the organisation principal on which it is based (e.g., taxon, stratigraphy, geography, etc., or a combination) So that I can respond to a visiting researcher. For this I need the core data by which the collection is organised.

## Use case 8: ...Avoid ambiguity, close off options, making information comparable ... (NFR)

*To be completed.* *Non-functional requirement. Speaks to ICS proforma, section 9 (conformance) in draft v0.12.* *A couple of the user stories under other use cases allude to this non-functional requirement too.*

> As a Software Developer I want to use the different MIDS levels as guidance to focus initial development of new software on the most relevant fields first So that early software prototypes can already deliver relevant data and later releases follow the higher MIDS levels.
> 
> As a software developer I want to find specimen records at specific MIDS levels So that I can make assumptions in my code about which fields will and won't be present in the records (so that I don't have to do extensive checks over the record's fields when processing/analysing them).

## Use case 9: ... something to do with completeness - words to be worked out ...

*To be completed.* *To what extent is the notion of completeness served by the deterministic algorithm mentioned as part of use case 1?*

*There are a large number of user stories that refer to completeness. Keywords identifiable in these stories include: completeness, accuracy, gaps, multiple collection/catalog numbers and other values (=repetition of fields), depth of digitization.*

> As a collections manager I want oversight of the completeness of records at various levels So that I can focus resources on gap filling based on demands.
> 
> As a Digizitation Manager I want to know the (planned/targeted) depth of digitization So that I can assign staff/money to that collection.
> 
> As a computer scientist I want to understand level of completeness across duplicated specimens So that I can mobilise annotations to duplicates following duplicate clustering.
> 
> As a collections manager and researcher (scientist, historian) I want to find specimens in other collections that are duplicates of specimens I might have in my collection So that I can match up duplicate specimens and both annotate my specimens with the information already out there - and reduce duplication of effort in digitizing my own collection, and accidentally diverging records. For this I need core fields that are likely on those duplicates, including collector name, location (including possibly verbatim strings of text), any collection numbers (there may be multiple different numbers), collection dates, collection donors (e.g., historic sets of specimens).
> 
> As a data creator I want to know what fields in the collection records need focussed attention So that I can develop new streamlined workflows to maximize efficiency in entering data (Where are the holes? How can they plugged most efficiently by using patterns and data now available with the bigger data sets?).
> 
> As a collection manager I want to find all herbarium records created in year 2020, in different completeness level So that I can make a report for the management.
> 
> As a collections manager I want to assess digitization effort and completeness So that the importance and value of the collection can be promoted to leadership, funders, the public and strategically managed.
> 
> As a collection manager I want to see the record completeness visualized So that I can understand where best to spend effort to work on completeness. For this I need to have a system where fields that are NULL can be grouped. I would also need some way to indicate that originally, not all data was captured from primary source(s).
> 
> As a contributor to GBIF I want to others to know the value (completeness and accuracy) of the overall record that my institution is providing, meta-data about record completeness, known field-level deficiencies, location of additional data, and finally a field to indicate last internal review data of the provided record So that all values provided are explicit and a “user” of the record does not need to spend time contacting my institution for missing data because they don’t understand why data are missing.  Why? Because time is money and there are not currently adequate funds for digitization or frequently reviewing individual records. For this I need: controlled vocabularies for key fields (explicit reasons for missing data - for example “does not exist, not legible, not recorded”); record-level assessment fields (good, bad, ugly).
> 
> As a researcher I want to be able to find as many records of a species as possible So that my distribution reporting will be comprehensive. For this I need to have more records published that include more data than just MIDS 1i.
> 
> As a decision maker in a government department I want to work with ‘the best’ data for the species I’m interested in (e.g. threatened species) So that I don’t have to spend time culling records that are very poor or incomplete. For this I need an indication of completeness in records as a start point for further filtering to obtain a dataset I can work with. 
> 
> As a citizen scientist or volunteer I want to know what records are incomplete and require my assistance to transcribe So that I know where my efforts will have the greatest impact. For this I need to know what records are openly licensed.
> 
> As a Collection Manager I want to be able to assess the completeness of my data records So that data I am publishing is of reasonably even quality. For this I need a comparative standard for judging this. *Also appears under the data quality use case.*
> 
> As a digitization project manager/lead I want to know what progress has been made in a very large digitization project across multiple collection types each using different capture methods and at different scales (amount of info captured) So that I can see progress on a dashboard and address any issues or assess where additional resources are required as well as share this with higher management. For this I need access to the data at standardized levels (MIDS) so they can be easily compared.
> 
> As a public relations/principal investigator I want to report on the digitization progress So that I can inform the public/funders. *Also appears under use case 1.*
> 
> As a museums director I want to know the development of digitization process in the different collections and the MIDS level So that I can see progress. *Also appears under use case 1.*
> 
> As a collection administrator I want to be able to guide the collecting efforts and create a loans plan in my institution So that the limited budget is optimized for impact. For this I need an easy way to grade the level of “completeness” and “quality” of the current information in my collection database. *Also appears under the data quality use case.*

## Use case 10: ... something to do with image characteristics ... (probably NFR)

*To be completed. Need to decided what is in scope and what is out of scope in respect of details about images* *Image types and image characteristics - former might be in scope latter might be out of scope.*

> As a Data manager I am missing pointers to best practices and recommendations for image meta(data) and inclusion of terms relating to images e.g., region of interest (ROI) pixel corner position. 
> 
> As a trait extraction tool I want to select all specimens that have images of the object So that I can use the images to extract the traits. For this I need to find the specimen records that have images of a certain type (object images).
> 
> As a CMS provider I want to understand workflows and desired outcomes So that we can support workflows with software in some form. For this I need standards -- possibly for images as well as data if we are looking at OCR for labels (does every image have a label?, should those with labels be identifiable?,  what dpi is required for best OCR outcomes?)

## Use case 11: ... something to do with data quality ... (probably NFR)

*To be completed.* 

> As a funder (and as an applicant to grants) I want to easily filter specimens with different levels of information quality (geographical, taxonomical, time) So that I can create particular lists and distribution maps of the specimens (my country, threatened species, current vs. last years) - To demonstrate what impact could the support of certain collecting, digitization and identification efforts have in the overall information available for certain uses.
> 
> As a Collection Manager I want to be able to assess the completeness of my data records So that data I am publishing is of reasonably even quality. For this I need a comparative standard for judging this. *Also appears under the completeness use case.*
> 
> As a collection administrator I want to be able to guide the collecting efforts and create a loans plan in my institution So that the limited budget is optimized for impact. For this I need an easy way to grade the level of “completeness” and “quality” of the current information in my collection database. *Also appears under the completeness use case.*

## Use case 12: ... something to do with being able to identify missing values or empty fields ...

*To be completed. This is the unknown values for fields (section 4.5 of the current draft v0.12)* 

> As a researcher I want to know how many records include a locality string but are not georeferenced (for my (taxonomic and/or geographic) group of interest) So that I can plan a georeferencing effort / grant. For this I need to know if the locality field is populated, along with other potential locality-related fields.

## Use case 13: ... something to do with helping with project management ...

*To be completed.* *Or is this in the completeness category?* 

> As a collection manager I want to cure my addiction to creating skeleton records So that I have a cleaner database & publishing pipeline. For this I need time/coffee or a sanity-check (when is it too pipe-dreamy to pin our hopes on OCR/ML for auto-transcribing images, and worth continuing to do more the manual way?) Granted, this is institution/funding specific, not strictly a matter of the currently viable technologies, but interested in where might MIDS help with project management/prioritization?


END.