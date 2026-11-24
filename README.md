# Iberian lead-plaque lexicon: 40 lexical units with proposed meanings (not translations), certainty and provenance coding

## Warning for reuse: proposed meanings, not translations

Iberian is an undeciphered language. Every form–concept pair in this dataset is a *proposal* with a stated certainty grade, not an established translation. **Do not use the dataset as a dictionary**; filter by `Certainty` before any comparison. The warning is repeated in the `Comment` of every form.

## Content

Forty lexical units of the Iberian lead plaques (64 attested forms). For each unit:

- the meaning proposed in the literature or by the author;
- a certainty grade: **A**, value secured by metrology or by the literature; **B**, regularity documented in a text or group of texts; **C**, working hypothesis (mixed grades such as B/C are kept as coded);
- the provenance of the meaning, a design against circularity in comparisons with Basque: **I**, prior proposal by third parties, supported by material evidence or internal context; **II**, proposal of the author's monographs, deduced from the slot the term occupies in the document; **III**, Basque intervenes, at least in the checking (for the numerals, value assigned by position in the series). `Provenance_Author` is the author's coding; `Provenance_Jury` is the least favourable classification given by a blind jury.

- Base data: `raw/iberian_lead_plaque_lexicon.xlsx` (sheets `units` and `forms`) and `raw/sources.bib`.
- Concepticon linking: `etc/concepts.tsv` (36 of 40 units; A3, A4, A16 and A23 have no close concept set yet).
- Language: `etc/languages.tsv` (Glottocode iber1250). Orthography profile: `etc/orthography.tsv`; the values of *ś*, *ŕ* and *ḿ* are conventional and disputed.
- Forms are given in the standard transliteration of the Palaeohispanic semi-syllabary; `Inscriptions` holds the references of the Hesperia databank where the form is attested. The inscriptions themselves are not part of this dataset.

## How the dataset was made

The CLDF data are generated only by the cldfbench script in this repository (`cldfbench lexibank.makecldf lexibank_martinvalladolidiberian.py`), from the Excel file in `raw/` and the tables in `etc/`. The repository was prepared with the help of AI tools under the author's direction; the conversion is rebuilt and validated on every change by the workflow in `.github/workflows/`.

Related record (replication data and programs of the statistical study): https://doi.org/10.5281/zenodo.24446155
