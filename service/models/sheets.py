from octopus.lib import clcsv, dataobj
import re

def synonym(cell):
    vals = [x.strip() for x in cell.split("|")]

    return vals

def common_name(cell):
    vals = [x.strip() for x in cell.split(",")]

    return vals

def petition(cell):
    if not cell:
        return False
    elif cell.strip().lower() == 'n':
        return False
    else:
        return True

def owner(cell):
    owners = []
    share_rx = "^(.+) \((.+)\)$"
    lines = cell.split("\n\n")

    for line in lines:
        m = re.search(share_rx, line)
        own = {}
        if m is not None:
            own["name"] = m.group(1)
            own["share"] = m.group(2)
        else:
            own["name"] = line
        owners.append(own)

    return owners

class SpeciesSheet(clcsv.SheetWrapper):

    HEADERS = {
        # main identifying field
        u'Species ID': u'species_id',

        # fields in the species sheet
        u'Kingdom': u'kingdom',
        u'Phylum': u'phylum',
        u'Class': u'species_class',
        u'Order': u'order',
        u'Family': u'family',
        u'Genus': u'genus',
        u'Species': u'species',
        u'Authority': u'authority',
        u'Infraspecific rank': u'infraspecific_rank',
        u'Infraspecific name': u'infraspecific_name',
        u'Infraspecific authority': u'infraspecific_authority',
        u'Stock/subpopulation': u'subpopulation',
        u'Synonyms': u'synonyms',
        u'Common names (Eng)': u'common_names_eng',
        u'Common names (Fre)': u'common_names_fre',
        u'Common names (Spa)': u'common_names_spa',
        u'Red List status': u'red_list_status_code',
        u'Red List criteria': u'red_list_criteria',
        u'Red List criteria version': u'red_list_criteria_version',
        u'Year assessed': u'year_assessed',
        u'Population trend': u'population_trend',
        u'Petitioned': u'petitioned',
    }

    COERCE = {
        "synonyms" : synonym,
        "common_names_eng" : common_name,
        "red_list_criteria_version" : dataobj.to_float(),
        "year_assessed": dataobj.to_int(),
        "petitioned" : petition,
    }

    DEFAULT_COERCE = [dataobj.to_unicode()]

    IGNORE_VALUES = {
    }

    EMPTY_STRING_AS_NONE = True

    def __init__(self, path):
        super(SpeciesSheet, self).__init__(path)


