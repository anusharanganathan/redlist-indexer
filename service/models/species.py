from service.dao import SpeciesJobDAO
from octopus.lib import dataobj, strings, dates


class Species(dataobj.DataObj, SpeciesJobDAO):
    def __init__(self, raw=None):
        struct = {
            "fields" : {
                "id" : {"coerce" : "unicode"},
                "created_date" : {"coerce" : "utcdatetime"},
                "last_updated" : {"coerce" : "utcdatetime"},

                "species_id" : {"coerce" : "integer", "allow_none" : False},
                "kingdom" : {"coerce" : "unicode", "ignore_none" : True},
                "phylum" : {"coerce" : "unicode", "ignore_none" : True},
                "species_class" : {"coerce" : "unicode", "ignore_none" : True},
                "order" : {"coerce" : "unicode", "ignore_none" : True},
                "family" : {"coerce" : "unicode", "ignore_none" : True},
                "genus" : {"coerce" : "unicode", "ignore_none" : True},
                "species" : {"coerce" : "unicode", "ignore_none" : True},
                "authority" : {"coerce" : "unicode", "ignore_none" : True},
                "infraspecific_rank" : {"coerce" : "unicode", "ignore_none" : True},
                "infraspecific_name" : {"coerce" : "unicode", "ignore_none" : True},
                "infraspecific_authority" : {"coerce" : "unicode", "ignore_none" : True},
                "subpopulation" : {"coerce" : "unicode", "ignore_none" : True},
                "synonyms" : {"coerce" : "unicode", "ignore_none" : True},
                "common_names_eng" : {"coerce" : "unicode", "ignore_none" : True},
                "red_list_status_code" : {"coerce" : "unicode", "ignore_none" : True},
                "red_list_status_label" : {"coerce" : "unicode", "ignore_none" : True},
                "red_list_criteria" : {"coerce" : "unicode", "ignore_none" : True},
                "red_list_criteria_version" : {"coerce" : "float", "ignore_none" : True},
                "year_assessed" : {"coerce" : "integer", "ignore_none" : True},
                "population_trend" : {"coerce" : "unicode", "ignore_none" : True},
                "petitioned" : {"coerce" : "boolean", "ignore_none" : True}
            }
        }

        self._add_struct(struct)
        super(Species, self).__init__(raw=raw, expose_data=True)