"""One-off generator: stadocgen TSV -> terms CSV (latimer-shaped + mids extensions)."""
import csv
from collections import defaultdict
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "stadocgen/20260430/output"
LATIMER = Path(__file__).resolve().parent / "examples/latimer.csv"
OUT_PATH = Path(__file__).resolve().parent / "mids.csv"

DOC_MOD = "2026-04-30T12:00:00-05:00"
TERM_NS = "http://rs.tdwg.org/mids/"
ORG_IE = "http://rs.tdwg.org/mids/InformationElement"
ORG_LEVEL = "http://rs.tdwg.org/mids/MIDSLevel"
ORG_DISC = "http://rs.tdwg.org/mids/Discipline"

# Extra columns appended after the latimer template
EXTRA_COLS = ["purpose", "isRequiredBy"]

META_CLASSES = [
    {
        "document_modified": DOC_MOD,
        "term_localName": "InformationElement",
        "term_isDefinedBy": TERM_NS,
        "term_created": "2024-05-16",
        "term_modified": "",
        "term_deprecated": "",
        "replaces_term": "",
        "replaces1_term": "",
        "replaces2_term": "",
        "label": "Information Element",
        "definition": (
            "A structured category of specimen data expected to be present in a digital "
            "record at a given MIDS level. Information elements define the minimum set of "
            "data fields required to achieve each level of digitization for natural science "
            "specimens."
        ),
        "usage": (
            "Information elements are grouped by MIDS level and, at levels 2 and 3, by "
            "scientific discipline (Biology, Geology, Palaeontology). Each element includes "
            "a definition, purpose, and usage note. See "
            "https://tdwg.github.io/mids/information-elements/index.html"
        ),
        "notes": (
            "Information elements are the normative building blocks of MIDS. Each element "
            "has a definition, purpose, usage note, and is required by one or more "
            "discipline schemas at specific MIDS levels. MIDS defines the minimum "
            "information at each level; capturing more information is strongly encouraged."
        ),
        "examples": "",
        "rdf_type": "http://www.w3.org/2000/01/rdf-schema#Class",
        "tdwgutility_organizedInClass": TERM_NS,
        "tdwgutility_required": "No",
        "tdwgutility_repeatable": "No",
        "purpose": "",
        "isRequiredBy": "",
    },
    {
        "document_modified": DOC_MOD,
        "term_localName": "MIDSLevel",
        "term_isDefinedBy": TERM_NS,
        "term_created": "2024-05-16",
        "term_modified": "",
        "term_deprecated": "",
        "replaces_term": "",
        "replaces1_term": "",
        "replaces2_term": "",
        "label": "MIDS Level",
        "definition": (
            "A progressive level of digitization representing the type and depth of "
            "digitization achieved for a natural science specimen. Four levels (0\u20133) "
            "represent a simple categorization of digitization approaches, from a bare "
            "record associating a physical specimen with a digital identifier (level 0) to "
            "an extended record with linked open data identifiers (level 3)."
        ),
        "usage": (
            "Levels 0 and 1 apply generically to all disciplines. Levels 2 and 3 are "
            "discipline-specific, reflecting recognized differences in data priorities for "
            "Biology, Geology, and Palaeontology. The different levels relate to a staged "
            "digitization programme that may require different funding, equipment, and "
            "workflows at each stage. See "
            "https://tdwg.github.io/mids/information-elements/index.html"
        ),
        "notes": (
            "Each MIDS level has been determined to reflect a broad use case, helping "
            "build a business case for funding. The MIDS score for an individual specimen "
            "can be calculated by assessing the information required for each level against "
            "the information present in the digitized specimen record. Data can be mapped "
            "to Darwin Core or ABCD terms using the mapping tables provided at "
            "https://tdwg.github.io/mids/mappings/index.html"
        ),
        "examples": "`MIDS Level 0`, `MIDS Level 1`, `MIDS Level 2`, `MIDS Level 3`",
        "rdf_type": "http://www.w3.org/2000/01/rdf-schema#Class",
        "tdwgutility_organizedInClass": TERM_NS,
        "tdwgutility_required": "No",
        "tdwgutility_repeatable": "No",
        "purpose": "",
        "isRequiredBy": "",
    },
    {
        "document_modified": DOC_MOD,
        "term_localName": "Discipline",
        "term_isDefinedBy": TERM_NS,
        "term_created": "2024-05-16",
        "term_modified": "",
        "term_deprecated": "",
        "replaces_term": "",
        "replaces1_term": "",
        "replaces2_term": "",
        "label": "Discipline",
        "definition": (
            "A scientific discipline for which distinct digitization priorities and "
            "information element requirements are recognized within MIDS. Three disciplines "
            "are currently defined: Biology, Geology, and Palaeontology."
        ),
        "usage": (
            "Disciplines are used to differentiate the information element requirements at "
            "MIDS levels 2 and 3. All three disciplines share the same information elements "
            "at MIDS levels 0 and 1. It was recognized that, at higher levels, there were "
            "sufficient differences in the data between Biology, Geology, and Palaeontology "
            "to warrant discipline-specific element sets. See "
            "https://tdwg.github.io/mids/about/index.html"
        ),
        "notes": (
            "The Earth Sciences and Paleobiology Interest Group (ESP IG) work is oriented "
            "to ensure that minimum information about both biological and non-biological "
            "(i.e., fossil, rock, mineral) specimens can be presented within the MIDS "
            "framework. Additional disciplines may be added in future versions of the "
            "standard."
        ),
        "examples": "`Biology`, `Geology`, `Palaeontology`",
        "rdf_type": "http://www.w3.org/2000/01/rdf-schema#Class",
        "tdwgutility_organizedInClass": TERM_NS,
        "tdwgutility_required": "No",
        "tdwgutility_repeatable": "No",
        "purpose": "",
        "isRequiredBy": "",
    },
]

REPEATABLE_LOCALS = {
    "CollectingAgent",
    "Media",
    "CollectingAgentID",
    "IdentifiedByID",
    "MediaID",
}


def load_tsv(name: str) -> list[dict[str, str]]:
    path = OUT_DIR / name
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def fmt_examples(examples: list[str]) -> str:
    parts: list[str] = []
    for ex in examples:
        ex = ex.strip()
        if ex:
            parts.append(f"`{ex}`")
    return ", ".join(parts)


def empty_extras() -> dict[str, str]:
    return {col: "" for col in EXTRA_COLS}


def main() -> None:
    with open(LATIMER, encoding="utf-8") as f:
        latimer_header = next(csv.reader(f))

    header = latimer_header + EXTRA_COLS

    rows: list[dict[str, str]] = []

    for rec in load_tsv("master-list.tsv"):
        tln = rec["term_local_name"].strip()
        rows.append(
            {
                "document_modified": DOC_MOD,
                "term_localName": tln,
                "term_isDefinedBy": TERM_NS,
                "term_created": rec.get("term_created", "").strip(),
                "term_modified": rec.get("term_modified", "").strip(),
                "term_deprecated": "",
                "replaces_term": "",
                "replaces1_term": "",
                "replaces2_term": "",
                "label": rec.get("label", "").strip(),
                "definition": rec.get("definition", "").strip(),
                "usage": rec.get("usage", "").strip(),
                "notes": rec.get("notes", "").strip(),
                "examples": "",
                "rdf_type": rec.get("rdf_type", "").strip(),
                "tdwgutility_organizedInClass": ORG_IE,
                "tdwgutility_required": "No",
                "tdwgutility_repeatable": "Yes" if tln in REPEATABLE_LOCALS else "No",
                "purpose": rec.get("purpose", "").strip(),
                "isRequiredBy": rec.get("isRequiredBy", "").strip(),
                "_ex_key": tln,
            }
        )
        if rec.get("examples", "").strip():
            rows[-1]["examples"] = rec["examples"].strip()

    ex_by_term: dict[str, list[str]] = defaultdict(list)
    for rec in load_tsv("examples.tsv"):
        k = rec["term_local_name"].strip()
        ex_by_term[k].append(rec.get("example", "").strip())

    for r in rows:
        key = r.pop("_ex_key")
        merged: list[str] = []
        if r["examples"]:
            merged.append(r["examples"])
        merged.extend(ex_by_term.get(key, []))
        r["examples"] = fmt_examples(merged)

    for rec in load_tsv("levels.tsv"):
        tln = rec["term_local_name"].strip()
        rows.append(
            {
                "document_modified": DOC_MOD,
                "term_localName": tln,
                "term_isDefinedBy": TERM_NS,
                "term_created": "",
                "term_modified": "",
                "term_deprecated": "",
                "replaces_term": "",
                "replaces1_term": "",
                "replaces2_term": "",
                "label": (rec.get("pref_label") or "").strip() or tln,
                "definition": rec.get("definition", "").strip(),
                "usage": rec.get("usage", "").strip(),
                "notes": "",
                "examples": "",
                "rdf_type": rec.get("rdf_type", "").strip(),
                "tdwgutility_organizedInClass": ORG_LEVEL,
                "tdwgutility_required": "No",
                "tdwgutility_repeatable": "No",
                "purpose": rec.get("purpose", "").strip(),
                "isRequiredBy": "",
            }
        )

    for rec in load_tsv("discipline_terms.tsv"):
        term = rec["term"].strip()
        src = rec.get("source", "").strip()
        url = rec.get("source_url", "").strip()
        note = f"Source: {src}." + (f" {url}" if url else "")
        rows.append(
            {
                "document_modified": DOC_MOD,
                "term_localName": term,
                "term_isDefinedBy": TERM_NS,
                "term_created": "",
                "term_modified": "",
                "term_deprecated": "",
                "replaces_term": "",
                "replaces1_term": "",
                "replaces2_term": "",
                "label": term,
                "definition": rec.get("definition", "").strip(),
                "usage": "",
                "notes": note,
                "examples": "",
                "rdf_type": "http://www.w3.org/2000/01/rdf-schema#Class",
                "tdwgutility_organizedInClass": ORG_DISC,
                "tdwgutility_required": "No",
                "tdwgutility_repeatable": "No",
                "purpose": "",
                "isRequiredBy": "",
            }
        )

    rows = rows + META_CLASSES

    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in header})

    print(f"Wrote {len(rows)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
