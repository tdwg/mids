# SSSOM mapping of MIDS elements
We use the [SSSOM standard](https://w3id.org/sssom/spec) to effectively map the elements of each MIDS level to terms as used in common domain data standards, such as Darwin Core or ABCD, but this implementation could also support other data models such as those used by a local collection management system. These mappings should make the MIDS calculation process machine actionable and reproducible.

In this readme, we will explain how exactly we are using the SSSOM standard and what this means for both the creation and interpretation of the mapping. The mappings are intended to connect MIDS elements to their corresponding terms in different data standards, in a simple manner. More complex models might not be compatible with SSSOM and require intricate RDF mappings to work. This is currently outside the scope of the MIDS standard. The mappings SHOULD be agnostic to the serialization of the standard as applied to a data source for which MIDS levels are to be calculated. Hence, mappings are for example between MIDS and Darwin Core, but not MIDS and a Darwin Core Archive.

## Mapping availability

Currently, we host the latest drafts of mappings created by the MIDS task group on the [TDWG MIDS repository](https://github.com/tdwg/mids), under the `mappings` [directory](https://github.com/tdwg/mids/tree/main/source/mappings).

Mapping files are currently separated by standard (e.g. dwc for Darwin Core) and by domain (e.g. biology). This info can also be found in the MappingSet metadata under `object_type` and `subject_type` respectively.

## Mapping file structure

We make use of a separate serialisation for the MappingSet metadata block (in YAML) and for the Mappings block (in tsv), in line with the [guide](https://mapping-commons.github.io/sssom/spec-formats-tsv/) from SSSOM documentation. We separate both data types so we do not need to combine the two serialisation formats into a single file.

The files SHOULD take the `mapping_set_id` from the metadata block as a filename, with a suffix of `.sssom.tsv` or `.sssom.yml`.

## Mapping specification
### General recommendations
When a field has multiple values, it is recommended to delimit it using the `|` (pipe) character, without any leading or trailing whitespace unless they are part of the value.

Any SSSOM mapping file SHOULD be UTF-8 encoded.

### Composition of the MappingSet
The MappingSet MUST be a valid YAML text file and include as its first element a `curie_map` which includes definitions of all namespaces used in the Mappings. 

A MappingSet SHOULD further include:

* `mapping_set_id`: A unique identifier to be used for this specific MappingSet and its associated Mappings. `mapping_set_id` should be constructed as a concatenation (using `_` to concatenate) of the prefix `mids` and the metadata terms `object_type`, `subject_type` and `mapping_set_version`.
* `license`: A URI specifying the license (or lack thereof) of these mappings.
* `mapping_set_version`: A MappingSet version indicator. Recommended practice is to use an incrementing integer starting at 1. Any change to the Mappings or MappingSet requires a new version.
* `mapping_provider`: A reference URL or persistent ID for the source or entity which makes this MappingSet available.
* `mapping_date`: Date the Mappings or MappingSet were last modified.
* `object_type`: The standard to map to. Recommended practice is to use the namespace from the curie_map. Alternatively a URI or other persistent ID.
* `subject_type`: Domain the mappings apply to. A formal definition of domains will be included in the MIDS specification.

A MappingSet can optionally also include:

* `mapping_set_title`: A human-readable title for the MappingSet.
* `mapping_set_description`: A human-readable description for the MappingSet. This can include a list of latest changes, but it is recommended to principally store these at the Mappings level in `sssom:comment`.
* `object_preprocessing`: If any preprocessing needs to be applied to the terms that are to be mapped, this should be documented here. Best practice is to use a controlled vocabulary such as `semapv`. If the preprocessing technique has any parameters, these should be included in the Mappings. For example, if `object_preprocessing` includes `semapv:RegexRemoval`, then a column with name `semapv:RegexRemoval` should be included in the Mappings and the parameters (` | `-delimited if more than one) should be included in that column.

### Composition of the Mappings
The Mappings MUST be a valid tab-separated values (tsv) text file. String quotation using single `"` pairs is allowed. `"` characters as part of a field require the whole field to be quoted, and need to be individually escaped with a second `"`. This follows the [recommendation](https://mapping-commons.github.io/sssom/spec-formats-tsv/#quoting) made in the SSSOM specification.

The mappings MUST include most of the following properties as columns, in the order specified. OPTIONAL columns may be omitted. Column names MUST include the proper namespace, even if it is mostly `sssom:`. `_label` terms from the sssom specification are all optional, but if used should be added in the same order as they occur in the [list of Mapping terms](https://mapping-commons.github.io/sssom/Mapping/).

* `sssom:subject_id`: MUST. The MIDS element being mapped to.
* `sssom:subject_category`: MUST. The MIDS level of the MIDS element, specified as `mids:MIDS0` and so on.
* `sssom:predicate_id`: MUST. The type of relation between the MIDS element and the term that is being mapped to it. We currently recognize three types of relations:
  * `skos:narrowMatch`: The MIDS element may be found in multiple terms of the standard that is being mapped, all of which should have this predicate. This is similar to the logic of an `OR` operator.
  * `skos:exactMatch`: The MIDS element maps exactly to a term in the standard, and therefore no instances of `skos:narrowMatch` can apply for this MIDS element.
  * `owl:intersectionOf`: The MIDS element maps exactly to a combination of terms in the standard. The combination is specified in the `sssom:object_match_field` column (`|`-delimited), but only once for one of the combination member rows. It is in theory possible that a MIDS element maps to multiple overlapping combinations of terms in the mapped standard. This is similar to the logic of an `AND` operator.
* `sssom:object_id`: MUST. ID of a term in the mapped standard.
* `sssom:object_category`: OPTIONAL. ID of a category in the mapped standard. A category will typically indicate which file of the standard the term may be found in, if it is more complex in structure. Darwin Core extensions are an example.
* `sssom:mapping_justification`: OPTIONAL. To indicate how the mapping was established.
* `sssom:author_id`: OPTIONAL. An ID for the asserter of the mapping (not necessarily the same person who compiled the mappings into the SSSOM format). Recommended to use ORCID.
* `sssom:creator_id`: MUST. An ID for the creator of the mapping in the SSSOM format.
* `sssom:subject_type`: OPTIONAL. The type of property of the MIDS element. Currently defined as `rdf property`.
* `sssom:object_type`: OPTIONAL. The type of property of the term in the standard. 
* `sssom:mapping_date`: MUST. ISO date of when the mapping was asserted by the author.
* `sssom:object_match_field`: OPTIONAL. A `|`-delimited list of object_ids which combine to form an `owl:intersectionOf` mapping.
* `sssom:comment`: OPTIONAL. Clarifications.
* `semapv:RegexRemoval`: OPTIONAL. As an example of how `object_preprocessing` at the MappingSet level can be used. This field should be populated with a `|`-delimited list of values that are not sufficient to fullfill the condition of a MIDS level. Recommendation is to always start with a leading `|`, to emphasize that empty strings (in addition to default `null` values) are not sufficient to fulfill a MIDS condition.

## Interpretation of the Mappings
The ultimate outcome of a MIDS calculation is a level score for each processed specimen. A level is reached if all MIDS elements that are defined at that level or below it, have non-`null` values for any of the provided mappings. This includes a single `narrowMatch` or `exactMatch`, or a complete combination of `intersectionOf`, for each Element.

The calculation process requires data formulated following the mapped standard to be checked for null values in each mapping. `object_preprocessing` may also apply to exclude other insufficient non-null values, such as `unknown:undigitized` as recommended in [Groom et aL. (2019)](https://doi.org/10.1093/database/baz129). The outcome of this calculation is a binary map of all mappings with true or false (1 or 0) depending on whether a value was found. This map is then thresholded into a single value of the MIDS level reached, which is the minimal level of MIDS for which all elements have at least one mapping that returns true.

The binary map is currently no formal defined outcome of MIDS and implementers can calculate it in any way they want. It is useful to show these more detailed results to the data providers, as they make it more clear why a certain MIDS level was (not) met. Recommended practice is to at least produce and, ideally, store the following metadata for each specimen processed in the calculation:

* `dc:identifier`: A persistent ID for the specimen that was processed in the MIDS calculation.
* `dc:created`: An ISO date of when the calculation was performed.
* `sssom:mapping_set_id`: MappingSet ID of the mappings used for the calculation.
* `dwc:datasetID`: An ID for the dataset processed. Can be versioned.
* `dc:publisher`: Entity responsible for the calculation process.