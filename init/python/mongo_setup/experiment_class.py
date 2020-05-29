class Experiment:

    def set_polymer(self, polymer):
        for entry in self.data['trials']:
            entry["membrane_or_polymer"] = polymer
        return 0

    def set_adsorbing(self, adsorbing):
        for entry in self.data['trials']:
            entry['adsorbing'] = adsorbing
            entry["solutes_present"].append(adsorbing)
        return 0

    def __init__(self):
        self.data = {
            "name": "",
            "technique": {
                "name": "sample_technique",
                "technique_metadata": {
                    "some_stuff": "some more things",
                    "some_more_stuff": "some things"
                }
            },
            "experiment_metadata": {
                "gap": ""
            },
            "researcher": {
                "mwet_id": "",
                "name": "",
                "group": "",
                "institution": ""
            },
            "experimental_conditions": {
                "run_time": "7 days",
                "membrane_or_polymer_area": "1 cm^2"
            },
            "trials": [

                {
                    "membrane_or_polymer": "",
                    "ph": 7,
                    "ionic_strength": {
                        "value": 0.01,
                        "unit": "mM"
                    },
                    "solutes_present": ["Na+", "Cl-", ],
                    "adsorbing": ""
                },

                {
                    "membrane_or_polymer": "",
                    "ph": 10,
                    "ionic_strength": {
                        "value": 0.01,
                        "unit": "mM"
                    },
                    "solutes_present": ["Na+", "Cl-", ],
                    "adsorbing": ""
                },
                {
                    "membrane_or_polymer": "",
                    "pH": 7,
                    "ionic_strength": {
                        "value": 0.1,
                        "unit": "mM"
                    },
                    "solutes_present": ["Na+", "Cl-", ],
                    "adsorbing": ""
                },
                {
                    "membrane_or_polymer": "",
                    "ph": 10,
                    "ionic_strength": {
                        "value": 0.1,
                        "unit": "mM"
                    },
                    "solutes_present": ["Na+", "Cl-", ],
                    "adsorbing": ""
                }
            ]
        }
