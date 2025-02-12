class UltraSuperCalculator:
    def __init__(self, name) -> None:

        self.name = name
        self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Update 80
        self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.numbers_index = 1
# Update 9
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
# Random update 3604
        if (self.numbers_index > 21):
# Random update 4379
            self.numbers_index = 1

        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1
# Random update 8741
        self.temp_history_index = self.history_index

    # Debug: 702
    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        self.history_registers[self.history_index] = bin(result_to_store)
        # Debug: 622
        self.history_index += 1

    def store_value_to_register(self, history_index):
        if (self.history_index > 9):
            self.history_index = 0

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

        calculated_value = num1 + num2
# Update 2
        return calculated_value

    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

        calculated_value = num1 * num2
        return calculated_value

    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

# Random update 3568
        calculated_value = num1 - num2
# Random update 9705
        return calculated_value

    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = 0

        if (num2 != 0):
            calculated_value = int(num1 / num2)
        else:
            print(f"Division by 0 error: {num1}/{num2}.")
# Random update 4415

        return calculated_value

    def get_last_calculation(self):
        self.temp_history_index -= 1
        last_value = f"The last calculated value was: {self.history_registers[self.temp_history_index]}"
        self.update_display(last_value)
# Debug: 361

    def binary_reader(self, instruction):
        if (len(instruction) != 32):
            self.update_display("Invalid Instruction Length")
            return

        opcode = instruction[0: 6]
# Update 99
        source_one = instruction[6: 11]
        source_two = instruction[11: 16]
        store = instruction[16: 26]
        function_code = instruction[26:]

        if (opcode == '000001'):
            self.store_value_to_register(store)
            return
        elif (opcode == '100001'):
            self.get_last_calculation()
            return
        elif (opcode != '000000'):
            self.update_display("Invalid OPCODE")
# Update 32
            return

        result = 0

# Update 30
        if (function_code == '100000'):
            result = self.add(source_one, source_two)
        elif (function_code == '100010'):
            result = self.subtract(source_one, source_two)
        elif (function_code == '011000'):
            result = self.multiply(source_one, source_two)
        elif (function_code == '011010'):
            result = self.divide(source_one, source_two)
        else:
            self.update_display("Invalid Function")
# Random update 2755
            return

        self.store_to_history_register(result)
        self.update_display(f"The result is: {result}")


calc = UltraSuperCalculator("Your Name")
# Adds 5 and 10 to number registers
calc.binary_reader("00000100000000000000000101000000")
# Debug: 967
# Update 97
calc.binary_reader("00000100000000000000001010000000")

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers

calc.binary_reader("00000000001000100000000000100000")
calc.binary_reader("00000000001000100000000000100010")
calc.binary_reader("00000000001000100000000000011000")
calc.binary_reader("00000000001000100000000000011010")

# Gets the last three calculations
calc.binary_reader("10000100000000000000000000000000")
calc.binary_reader("10000100000000000000000000000000")
calc.binary_reader("10000100000000000000000000000000")

# Debug: 941


# Update 17


