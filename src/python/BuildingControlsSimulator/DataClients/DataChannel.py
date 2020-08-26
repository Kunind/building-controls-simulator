# created by Tom Stesco tom.s@ecobee.com

import logging
from abc import ABC, abstractmethod

import attr
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


@attr.s(kw_only=True)
class DataChannel:

    data = attr.ib()
    spec = attr.ib()
    full_data_periods = attr.ib(default=None)

    def get_full_data_periods(self, expected_period):
        # if self.data has no records then there are no full_data_periods
        full_data_periods = []
        if len(self.data) > 0:
            self.data = self.data.sort_values(
                self.spec.datetime_column, ascending=True
            )
            # drop records that are incomplete
            # weather_column = [
            #     self.epw_column_map[c] for c in self.weather_columns
            # ][0]
            self.data = self.data[
                ~self.data[self.spec.null_check_column].isnull()
            ].reset_index()

            diffs = self.data[self.spec.datetime_column].diff()

            # check for missing records
            missing_start_idx = diffs[
                diffs > pd.to_timedelta(expected_period)
            ].index.to_list()

            missing_end_idx = [idx - 1 for idx in missing_start_idx] + [
                len(self.data) - 1
            ]
            missing_start_idx = [0] + missing_start_idx
            # ensoure ascending before zip
            missing_start_idx.sort()
            missing_end_idx.sort()

            full_data_periods = list(
                zip(
                    pd.to_datetime(
                        self.data[self.spec.datetime_column][
                            missing_start_idx
                        ].values,
                        utc=True,
                    ),
                    pd.to_datetime(
                        self.data[self.spec.datetime_column][
                            missing_end_idx
                        ].values,
                        utc=True,
                    ),
                )
            )

        self.full_data_periods = full_data_periods
