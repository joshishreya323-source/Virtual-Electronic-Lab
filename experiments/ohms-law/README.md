# Experiment 1 — Ohm's Law

## 1. Experiment Name

Ohm's Law

## 2. Objective

To verify the relationship between voltage, current and resistance.

## 3. Required Components

1. DC Voltage Source
2. Resistor
3. Ammeter
4. Voltmeter
5. Ground

## 4. Student Input Values

The student should be able to enter/change:

- Voltage value
- Resistance value

Example:

Voltage = 10 V

Resistance = 1 kΩ

## 5. Expected Calculation

The application should calculate the current from the voltage and resistance.

Example:

Voltage = 10 V

Resistance = 1 kΩ

Expected current = 10 mA

## 6. Correct Circuit

The voltage source, resistor and ammeter should form a complete series path.

The voltmeter should be connected across the resistor.

The circuit should have a proper reference/ground connection.

## 7. Possible Student Mistakes

### Error 1 — Open Circuit

If the circuit path is not complete:

Message:

"Your circuit is incomplete. Please check the connections."

### Error 2 — Voltmeter Connected Incorrectly

If the voltmeter is not connected across the resistor:

Message:

"Voltmeter should be connected across the resistor."

### Error 3 — Ammeter Connected Incorrectly

If the ammeter is not connected in series:

Message:

"Ammeter should be connected in series with the circuit."

### Error 4 — Missing Resistor

If the resistor is missing:

Message:

"Resistor is required for this experiment."

### Error 5 — Missing Voltage Source

If the voltage source is missing:

Message:

"Voltage source is required for this experiment."

### Error 6 — Missing Ground

If the required ground/reference connection is missing:

Message:

"Please add a ground/reference connection."

## 8. Correct Example

Voltage = 10 V

Resistance = 1 kΩ

Circuit is complete.

Expected current = 10 mA.

Result:

"Experiment completed successfully."

## 9. Test Cases

### Test Case 1

Voltage = 10 V

Resistance = 1 kΩ

Expected result = 10 mA

### Test Case 2

Voltage = 5 V

Resistance = 1 kΩ

Expected result = 5 mA

### Test Case 3

Voltage = 10 V

Resistance = 2 kΩ

Expected result = 5 mA

### Test Case 4

Resistor missing

Expected result = Error

### Test Case 5

Voltage source missing

Expected result = Error

### Test Case 6

Open circuit

Expected result = Error

### Test Case 7

Ammeter connected incorrectly

Expected result = Error

### Test Case 8

Voltmeter connected incorrectly

Expected result = Error

### Test Case 9

Ground missing

Expected result = Error

### Test Case 10

All connections correct

Expected result = Success