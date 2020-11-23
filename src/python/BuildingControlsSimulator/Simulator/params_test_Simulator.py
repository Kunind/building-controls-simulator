# created by Tom Stesco tom.s@ecobee.com
import os
from BuildingControlsSimulator.DataClients.DataSpec import (
    DonateYourDataSpec,
    Internal,
    FlatFilesSpec,
)

"""
Models:
    Furnace.idf:
        This model is not realistic at all, but is included in every
        EnergyPlus installation and for this reason is used to test
        basic I/O and functionality of the simulation platform.
    
"""

test_params_local = []
test_params_gcs_dyd = []
test_params_gbq_flatfiles = []

# if os.environ.get("LOCAL_CACHE_DIR"):
if False:
    test_params_local = [
        {
            "config": {
                "identifier": "DYD_dummy_data",
                "latitude": 41.8781,
                "longitude": -87.6298,
                "start_utc": "2018-05-16",
                "end_utc": "2018-06-01",
                "min_sim_period": "1D",
                "sim_step_size_seconds": 900,
                "output_step_size_seconds": 300,
            },
            "data_client": {
                "is_local_source": True,
                "is_gcs_source": False,
                "is_gbq_source": False,
                "gcp_project": None,
                "gcs_uri_base": None,
                "gbq_table": None,
                "source_data_spec": DonateYourDataSpec(),
                "source_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
                "is_local_destination": True,
                "is_gcs_destination": False,
                "is_gbq_destination": False,
                "destination_data_spec": DonateYourDataSpec(),
                "destination_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
            },
            "building_model": {
                "is_energyplus_building": True,
                "idf_name": "Furnace.idf",
                "epw_name": "USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw",
            },
            "controller_model": {
                "is_deadband": True,
                "is_fmu": False,
            },
            "state_estimator_model": {
                "is_low_pass_filter": True,
                "low_pass_filter_alpha": 0.5,
            },
            "expected_result": {
                "mean_thermostat_temperature": 31.277347564697266,
                "mean_thermostat_humidity": 94.8772964477539,
                "output_format_mean_thermostat_temperature": 88.2989273071289,
                "output_format_mean_thermostat_humidity": 94.8772964477539,
            },
        },
        {
            "config": {
                "identifier": "DYD_dummy_data",
                "latitude": 41.8781,
                "longitude": -87.6298,
                "start_utc": "2018-05-16",
                "end_utc": "2018-06-01",
                "min_sim_period": "1D",
                "sim_step_size_seconds": 60,
                "output_step_size_seconds": 300,
            },
            "data_client": {
                "is_local_source": True,
                "is_gcs_source": False,
                "is_gbq_source": False,
                "gcp_project": None,
                "gcs_uri_base": None,
                "gbq_table": None,
                "source_data_spec": DonateYourDataSpec(),
                "source_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
                "is_local_destination": True,
                "is_gcs_destination": False,
                "is_gbq_destination": False,
                "destination_data_spec": DonateYourDataSpec(),
                "destination_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
            },
            "building_model": {
                "is_energyplus_building": True,
                "idf_name": "Furnace.idf",
                "epw_name": "USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw",
            },
            "controller_model": {
                "is_deadband": True,
                "is_fmu": False,
            },
            "state_estimator_model": {
                "is_low_pass_filter": True,
                "low_pass_filter_alpha": 0.5,
            },
            "expected_result": {
                "mean_thermostat_temperature": 30.995126724243164,
                "mean_thermostat_humidity": 96.03016662597656,
                "output_format_mean_thermostat_temperature": 87.79023742675781,
                "output_format_mean_thermostat_humidity": 96.03016662597656,
            },
        },
    ]

# if os.environ.get("DYD_GCS_URI_BASE"):
if False:
    test_params_gcs_dyd = [
        {
            "config": {
                "identifier": "2e7467a283eaa1ab1d435bca6d7a36017e0fabf6",
                "latitude": 41.8781,
                "longitude": -87.6298,
                "start_utc": "2018-01-10",
                "end_utc": "2018-01-17",
                "min_sim_period": "1D",
                "sim_step_size_seconds": 60,
                "output_step_size_seconds": 300,
            },
            "data_client": {
                "is_local_source": False,
                "is_gcs_source": True,
                "is_gbq_source": False,
                "gcp_project": os.environ.get("DYD_GOOGLE_CLOUD_PROJECT"),
                "gcs_uri_base": os.environ.get("DYD_GCS_URI_BASE"),
                "gbq_table": None,
                "source_data_spec": DonateYourDataSpec(),
                "source_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
                "is_local_destination": True,
                "is_gcs_destination": False,
                "is_gbq_destination": False,
                "destination_data_spec": DonateYourDataSpec(),
                "destination_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
            },
            "building_model": {
                "is_energyplus_building": True,
                "idf_name": "IL_Chicago_gasfurnace_heatedbsmt_IECC_2018_940_upgraded.idf",
                "epw_name": "USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw",
            },
            "controller_model": {
                "is_deadband": True,
                "is_fmu": False,
            },
            "state_estimator_model": {
                "is_low_pass_filter": True,
                "low_pass_filter_alpha": 0.5,
            },
            "expected_result": {
                "mean_thermostat_temperature": 20.913745880126953,
                "mean_thermostat_humidity": 25.508949279785156,
                "output_format_mean_thermostat_temperature": 69.64488983154297,
                "output_format_mean_thermostat_humidity": 25.508949279785156,
            },
        },
        {
            "config": {
                "identifier": "2e7467a283eaa1ab1d435bca6d7a36017e0fabf6",
                "latitude": 41.8781,
                "longitude": -87.6298,
                "start_utc": "2018-06-10",
                "end_utc": "2018-06-17",
                "min_sim_period": "1D",
                "sim_step_size_seconds": 60,
                "output_step_size_seconds": 300,
            },
            "data_client": {
                "is_local_source": False,
                "is_gcs_source": True,
                "is_gbq_source": False,
                "gcp_project": os.environ.get("DYD_GOOGLE_CLOUD_PROJECT"),
                "gcs_uri_base": os.environ.get("DYD_GCS_URI_BASE"),
                "gbq_table": None,
                "source_data_spec": DonateYourDataSpec(),
                "source_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
                "is_local_destination": True,
                "is_gcs_destination": False,
                "is_gbq_destination": False,
                "destination_data_spec": DonateYourDataSpec(),
                "destination_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
            },
            "building_model": {
                "is_energyplus_building": True,
                "idf_name": "IL_Chicago_gasfurnace_heatedbsmt_IECC_2018_940_no_elec_no_dhw.idf",
                "epw_name": "USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw",
            },
            "controller_model": {
                "is_deadband": True,
                "is_fmu": False,
            },
            "state_estimator_model": {
                "is_low_pass_filter": True,
                "low_pass_filter_alpha": 0.5,
            },
            "expected_result": {
                "mean_thermostat_temperature": 20.913745880126953,
                "mean_thermostat_humidity": 25.508949279785156,
                "output_format_mean_thermostat_temperature": 69.64488983154297,
                "output_format_mean_thermostat_humidity": 25.508949279785156,
            },
        },
    ]

if os.environ.get("FLATFILES_GBQ_TABLE"):
    test_params_gbq_flatfiles = [
        {
            "config": {
                "identifier": os.environ.get("TEST_GBQ_FF_IDENTIFIER"),
                "latitude": 41.8781,
                "longitude": -87.6298,
                "start_utc": "2019-01-14",
                "end_utc": "2019-01-18",
                "min_sim_period": "1D",
                "sim_step_size_seconds": 60,
                "output_step_size_seconds": 300,
            },
            "data_client": {
                "is_local_source": False,
                "is_gcs_source": False,
                "is_gbq_source": True,
                "gcp_project": os.environ.get("DYD_GOOGLE_CLOUD_PROJECT"),
                "gcs_uri_base": None,
                "gbq_table": os.environ.get("FLATFILES_GBQ_TABLE"),
                "source_data_spec": FlatFilesSpec(),
                "source_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
                "is_local_destination": True,
                "is_gcs_destination": False,
                "is_gbq_destination": False,
                "destination_data_spec": FlatFilesSpec(),
                "destination_local_cache": os.environ.get("LOCAL_CACHE_DIR"),
            },
            "building_model": {
                "is_energyplus_building": True,
                "idf_name": "Chicago_IL_2story_heatedbsmt_gasfurnace_AC.idf",
                "epw_name": "USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw",
                "building_config": {
                    "ach50": 5,
                    "wsf": 0.6,
                    "r_si_wall": 5.2,
                    "r_si_floor": 4.0,
                    "r_si_ceil": 6.5,
                    "window_to_wall_ratio": 0.2,
                    "u_window": 1.1,
                },
            },
            "controller_model": {
                "is_deadband": True,
                "is_fmu": False,
            },
            "state_estimator_model": {
                "is_low_pass_filter": True,
                "low_pass_filter_alpha": 0.2,
            },
            "expected_result": {
                "mean_thermostat_temperature": 20.913745880126953,
                "mean_thermostat_humidity": 25.508949279785156,
                "output_format_mean_thermostat_temperature": 69.64488983154297,
                "output_format_mean_thermostat_humidity": 25.508949279785156,
            },
        },
    ]

test_params = (
    test_params_local + test_params_gcs_dyd + test_params_gbq_flatfiles
)