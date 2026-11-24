"""Lexibank dataset: Iberian lead-plaque lexicon (40 lexical units with certainty and provenance coding).

Base data: raw/iberian_lead_plaque_lexicon.xlsx (sheets "units" and "forms").
Concepticon linking: etc/concepts.tsv.  Language: etc/languages.tsv.  Orthography profile: etc/orthography.tsv.

Run with:  cldfbench lexibank.makecldf lexibank_martinvalladolidiberian.py
"""
import pathlib

import attr
import openpyxl
from clldutils.misc import slug
from pylexibank import Concept, Lexeme, FormSpec
from pylexibank import Dataset as BaseDataset

XLSX = "iberian_lead_plaque_lexicon.xlsx"


@attr.s
class CustomConcept(Concept):
    Number = attr.ib(default=None)
    Spanish_Gloss = attr.ib(default=None)
    Certainty = attr.ib(default=None)
    Provenance_Author = attr.ib(default=None)
    Provenance_Jury = attr.ib(default=None)
    Unit_ID = attr.ib(default=None)


@attr.s
class CustomLexeme(Lexeme):
    Inscriptions = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "martinvalladolidiberian"
    concept_class = CustomConcept
    lexeme_class = CustomLexeme
    form_spec = FormSpec(separators="~;,/", missing_data=["∅"], first_form_only=False)

    def read_sheet(self, name):
        """Rows of one sheet of the raw Excel file as dicts (header in the first row; empty rows skipped)."""
        wb = openpyxl.load_workbook(str(self.raw_dir / XLSX), read_only=True, data_only=True)
        rows = list(wb[name].iter_rows(values_only=True))
        head = [str(h).strip() for h in rows[0]]
        return [
            dict(zip(head, ["" if v is None else str(v).strip() for v in row]))
            for row in rows[1:]
            if any(v is not None and str(v).strip() for v in row)
        ]

    def cmd_makecldf(self, args):
        args.writer.add_sources()
        args.writer.add_languages()
        units = {u["UNIT_ID"]: u for u in self.read_sheet("units")}
        concepts = {}
        for c in self.concepts:  # etc/concepts.tsv: one row per unit, with the Concepticon link
            u = units[c["ID"]]  # every unit of etc/concepts.tsv must exist in the raw file
            assert u["PROPOSED_MEANING_EN"] == c["ENGLISH"], c["ID"]
            idx = "{0}_{1}".format(c["NUMBER"], slug(c["ENGLISH"].split(";")[0]))
            args.writer.add_concept(
                ID=idx,
                Name=c["ENGLISH"],
                Number=c["NUMBER"],
                Concepticon_ID=c["CONCEPTICON_ID"] or None,
                Concepticon_Gloss=c["CONCEPTICON_GLOSS"] or None,
                Spanish_Gloss=u["PROPOSED_MEANING_ES"],
                Certainty=u["CERTAINTY"],
                Provenance_Author=u["PROVENANCE_AUTHOR"],
                Provenance_Jury=u["PROVENANCE_JURY"] or None,
                Unit_ID=c["ID"],
            )
            concepts[c["ID"]] = idx
        assert set(units) == set(concepts), set(units) ^ set(concepts)
        for row in self.read_sheet("forms"):
            args.writer.add_lexemes(
                Language_ID="Iberian",
                Parameter_ID=concepts[row["UNIT_ID"]],
                Value=row["FORM"],
                Source=[s for s in row["SOURCE"].split(";") if s],
                Inscriptions=row["INSCRIPTIONS"],
                # The warning travels with every form, also when only the forms table is reused.
                Comment="Proposed meaning, not an established translation (certainty {0}; provenance {1}).".format(
                    units[row["UNIT_ID"]]["CERTAINTY"], units[row["UNIT_ID"]]["PROVENANCE_AUTHOR"]
                ),
            )
