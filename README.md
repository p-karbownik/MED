# MED

## 1. Instalacja wymaganych bibliotek
```requirements
pip install -r requirements.txt
```

## 2. Struktura projektu
```struktura
MED
  |--dataset
  |--declat
  |--experiments
  |--experiments_stage2
  |--plotting
  |--results
     |--time
        |--plots
  |--test
```

### 2.1 dataset
Folder zawiera przygotowane zbiory danych w postaci plików .csv. 
Dodatkowo znajduje się tam skrypt pozwalajacy na stworzenie zbiorów.

### 2.2 declat
Znajduje się tutaj implementacja obu algorytmów DECLAT. declat.py oraz readDataset.py
są podstawową wersją naszego algorytmu, natomiast bit_declat.py oraz readBitDataset.py 
zawierają implementację z użyciem bitarrays w zakresie transakcji oraz diffsetów.

### 2.3 experiments oraz experiments_stage2
Foldery zawierające skrypty służące do przeprowadzenia eksperymentów obu algorytmów

### 2.4 ploting
Zawarta jest tutaj implementacja funkcji służących do wizualizacji otrzymanych wyników.
Dane mogą być pokzane za pomocą kraty algebraicznej tagów, analizy ilości zbiorów częstych 
o określonym wsparciu. Dodatkowo generujemy wykres czasu działania algorytmu w zależności
od minimalnego wsparcia dla zbiorów częstych.

