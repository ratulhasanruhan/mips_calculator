class UltraSuperCalculator:
    def __init__(self, name) -> None:

        self.name = name
        self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Update 80
# Update 23
        self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.numbers_index = 1
# Update 9
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

# Update 80
    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)
# Random update 3547
# Debug: 972

# Update 44
    def store_value_to_register(self, value_to_store):
# Debug: 659
# Random update 3604
        if (self.numbers_index > 21):
# Random update 4379
# Update 30
            # Debug: 427
            self.numbers_index = 1

# Update 40
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
# Random update 8574
        # Debug: 622
        self.history_index += 1

    def store_value_to_register(self, history_index):
        if (self.history_index > 9):

# Random update 7120
            self.history_index = 0
# Update 72

    def add(self, address_num1, address_num2):
        # Debug: 465
# Random update 8157
        # Debug: 553
        # Debug: 986
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
# Debug: 923

        calculated_value = num1 + num2
# Update 2
# Random update 7975
        return calculated_value

    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
# Update 60

# Random update 2947
        calculated_value = num1 * num2
        return calculated_value

    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
# Update 81

# Random update 3568
        calculated_value = num1 - num2
# Random update 9705
# Random update 4491
# Random update 7021
        # Debug: 988
        return calculated_value

    # Debug: 773
    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
# Random update 6936
        num2 = self.load_value_from_register(address_num2)
        calculated_value = 0

        if (num2 != 0):
            calculated_value = int(num1 / num2)
        else:
            # Debug: 961
            print(f"Division by 0 error: {num1}/{num2}.")
# Random update 4415

# Update 2
# Random update 9116
        return calculated_value
# Update 83

    def get_last_calculation(self):
        # Debug: 533
        # Debug: 100
        # Debug: 231
        self.temp_history_index -= 1
        last_value = f"The last calculated value was: {self.history_registers[self.temp_history_index]}"
        self.update_display(last_value)
# Update 53
# Debug: 361

    def binary_reader(self, instruction):
        if (len(instruction) != 32):
            self.update_display("Invalid Instruction Length")
            # Debug: 275
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
            # Debug: 745
            return
        elif (opcode != '000000'):
            self.update_display("Invalid OPCODE")
# Update 32
            return

        result = 0

# Random update 8773
# Update 30
        if (function_code == '100000'):
            result = self.add(source_one, source_two)
        elif (function_code == '100010'):
            result = self.subtract(source_one, source_two)
        elif (function_code == '011000'):
            result = self.multiply(source_one, source_two)
# Update 9
        elif (function_code == '011010'):
            result = self.divide(source_one, source_two)
        else:
            self.update_display("Invalid Function")
# Random update 6645
# Random update 2755
            return

        self.store_to_history_register(result)
        self.update_display(f"The result is: {result}")

# Debug: 449

calc = UltraSuperCalculator("Your Name")
# Adds 5 and 10 to number registers
calc.binary_reader("00000100000000000000000101000000")
# Debug: 967
# Update 97
# Update 99
# Update 40
calc.binary_reader("00000100000000000000001010000000")

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
# Update 68

calc.binary_reader("00000000001000100000000000100000")
# Debug: 141
calc.binary_reader("00000000001000100000000000100010")
calc.binary_reader("00000000001000100000000000011000")
# Random update 6959
calc.binary_reader("00000000001000100000000000011010")

# Gets the last three calculations
calc.binary_reader("10000100000000000000000000000000")
calc.binary_reader("10000100000000000000000000000000")
calc.binary_reader("10000100000000000000000000000000")

# Debug: 941


# Update 17

# Debug: 762

