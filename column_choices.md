**Included Columns (and Why)**
* CURRENT_ENERGY_RATING – Target variable for classification (EPC rating A–G).
* POTENTIAL_ENERGY_RATING – Useful for comparison and understanding improvement potential.
* CURRENT_ENERGY_EFFICIENCY – Numeric score associated with the current rating, helpful for deeper analysis.
* POTENTIAL_ENERGY_EFFICIENCY – Shows potential efficiency improvements, could affect recommendations.
* PROPERTY_TYPE – Categorical feature; property type likely impacts energy rating.
* BUILT_FORM – Structural type affects insulation and energy performance.
* TOTAL_FLOOR_AREA – Larger homes typically consume more energy, influencing ratings.
* ENERGY_CONSUMPTION_CURRENT – Directly relates to energy usage patterns.
* ENERGY_CONSUMPTION_POTENTIAL – Indicates potential consumption reduction.
* CO2_EMISSIONS_CURRENT – Important environmental impact factor.
* CO2_EMISSIONS_POTENTIAL – Shows potential for emission reduction.
* NUMBER_HABITABLE_ROOMS – Proxy for property size and occupancy.
* NUMBER_HEATED_ROOMS – Indicates heating demand and usage.
* LOW_ENERGY_LIGHTING – Reflects presence of energy-efficient lighting.
* MAIN_FUEL – Type of main energy source affects consumption and efficiency.
* CONSTRUCTION_AGE_BAND – Age of property correlates with building standards and insulation.


**Excluded Columns (and Why)**
* LMK_KEY, UPRN, ADDRESS*, POSTCODE – Identifiers and location data; high cardinality and not predictive.
* LOCAL_AUTHORITY_LABEL, CONSTITUENCY_LABEL, POSTTOWN – Location info; excluded to avoid introducing regional bias.
* HOTWATER_DESCRIPTION, WINDOWS_DESCRIPTION, etc. – Free-text fields; difficult to encode without NLP.
* REPORT_TYPE, TENURE, PHOTO_SUPPLY, MECHANICAL_VENTILATION – Not directly relevant or too detailed for this classification task.
* ENERGY_TARIFF, WIND_TURBINE_COUNT, SOLAR_WATER_HEATING_FLAG – Rare or missing data; low predictive value.
* Technical efficiency ratings (e.g., WINDOWS_ENERGY_EFF) – Risk of data leakage; directly tied to the outcome variable.
* Detailed cost columns (HEATING_COST_CURRENT, etc.) – Reflect the outcome rather than predict it.