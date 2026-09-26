#!/usr/bin/env bash
set -euo pipefail
cat > MISSION.md <<'MD'
# Mission: Object-Oriented Programming

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab 4 (individual, graded) | 15% | 2026-11-13 | — |

## AI policy
AI may be used to study; code submitted must be written by the student.
MD
mkdir -p assignments/lab4
cat > assignments/lab4/STATEMENT.md <<'MD'
# Lab 4: bank accounts
Complete the TODOs in Bank.java. deposit and withdraw reject non-positive amounts; withdraw and
transfer throw InsufficientFundsException when the balance is too low; transfer is atomic.
MD
cat > assignments/lab4/Bank.java <<'JAVA'
import java.util.HashMap;
import java.util.Map;

public class Bank {
    private final Map<String, Long> balances = new HashMap<>();

    public void open(String id) {
        balances.put(id, 0L);
    }

    public void deposit(String id, long cents) {
        // TODO
    }

    public void withdraw(String id, long cents) throws InsufficientFundsException {
        // TODO
    }

    public void transfer(String from, String to, long cents) throws InsufficientFundsException {
        // TODO
    }
}
JAVA
