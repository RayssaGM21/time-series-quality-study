# src/time_series_quality.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TimeSeriesQuality:
    def __init__(self, data: pd.DataFrame, time_column: str, value_column: str):
        self.data = data.copy()  # Evita modificar o DataFrame original
        self.time_column = time_column
        self.value_column = value_column

    def check_missing_values(self):
        """ Retorna o número e a porcentagem de valores ausentes. """
        missing_values = self.data[self.value_column].isna().sum()
        total_values = len(self.data)
        missing_percentage = (missing_values / total_values * 100) if total_values > 0 else 0
        return {"missing_count": missing_values, "missing_percentage": missing_percentage}

    def fill_missing_values(self, method="mean"):
        """ Preenche os valores ausentes usando diferentes estratégias. """
        if method == "mean":
            # Verificando e tratando os valores NaN de forma explícita
            valid_values = self.data[self.value_column][~self.data[self.value_column].isna()]  # Apenas valores não NaN
            mean_value = valid_values.mean()
            # print(f"Média calculada: {mean_value}")  # Para depuração
            self.data[self.value_column] = self.data[self.value_column].fillna(mean_value)
        elif method == "median":
            # Calcula a mediana dos valores não ausentes
            valid_values = self.data[self.value_column][~self.data[self.value_column].isna()]  # Apenas valores não NaN
            median_value = valid_values.median()
            # print(f"Mediana calculada: {median_value}")  # Para depuração
            self.data[self.value_column] = self.data[self.value_column].fillna(median_value)
        elif method == "ffill":
            self.data[self.value_column] = self.data[self.value_column].fillna(method="ffill")
        elif method == "bfill":
            self.data[self.value_column] = self.data[self.value_column].fillna(method="bfill")
        else:
            raise ValueError("Método de preenchimento inválido. Escolha entre: 'mean', 'median', 'ffill', 'bfill'.")


    def detect_anomalies(self, method="zscore", threshold=3):
        """ Detecta anomalias na série temporal usando diferentes métodos. """
        anomalies = None

        if method == "zscore":
            mean = self.data[self.value_column].mean()
            std = self.data[self.value_column].std()
            self.data["z_score"] = (self.data[self.value_column] - mean) / std
            print("Z-scores calculados:", self.data["z_score"])  # Imprimir os Z-scores para verificação
            anomalies = self.data[abs(self.data["z_score"]) > threshold].copy()
            self.data.drop(columns=["z_score"], inplace=True)  # Remove a coluna auxiliar
        elif method == "iqr":
            q1 = self.data[self.value_column].quantile(0.25)
            q3 = self.data[self.value_column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            anomalies = self.data[(self.data[self.value_column] < lower_bound) | 
                                (self.data[self.value_column] > upper_bound)].copy()
        else:
            raise ValueError("Método inválido. Escolha entre: 'zscore' ou 'iqr'.")
        
        return anomalies


    def plot_data(self):
        """ Plota a série temporal com possíveis anomalias. """
        plt.figure(figsize=(10,5))
        plt.plot(self.data[self.time_column], self.data[self.value_column], label="Série Temporal", color="blue")
        
        anomalies = self.detect_anomalies()
        if anomalies is not None and not anomalies.empty:
            plt.scatter(anomalies[self.time_column], anomalies[self.value_column], color="red", label="Anomalias", zorder=3)
        
        plt.xlabel("Tempo")
        plt.ylabel("Valor")
        plt.title("Série Temporal com Detecção de Anomalias")
        plt.legend()
        plt.show()
