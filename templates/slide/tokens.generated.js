/* GENERATED FILE - DO NOT EDIT.
   Written by scripts/build_slide_tokens.py from brand/tokens.json, which is the
   only place in SHULL OS where a hex is typed. Edit tokens.json and re-run.
   Hand-editing this file puts a colour in two places, which is the defect the
   whole system is built to prevent. */

module.exports = {
  "version": "1.0.0",
  "ground": {
    "white": "FFFFFF",
    "parchment": "EDF0E5",
    "asphalt": "14161B",
    "graphite": "2E3338",
    "mutedOnDark": "BDB6AA",
    "ruleHairline": "C8CDC2",
    "label": "55604F",
    "footer": "61675B"
  },
  "courses": {
    "chemistry": {
      "primary": "A3E635",
      "secondary": "22D3EE",
      "primaryDeep": "4D730E",
      "label": "CHEMISTRY"
    },
    "physics": {
      "primary": "F5B82E",
      "secondary": "8B5CF6",
      "primaryDeep": "896107",
      "label": "PHYSICS"
    },
    "geology": {
      "primary": "16B8A6",
      "secondary": "E85D24",
      "primaryDeep": "0E766A",
      "label": "GEOLOGY"
    }
  },
  "type": {
    "$comment": "Slide System v2 scale. Supersedes the older slide-standard.md scale - see CONFLICT-07.",
    "unitTitle": 40,
    "sectionNumber": 44,
    "headline": 28,
    "subhead": 17,
    "body": 16,
    "workArea": 19,
    "cardLabel": 12,
    "eyebrow": 11,
    "footer": 10
  },
  "fonts": {
    "display": "Trade Gothic Next",
    "body": "Trade Gothic Next"
  },
  "floor": 16,
  "geom": {
    "W": 13.333,
    "H": 7.5,
    "M": {
      "l": 0.75,
      "r": 0.75,
      "t": 0.62,
      "b": 0.55
    },
    "RAIL": 0.18,
    "eyebrowY": 0.42,
    "hairlineY": 0.74,
    "hairlineW": 1.5,
    "headlineY": 1.02,
    "headlineH": 0.95,
    "subheadY": 2.02,
    "bodyTopY": 2.62,
    "footerY": 6.98,
    "mustWriteH": 0.62,
    "padX": 0.22,
    "padY": 0.18
  },
  "lineCaps": {
    "contentWithHighlight": 3,
    "contentWithoutHighlight": 5,
    "vocabularyTerms": 4,
    "workedExampleSteps": 4,
    "tableDataRows": 6
  },
  "darkGroundLayouts": [
    "01_UNIT_TITLE",
    "02_SECTION_TITLE",
    "04_DIVIDER",
    "06_CONCEPT_IMAGE",
    "12_DECK_INDEX"
  ]
};
