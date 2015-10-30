from service.models import  SpeciesSheet, Species

def import_species(species_path):

    species = SpeciesSheet(species_path)

    for obj in species.objects():
        # Get the status label for the code
        code = obj.get('red_list_status_code', 'NA')
        IUCN_REDLIST_CATEGORIES = app.config.get("IUCN_REDLIST_CATEGORIES")
        obj['red_list_status_label'] = code
        if code in IUCN_REDLIST_CATEGORIES:
            obj['red_list_status_label'] = IUCN_REDLIST_CATEGORIES[code]
        # Populate and save species object
        s = Species()
        s.populate(obj)
        s.save()
