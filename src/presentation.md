---
marp: true
---

# Klasifikácia

Matej Kubinec

---

# Čo je to klasifikácia?

- Klasifikácia je proces predikcie triedy danej množiny dát.
- Triedy sú nazývané aj cieľ/značka alebo kategória.
- Patrí do skupiny učenia s učiteľom (trenovacie dáta majú známu triedu)

---

# Prečo vôbec klasifikovať dáta?

- detekcia spamu (binárna klasifikácia)
- ***

# Ako môžeme klasifikovať dáta?

1. Lazy Learners
   - Trieda je určená na základe podobnosti/blízkosti k testovacím dátam.
   - Oproti Eager Learners je náročnejší výpočet predikcie.
   - napr. k-nearest neighbor, case-based reasoning
2. Eager Learners
   - Zostrojí sa klasifikátor založený na trénovacích dátach.
   - Oproti Lazy Learners je výpočet náročnejší v trénovacej fáze.
   - napr. rozhodovacie stromy, Naive Bayes klasifikátor, neurónové siete

---

# Dáta - Golf/Weather

[zdroj](https://datacadamia.com/data_mining/weather)

| Outlook  | Temperature | Numeric Temperature |     | Nominal Humidity | Numeric Humidity | Nominal Windy | Play |
| -------- | ----------- | ------------------- | --- | ---------------- | ---------------- | ------------- | ---- |
| overcast | 83          | hot                 | 86  | high             | FALSE            | yes           |
| overcast | 64          | cool                | 65  | normal           | TRUE             | yes           |
| overcast | 72          | mild                | 90  | high             | TRUE             | yes           |
| overcast | 81          | hot                 | 75  | normal           | FALSE            | yes           |
| rainy    | 70          | mild                | 96  | high             | FALSE            | yes           |
| rainy    | 68          | cool                | 80  | normal           | FALSE            | yes           |
| rainy    | 65          | cool                | 70  | normal           | TRUE             | no            |
| rainy    | 75          | mild                | 80  | normal           | FALSE            | yes           |
| rainy    | 71          | mild                | 91  | high             | TRUE             | no            |
| sunny    | 85          | hot                 | 85  | high             | FALSE            | no            |
| sunny    | 80          | hot                 | 90  | high             | TRUE             | no            |
| sunny    | 72          | mild                | 95  | high             | FALSE            | no            |
| sunny    | 69          | cool                | 70  | normal           | FALSE            | yes           |
| sunny    | 75          | mild                | 70  | normal           | TRUE             | yes           |

---

# Predspracovanie

---

# K-Nearest Neighbour

---

# Rozhodovacie stromy

---

# Neuronové siete

---

# Vyhodnocovanie klasifikátora
