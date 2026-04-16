# MIDS Serialization Exploration
20260416

This directory contains exploratory RDF serializations of the MIDS specification, produced with the assistance of large language models. The contents are not intended for production use or to reflect any consensus among contributors — they are meant to explore how MIDS might be expressed as RDF.

---

## mids_ontology.ttl
Generated with the aid of Claude on 20260416

### Structure
* Ontology header — provenance, contributors, license (CC BY 4.0), and version (DRAFT) drawn from the source pages
* 4 classes — mids:InformationElement, mids:MIDSLevel, mids:Discipline, mids:DisciplineSchema
* Core properties — mids:requiresElement, mids:buildsOn, mids:hasMappingDwC/ABCD, mids:purpose, mids:usageNote, mids:isGenericLevel, etc.
* 4 MIDS level instances (Bare ? Basic ? Intermediate ? Extended) with mids:buildsOn chains
* 3 discipline instances with definitions sourced from MSO/USGS Thesaurus
* 21 information element instances — all definitions, purposes, usage notes, examples, and DwC mappings where clearly stated
* 12 discipline schema instances (3 disciplines × 4 levels) encoding which elements are required at each discipline+level combination

### Design decisions worth flagging

* Namespace http://rs.tdwg.org/mids/ is provisional — the spec says it's pending ratification; a comment block at the top makes this explicit
* The Paleontology MIDS3 schema table lists CollectorID, which has no separate definition in §6. I mapped it to the canonical mids-ie:CollectingAgentID with an inline comment; worth resolving in the spec
* DwC mappings are partial — only where the source makes explicit statements. The full SSSOM mapping table lives at /mappings/index.html and would need a separate pass to fully populate mids:hasMappingDwC and mids:hasMappingABCD
* Schemas encode incremental element sets per level, not cumulative — SPARQL queries should traverse mids:buildsOn to get the full element set for a given level      
