# tests/test_time_series_quality.py
import unittest
import pandas as pd
import numpy as np
from src.time_series_quality import TimeSeriesQuality

class TestTimeSeriesQuality(unittest.TestCase):

    def setUp(self):
        """ Método de preparação para os testes """
        self.data = pd.DataFrame({
            "date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
            "value": [1, 2, 3, np.nan, 5, 6, np.nan, 8, 9, 100]
        })
        self.ts_quality = TimeSeriesQuality(self.data, "date", "value")

    def test_check_missing_values(self):
        result = self.ts_quality.check_missing_values()
        self.assertEqual(result["missing_count"], 2)
        self.assertEqual(result["missing_percentage"], 20.0)

    def test_fill_missing_values_mean(self):
        self.ts_quality.fill_missing_values(method="mean")
        # Média dos valores não ausentes: [1, 2, 3, 5, 6, 8, 9, 100] = 134 / 8 = 16.75
        self.assertAlmostEqual(self.ts_quality.data["value"].iloc[3], 16.75)

    def test_fill_missing_values_median(self):
        self.ts_quality.fill_missing_values(method="median")
        # Mediana dos valores não ausentes: [1, 2, 3, 5, 6, 8, 9, 100] => mediana é 5.5
        self.assertEqual(self.ts_quality.data["value"].iloc[3], 5.5)

    def test_detect_anomalies_zscore(self):
        anomalies = self.ts_quality.detect_anomalies(method="zscore", threshold=2)
        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies["value"].iloc[0], 100)

    def test_detect_anomalies_iqr(self):
        anomalies = self.ts_quality.detect_anomalies(method="iqr")
        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies["value"].iloc[0], 100)

if __name__ == "__main__":
    unittest.main()
