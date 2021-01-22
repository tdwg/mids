# MIDS Task Group (Minimum Information about a Digital Specimen) 

This is the repository for the MIDS Task Group, dealing with Minimum Information about a Digital Specimen.

This README last updated: 03 November 2020.

## About the group

The [MIDS Task Group](https://www.tdwg.org/community/cd/mids/) is a task group to develop a standard for Minimum Information about a Digital Specimen (MIDS). The TG is chartered by its parent [Collection Descriptions Interest Group](https://www.tdwg.org/community/cd/). For full details of the TG and its scope, [read the charter](https://www.tdwg.org/community/cd/mids/).

The day-to-day operations of the Task Group is documented in this repository. You can also track and participate in the work of the group by watching this repository and monitoring the group's [issues tracker](https://github.com/tdwg/mids/issues).

The new MIDS standard will be complementary to the Collection Descriptions standard that is also under the responsibility of the [Collection Descriptions Interest Group](https://www.tdwg.org/community/cd/).

## How to become involved and contribute
This Task Group welcomes anyone who has a practical interest in minimum information standards, Digital Specimen information, experience with digitization processes and workflows and the subsequent management (including making public) of the outputs of digitization, including reporting requirements for management and funding agencies.

Become involved and contribute by:

- Contacting the Conveners and/or signing up to the [task group mailing list](http://lists.tdwg.org/mailman/listinfo/tdwg-mids).

- Watching this github repository. Submitting or commenting on an issue.

- Using and evaluating the the specification as it emerges and providing feedback e.g., by submitting an issue or suggesting a new need.

## Members

### Conveners

| Name | Affiliation | github name / Email |
| --- | --- | --- |
| Alex Hardisty | Cardiff University | @hardistyar / hardistyar AT cardiff.ac.uk|  
| Elspeth Haston | Royal Botanic Garden Edinburgh | @emhaston / ehaston AT rbge.org.uk |  

### Core Members

| Name | Affiliation | github name / Email |  
| --- | --- | --- |  
| Wouter Addink | Naturalis Biodiversity Center | @wouteraddink |  
| Mathias Dillen | Meise Botanic Garden | @matdillen |  
| Falko Glöckler | Museum für Naturkunde Berlin (MfN) | falko.gloeckler AT mfn.berlin |
| Quentin Groom | Meise Botanic Garden | @qgroom |
| Anton Güntsch | Botanic Garden and Botanical Museum Berlin | a.guentsch AT bgbm.org |
| Josh Humphries | Natural History Museum, London | @jrdh |
| Chris Hunter | GigaDB, BGI Group | chris AT gigasciencejournal.com> |
| Gunnhild Marthinsen | University of Oslo Natural History Museum | g.m.marthinsen AT nhm.uio.no |
| Deborah Paul | Florida State University / iDigBio | @debpaul |
| Mareike Petersen | Museum für Naturkunde Berlin (MfN) | mareike.petersen AT mfn.berlin |
| Richard Rabeler | University of Michigan Herbarium | rabeler AT umich.edu |
| Eirik Rindal | University of Oslo Natural History Museum | eirik.rindal AT nhm.uio.no |
| Hannu Saarenmaa | Bioshare Digitization | hannu AT bioshare.com |
| Lutz Suhrbier | Botanic Garden and Botanical Museum Berlin | l.suhrbier AT bgbm.org |
| Rachel Walcott | National Museums Scotland | r.walcott AT nms.ac.uk |

## Repo structure

The [master branch](https://github.com/tdwg/mids) contains this README.md file and the [released public version](MIDS-definition.md) of the MIDS specification. As of 03 November 2020, work is still in progress and there is not yet a released Version 1.0 of the specification.

The [working-draft branch](https://github.com/tdwg/mids/tree/working-draft) contains the current working draft in the [current-draft](https://github.com/tdwg/mids/tree/working-draft/current-draft) folder. Older drafts are moved to the [old-drafts](https://github.com/tdwg/mids/tree/working-draft/old-drafts) folder as they are superseded. The [use-cases](https://github.com/tdwg/mids/tree/working-draft/use-cases) folder contains the use cases on which the current working draft is based.

## TG Way of working

### Repo, email and meetings
The [github repository TDWG TG MIDS](https://github.com/tdwg/mids) together with the [TG mailing list](http://lists.tdwg.org/mailman/listinfo/tdwg-mids) and regular TG meetings is the way of working.

[Github issues](https://github.com/tdwg/mids/issues) and their [status labels](https://github.com/tdwg/mids/labels) provide the main way of keeping track of issues, discussions and progress.

Github issues are used in two ways to make progress. Labels indicate the kind of issue and other information. See issue label meanings below.

Issues labelled with the black 'MIDS Element' label are used to hold the working definition of a specific MIDS information element. Other labels (MIDS-0, MIDS-1, MIDS-2, MIDS-3) indicate which MIDS levels the information belongs to. These MIDS Elements are also labelled with a 'status: ...' label to indicate current discussion/agreement status. The values for this label are listed below, together with an explanation of the allowed state transitions.

All other issues than MIDS Element issues are used to raise issues (concerns) relating to the specification, such as bugs, suggestions for improvement, request for clarification, etc. These are labelled appropriately according to the second half of the list below.

### Issue label meanings

| **Label** | **Meaning** |
| ---- | ---- |
| MIDS Element | Defines and tracks progress towards agreement on a MIDS information element that appears at one or more MIDS levels. |
| MIDS-0 | Info element appears at MIDS level 0. |
| MIDS-1 | Info element appears at MIDS level 1. |
| MIDS-2 | Info element appears at MIDS level 2. |
| MIDS-3 | Info element appears at MIDS level 3. |
| | |
| status: ... | Status value of MIDS Element definition. *See next subsection for possible status values.* |
| | |
| specification | improvements, additions, changes needed to the specification text |
| question | Further information is requested |
| bug | Something isn't working |
| duplicate | This issue or pull request already exists |
| enhancement | New feature, function or request |
| good first issue | Good for newcomers |
| help wanted | Extra help is needed with this issue |
| invalid | This does not seem right |
| wontfix | This will not be worked on |

### Status values of MIDS Element definitions
A MIDS Element definition can have one of five statuses, as listed in the following table

| **Status label value** | **Meaning** |
| ---- | ---- |
| status: not yet discussed | The element has not been discussed yet. |
| status: under discussion | The element is being discussed in the task group. |
| status: agreed | The definition of the element at the level it appears at has been agreed by the task group. |
| status: accepted in specification | The agreed element definition has been written into the draft specification.  |
| status: has issues | The element definition has issues associated with it. |

### Allowed state transitions
The normal flow of state transitions for MIDS Element issues is the following:

*Not yet discussed* --> *under discussion* --> *agreed* --> *accepted into specification*

From either of the *agreed* or *accepted into specification* states, the status of the MIDS Element definition can change to the *has issues* state and from there it can re-enter the *under discussion* state when the matter is picked up again for discussion within the TG.

## TG relation to CETAF Digitization WG
The [CETAF Digitisation Working Group](https://cetafdigitization.biowikifarm.net/cdig/) collaborates on digitization issues and collectively works together to share experiences to increase capacity and capability to digitize natural science collections. In this sense, it works with the MIDS materials produced by the present task group to discuss, implement, evaluate and provide input/feedback on the development of MIDS specifications to the present task group.

## Resources

### Current draft of the specification
[MIDS-definition-v0.12-03Nov2020.md](https://github.com/tdwg/mids/blob/working-draft/current-draft/MIDS-definition-v0.12-03Nov2020.md)

Cite as:
*Hardisty, A., Addink, W., Dillen, M., Groom, Q., Haston, E., et al. (Draft) Minimum Information about a Digital Specimen (MIDS) v0.12, 03 November 2020*.

### Other resources
Borsch, T., Stevens, A.-D., Häffner, E., Güntsch, A., Berendsohn, W.G., et al. (2020): A complete digitization of German herbaria is possible, sensible and should be started now. Research Ideas and Outcomes 6: e50675. https://doi.org/10.3897/rio.6.e50675.

MISC 2012. iDigBio MISC Data Element Catalog (Phase 1, V0, rev. 15 December 2012). https://www.idigbio.org/wiki/images/c/c9/Phase_I_Report.pdf.   


END.
