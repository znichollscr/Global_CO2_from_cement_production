# functions for country codes etc. currently copied from UNFCCC?non-AnnexI_data
# import from primap2 once the functionality is integrated there

import pycountry

custom_country_mapping_code = {}
custom_country_mapping_name = {
    'Bonaire, Saint Eustatius and Saba': 'BES',
    'Cape Verde': 'CPV',
    'Democratic Republic of the Congo': 'COD',
    'Faeroe Islands': 'FRO',
    'Micronesia (Federated States of)': 'FSM',
    'Iran': 'IRN',
    'Laos': 'LAO',
    'Occupied Palestinian Territory': 'PSE',
    'Swaziland': 'SWZ',
    'Taiwan': 'TWN',
    'Wallis and Futuna Islands': 'WLF',
    'Global': 'EARTH',
}

def get_country_code(
    country_name: str,
) -> str:
    """
    obtain country code. If the input is a code it will be returned,
    if the input
    is not a three letter code a search will be performed

    Parameters
    __________
    country_name: str
        Country code or name to get the three-letter code for.

    Returns
    -------
        country_code: str

    """
    # First check if it's in the list of custom codes
    if country_name in custom_country_mapping_code:
        country_code = country_name
    elif country_name in custom_country_mapping_name:
        country_code = custom_country_mapping_name[country_name]
    else:
        try:
            # check if it's a 3 letter UNFCCC_GHG_data
            country = pycountry.countries.get(alpha_3=country_name)
            country_code = country.alpha_3
        except:
            try:
                country = pycountry.countries.search_fuzzy(
                    country_name.replace("_", " ")
                )
            except:
                raise ValueError(
                    f"Country name {country_name} can not be mapped to "
                    f"any country code. Try using the ISO3 code directly."
                )
            if len(country) > 1:
                country_code = None
                for current_country in country:
                    if current_country.name == country_name:
                        country_code = current_country.alpha_3
                if country_code is None:
                    raise ValueError(
                        f"Country name {country_name} has {len(country)} "
                        f"possible results for country codes."
                    )

            country_code = country[0].alpha_3

    return country_code