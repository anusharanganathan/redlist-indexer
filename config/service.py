############################################
# important overrides for the ES module

# elasticsearch back-end connection settings
ELASTIC_SEARCH_HOST = "http://localhost:9200"
ELASTIC_SEARCH_INDEX = "reactordb"
ELASTIC_SEARCH_VERSION = "1.4.4"

from esprit import mappings1x
ELASTIC_SEARCH_DEFAULT_MAPPING = mappings1x.make_mapping("_default_", [mappings1x.EXACT])

# Classes which will initialise themselves in the index with their self_init() method
# (note that if ELASTIC_SEARCH_DEFAULT_MAPPING is sufficient, you don't need to
# add anything here
ELASTIC_SEARCH_SELF_INIT = [
    "service.dao.SpeciesJobDAO"
]

############################################
# important overrides for account module

ACCOUNT_ENABLE = False
SECRET_KEY = "super-secret-key"

#############################################
# important overrides for storage module

#STORE_IMPL = "octopus.modules.store.store.StoreLocal"
#STORE_TMP_IMPL = "octopus.modules.store.store.TempStore"

from octopus.lib import paths
STORE_LOCAL_DIR = paths.rel2abs(__file__, "..", "service", "tests", "local_store", "live")
STORE_TMP_DIR = paths.rel2abs(__file__, "..", "service", "tests", "local_store", "tmp")

##############################################
IUCN_REDLIST_CATEGORIES = {
    u'EX':    u'Extinct',
    u'EW':    u'Extinct In The Wild',
    u'RE':    u'Regionally Extinct',
    u'CR':    u'Critically Endangered',
    u'EN':    u'Endangered',
    u'VU':    u'Vulnerable',
    u'LR/cd': u'Lower Risk: Conservation Dependent',
    u'NT':    u'Near Threatened',
    u'LR/nt': u'Near Threatened',
    u'DD':    u'Data Deficient',
    u'LC':    u'Least Concern',
    u'LR/lc': u'Least Concern',
    u'NA':    u'Not Available'
}