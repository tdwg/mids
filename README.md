# MIDS Task Group (Minimum Information about a Digital Specimen) 

This is the repository for the MIDS Task Group, dealing with Minimum Information about a Digital Specimen.

This README last updated: 15 May 2024.

## About the group

The [MIDS Task Group](https://www.tdwg.org/community/cd/mids/) is a task group to develop a standard for Minimum Information about a Digital Specimen (MIDS). The TG is chartered by its parent [Collection Descriptions Interest Group](https://www.tdwg.org/community/cd/). For full details of the TG and its scope, [read the charter](https://www.tdwg.org/community/cd/mids/).

The day-to-day operations of the Task Group is documented in this repository. You can also track and participate in the work of the group by watching this repository and monitoring the group's [issues tracker](https://github.com/tdwg/mids/issues). To be sure of hearing about meetings and updates join the group's  [mailing list](http://lists.tdwg.org/mailman/listinfo/tdwg-mids)

The MIDS specification will be complementary to the Collection Descriptions standard that is also under the responsibility of the [Collection Descriptions Interest Group](https://www.tdwg.org/community/cd/).

## How to become involved and contribute
This Task Group welcomes anyone who has a practical interest in minimum information standards, Digital Specimen information, experience with digitisation processes and workflows and the subsequent management (including making public) of the outputs of digitisation, including reporting requirements for management and funding agencies.

Become involved and contribute by:

- Contacting the Conveners and/or signing up to the [task group mailing list](http://lists.tdwg.org/mailman/listinfo/tdwg-mids).
  
- Participating in the meetings. The timing of these are currently weekly on Thursdays at 14:00 UTC. Contact the Conveners for more information.

- Watching this github repository. Submitting or commenting on an issue.

- Using and evaluating the the specification as it emerges and providing feedback e.g., by submitting an issue or suggesting a new need.

## Members

### Conveners

| Name | Affiliation | github name / Email |
| --- | --- | --- |
| Elspeth Haston | Royal Botanic Garden Edinburgh | @emhaston / ehaston AT rbge.org.uk|  
| Cat Chapman | Florida Museum of Natural History |  / cchapman AT floridamuseum |  

### Previous Conveners

Alex Hardisty, formerly Director of Informatics Projects, Cardiff University

### Core Members

| Name | Affiliation | github name / Email |  
| --- | --- | --- |  
| Wouter Addink | Naturalis Biodiversity Center | @wouteraddink |
| Christian Bölling | Museum für Naturkunde Berlin (MfN) | @cboelling |  
| Mathias Dillen | Meise Botanic Garden | @matdillen |
| Gabriele Dröge | Botanic Garden and Botanical Museum Berlin | @gdadade |
| Dag Endresen | University of Oslo, Natural History Museum | @dagendresen |  
| Falko Glöckler | Museum für Naturkunde Berlin (MfN) | falko.gloeckler AT mfn.berlin |
| Quentin Groom | Meise Botanic Garden | @qgroom |
| Anton Güntsch | Botanic Garden and Botanical Museum Berlin | a.guentsch AT bgbm.org |
| Josh Humphries | Natural History Museum, London | @jrdh |
| Pieter Huybrechts | Meise Botanic Garden | @PietrH |
| Chris Hunter | GigaDB, BGI Group | @only1chunts |
| Gunnhild Marthinsen | University of Oslo Natural History Museum | g.m.marthinsen AT nhm.uio.no |
| Ben Norton |  | <michaelnorton.ben@gmail.com> |
| Deborah Paul | University of Illinois Urbana-Champaign / Species File Group | @debpaul |
| Richard Pyle | Bernice Pauahi Bishop Museum | deepreef AT bishopmuseum.org |
| Mareike Petersen | Museum für Naturkunde Berlin (MfN) | mareike.petersen AT mfn.berlin |
| Richard Rabeler | University of Michigan Herbarium | rabeler AT umich.edu |
| Eirik Rindal | University of Oslo Natural History Museum | eirik.rindal AT nhm.uio.no |
| Hannu Saarenmaa | Bioshare Digitization | hannu AT bioshare.com |
| Lutz Suhrbier | Botanic Garden and Botanical Museum Berlin | l.suhrbier AT bgbm.org |
| Maarten Trekels | Meise Botanic Garden | @mtrekels |
| Dagmar Triebel | The Bavarian Natural History Collections (SNSB) | triebel AT snsb.de  |
| Rachel Walcott | National Museums Scotland | r.walcott AT nms.ac.uk |
| Claus Weiland  | Senckenberg Society for Nature Research  | @cp-weiland |
| Karin Wiltschke | Natural History Museum Vienna | @Karin-Wiltschke |


## Repo structure

The [main branch](https://github.com/tdwg/mids) contains the current documentation, including the most recently released draft version of the standard, the information elements and the mapping.

The [working-draft branch](https://github.com/tdwg/mids/tree/working-draft) contains the different versions of the standard during its development including the [current draft](https://github.com/tdwg/mids/tree/working-draft/current-draft) which is being actively updated. Older drafts are moved to the [old-drafts](https://github.com/tdwg/mids/tree/working-draft/old-drafts) folder as they are superseded. The [use-cases](https://github.com/tdwg/mids/tree/working-draft/use-cases) folder contains the use cases on which the current working draft is based.

## TG Way of working

### Repo, email and meetings
The [github repository TDWG TG MIDS](https://github.com/tdwg/mids) together with the [TG mailing list](http://lists.tdwg.org/mailman/listinfo/tdwg-mids) and regular TG meetings is the way of working.

[Github issues](https://github.com/tdwg/mids/issues) and their [status labels](https://github.com/tdwg/mids/labels) provide the main way of keeping track of issues, discussions and progress.

Github issues are used in two ways to make progress. Labels indicate the kind of issue and other information. See issue label meanings below.

Issues labelled with the black 'MIDS Element' label are used to hold the working definition of a specific MIDS information element. Other labels (MIDS-0, MIDS-1, MIDS-2, MIDS-3) indicate which MIDS levels the information belongs to.  

All other issues than MIDS Element issues are used to raise issues (concerns) relating to the specification, such as bugs, suggestions for improvement, request for clarification, etc.

## Resources

MIDS is being developed within the following structure:

**MIDS Levels** - Four levels have been defined and can be found [here](https://github.com/tdwg/mids/tree/main/standard/mids-levels)

**MIDS Information Elements** - The information elements have been defined and can be found [here](https://github.com/tdwg/mids/tree/main/standard/information_elements)

**MIDS SSSOM Mapping** - The elements of each MIDS level have been mapped to terms as used in common domain data standards, such as Darwin Core or ABCD and can be found [here](https://github.com/tdwg/mids/tree/main/sssom-mapping)

**MIDS Wiki** - A wiki is being developed to provide more information on the terms and concepts represented in MIDS, and guidance on how the MIDS may be used in practice. This can be found [here](https://github.com/tdwg/mids/wiki/)

**MIDS Implementations** - The following implementations have been developed and can be tested by users.
- **MIDS Calculator** - The [MIDS Calculator](https://github.com/AgentschapPlantentuinMeise/MIDSCalculator) developed at Meise Botanic Garden uses a zipped GBIF annotated Darwin Core Archive. This enables the user to define their own dataset from GBIF. It also enables the implementation of value permissions for some of the information elements.
- **MIDS Checker** - The [MIDS Checker](https://naturalhistorymuseum.github.io/gamc/
) developed at the Natural History Museum London interacts directly with the GBIF API. This allows a more direct calculation, although constrained by the data available via the API and is restricted to predefined datasets in GBIF.

### Most recent draft of the specification
We are currently developing the documentation in an updated structure on GitHub. Until this is in place, the most recent draft of the MIDS specification can be found here: 
[MIDS-definition-v0.17-13Jul2023](https://github.com/tdwg/mids/blob/working-draft/current-draft%20/MIDS-definition-v0.17-13Jul2023.md)
Cite as:
*tbc*

### Earlier drafts:
[MIDS-definition-v0.16-28May2022](https://github.com/tdwg/mids/blob/working-draft/old-drafts/MIDS-definition-v0.16-28May2022.md)
Cite as:
*Haston, E., Hardisty, A., Addink, W., Dillen, M., Groom, Q., Chapman, C. et al. (Draft) Minimum Information about a Digital Specimen (MIDS) v0.16, 28 May 2022*.

[MIDS-definition-v0.14-29Mar2021](https://github.com/tdwg/mids/blob/working-draft/old-drafts/MIDS-definition-v0.14-29Mar2021.md)
Cite as:
*Hardisty, A., Addink, W., Dillen, M., Groom, Q., Haston, E., et al. (Draft) Minimum Information about a Digital Specimen (MIDS) v0.14, 29 Mar 2021*.

### Other resources
Borsch, T., Stevens, A.-D., Häffner, E., Güntsch, A., Berendsohn, W.G., et al. (2020): A complete digitization of German herbaria is possible, sensible and should be started now. Research Ideas and Outcomes 6: e50675. https://doi.org/10.3897/rio.6.e50675.

iDigBio MISC Data Element Catalog (Phase 1, V0, rev. 15 December 2012). https://www.idigbio.org/wiki/images/c/c9/Phase_I_Report.pdf.   

