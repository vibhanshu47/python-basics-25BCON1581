# Audit Documentation

## 1. README Audit Table

| Claim made in README | True? | Evidence or Correction |
|---|---|---|
| `armstrong.py` checks whether a number is an Armstrong number. | Yes | The source code was reviewed and the program is intended to check Armstrong numbers. |
| `factorial.py` calculates the factorial of a number. | Yes | The source code was reviewed and the program calculates factorial. |
| `fibonacci.py` generates a Fibonacci sequence. | Yes | The source code was reviewed and the program generates Fibonacci numbers. |
| `prime.py` checks whether a number is prime. | Yes | The source code was reviewed and the program checks for prime numbers. |
| `pronic.py` checks whether a number is a pronic number. | Yes | The source code was reviewed and the program checks for pronic numbers. |
| `struct.py` demonstrates the required student-data program. | Yes | The source code was reviewed and the program stores and displays student information. |
| All programs automatically handle every invalid input. | No | Invalid-input handling depends on the implementation of each individual program. |

---

## 2. Commit Comparison Table

| Commit | My Original Commit Message | AI-Generated Commit Message | Which is clearer, and why? |
|---|---|---|---|
| 1 | Added Armstrong program | `feat: add Armstrong number checker` | The AI-generated message is shorter and clearly describes the purpose of the program. |
| 2 | Added factorial program | `feat: add factorial calculation` | The AI-generated message is concise and specific. |
| 3 | Added Fibonacci program | `feat: implement Fibonacci sequence generation` | The AI-generated message clearly describes what was implemented. |
| 4 | Added prime number program | `feat: add basic prime number checker` | The AI-generated message clearly identifies the functionality. |
| 5 | Added pronic number program | `feat: add pronic number checker` | The AI-generated message is short and descriptive. |
| 6 | Added student details program | `feat: add student information program` | The AI-generated message clearly explains what was added. |

---

## 3. Partner Review Notes

**Reviewed by:Mohit Jangid

- **armstrong.py:** The program was reviewed for correct Armstrong number checking logic.
- **factorial.py:** The factorial calculation was reviewed for correctness.
- **fibonacci.py:** The Fibonacci sequence generation was reviewed for correct logic.

---

## 4. Partner Review Notes

**Reviewed by:Mohit Jangid
- **prime.py:** The prime-number checking logic was reviewed and tested with appropriate values.
- **pronic.py:** The pronic-number checking logic was reviewed and tested.
- **struct.py:** The student information structure was reviewed for clarity and correct output formatting.

---

## 5. Testing Summary

The programs should be tested with both valid and invalid or boundary inputs where applicable.

### Armstrong
Example test values:
- `153` → Armstrong number
- `123` → Not an Armstrong number

### Factorial
Example test values:
- `5` → `120`
- `0` → `1`

### Fibonacci
Example test:
- Generate the sequence for a selected number of terms.

### Prime
Example test values:
- `7` → Prime
- `10` → Not prime

### Pronic
Example test values:
- `6` → Pronic
- `7` → Not pronic

### Student Information
Check that the entered student information is stored and displayed correctly.

---

## 6. Conclusion

The Python programs in this repository were reviewed according to their intended functionality. The programs should be tested before submission to make sure that their output matches the expected results.

The audit file will be updated if changes are made to the programs or repository.