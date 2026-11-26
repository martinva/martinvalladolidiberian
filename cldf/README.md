<a name="ds-cldfmetadatajson"> </a>

# Wordlist Iberian lead-plaque lexicon: 40 lexical units with proposed meanings (not translations), certainty and provenance coding

**CLDF Metadata**: [cldf-metadata.json](./cldf-metadata.json)

**Sources**: [sources.bib](./sources.bib)

Forty lexical units of the Iberian lead plaques (64 attested forms) with proposed meanings, certainty grades and provenance coding. Iberian is undeciphered: the meanings are proposals, not translations.

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Martín Valladolid, David (2026). Iberian lead-plaque lexicon: 40 lexical units with proposed meanings (not translations), certainty and provenance coding. CLDF dataset. Zenodo. https://doi.org/10.5281/zenodo.24530083
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Wordlist](http://cldf.clld.org/v1.0/terms.rdf#Wordlist)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://github.com/martinva/martinvalladolidiberian
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/martinva/martinvalladolidiberian
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/martinva/martinvalladolidiberian/tree/e2d63cd">martinva/martinvalladolidiberian  e2d63cd</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.4">Glottolog  v5.4</a></li><li><a href="https://github.com/concepticon/concepticon-data/tree/v3.4.0">Concepticon  v3.4.0</a></li><li><a href="https://github.com/cldf-clts/clts/tree/v2.3.1">CLTS  v2.3.1</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>lingpy-rcParams</strong>: <a href="./lingpy-rcParams.json">lingpy-rcParams.json</a></li><li><strong>python</strong>: 3.11.18</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | martinvalladolidiberian
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-formscsv"></a>Table [forms.csv](./forms.csv)

CustomLexeme(ID: str, Form: str, Value: str, Language_ID: str, Parameter_ID: str, Local_ID: Optional[str] = None, Segments: list[str] = <factory>, Graphemes: Optional[list[str]] = None, Profile: Optional[str] = None, Source: list[str] = <factory>, Comment: Optional[str] = None, Cognacy: Optional[str] = None, Loan: Optional[bool] = None, Inscriptions: Optional[str] = None)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF FormTable](http://cldf.clld.org/v1.0/terms.rdf#FormTable)
[dc:extent](http://purl.org/dc/terms/extent) | 64


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Local_ID](http://purl.org/dc/terms/identifier) | `string` | 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | 
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Cognacy` | `string` | 
`Loan` | `boolean` | 
`Graphemes` | `string` | 
`Profile` | `string` | 
`Inscriptions` | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

A language.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
`Glottolog_Name` | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
`Family` | `string` | 

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

CustomConcept(ID: Optional[str] = '', Name: Optional[str] = '', Concepticon_ID: Optional[str] = None, Concepticon_Gloss: Optional[str] = None, Number: Optional[str] = None, Spanish_Gloss: Optional[str] = None, Certainty: Optional[str] = None, Provenance_Author: Optional[str] = None, Provenance_Jury: Optional[str] = None, Unit_ID: Optional[str] = None)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 40


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Concepticon_ID](http://cldf.clld.org/v1.0/terms.rdf#concepticonReference) | `string` | 
`Concepticon_Gloss` | `string` | 
`Number` | `string` | 
`Spanish_Gloss` | `string` | 
`Certainty` | `string` | 
`Provenance_Author` | `string` | 
`Provenance_Jury` | `string` | 
`Unit_ID` | `string` | 
