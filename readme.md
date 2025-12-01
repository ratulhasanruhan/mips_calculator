# USCC Headquarter's Instruction Set Architecture (ISA)

A concise specification for a simple 32-bit instruction format used by a four-function calculator CPU.

## Overview
- Design: Four-function calculator that operates only on numbers stored in registers.
- Input: CPU receives instructions as 32-bit binary strings (ASCII '0'/'1').
- Output: Results are printed to the terminal.
- Supported operand range: 10-bit unsigned values (0 through 1023) stored in registers. Calculations may produce negative results (e.g., 5 - 10 = -5).

## Registers
- 32 registers, indexed 0..31.
  - Registers 0..21: Available for number storage.
    - Register 0 is a constant zero (read-only).
  - Registers 22..31: Reserved for history storage (H0..H9).

Register layout (for reference)
- 0: 0 (constant)
- 1..21: general storage
- 22..31: history registers H0..H9

## Instruction format (32 bits)
- Bit fields (total 32 bits):
  - Bits 0-5   : opcode (6 bits)
  - Bits 6-10  : source_one (5 bits) — first source register index
  - Bits 11-15 : source_two (5 bits) — second source register index
  - Bits 16-25 : store (10 bits) — immediate value for store operations or reserved
  - Bits 26-31 : function_code (6 bits)

Notes:
- The bit numbering above follows the original spec (bits 0..31). Keep the same numbering when assembling or decoding instructions.
- Use these field names in program code: opcode, source_one, source_two, store, function_code.

## Opcode / Function quick reference
- opcode 000000 (R-type): arithmetic operations; function_code selects the operation
  - function_code 100000 : ADD (add two registers)
  - function_code 100010 : SUBTRACT (subtract two registers)
  - function_code 011000 : MULTIPLY (multiply two registers)
  - function_code 011010 : DIVIDE (divide two registers)
- opcode 000001 with function_code 000000 : STORE immediate value to next register
- opcode 100001 with function_code 000000 : RETURN previous calculation (history)

## Detailed operation notes
- Arithmetic operations (opcode 000000):
  - Use source_one and source_two to pick registers (each 5 bits -> values 0..31).
  - The function_code identifies which arithmetic operation to perform.
  - The instruction may or may not place results into a register depending on the CPU implementation; the spec reserves registers 22..31 for history storage of prior results.

- Store operation (opcode 000001, function_code 000000):
  - The 10-bit 'store' field (bits 16-25) holds an immediate value between 0 and 1023.
  - When executed, the CPU stores the immediate value into the next available data register (implementation detail). Register 0 remains constant 0.

- Return operation (opcode 100001, function_code 000000):
  - Intended to return a previous calculation from history registers (22..31). Exact behavior depends on CPU implementation.

## Examples
- Field sizes: opcode(6) | source_one(5) | source_two(5) | store(10) | function_code(6)

1) Store the value 5 (decimal) as an immediate
- Decimal 5 in 10-bit binary: 0000000101
- Example instruction fields:
  - opcode: 000001 (store)
  - source_one: 00000 (unused)
  - source_two: 00000 (unused)
  - store: 0000000101
  - function_code: 000000
- Full 32-bit instruction (concatenate fields):
  000001 00000 00000 0000000101 000000
- As a single 32-bit string (spaces optional):
  00000100000000000000000101000000

2) Add contents of register 1 and register 2 (R-type add)
- Fields:
  - opcode: 000000
  - source_one: 00001 (register 1)
  - source_two: 00010 (register 2)
  - store: 0000000000 (unused for R-type)
  - function_code: 100000 (add)
- Full 32-bit instruction:
  000000 00001 00010 0000000000 100000
- As a single 32-bit string:
  00000000001000100000000000100000

## Implementation tips
- When parsing an instruction string, validate length == 32 and that each character is '0' or '1'.
- Convert bit slices to integers when extracting field values.
- Guard arithmetic: division should handle divide-by-zero and produce a well-defined result or error.
- The CPU should enforce register 0 as constant zero and prevent writes to it.

## Contact
- For questions about this ISA, consult the project owner or open an issue in the repository.

