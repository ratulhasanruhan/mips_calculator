class UltraSuperCalculator:
    def __init__(self, name) -> None:

        self.name = name
        self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Update 80
# Update 23
# Update 20
        self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.numbers_index = 1
# Update 9
        self.history_index = 0
        self.temp_history_index = 0
# Update 60

# Update 22
        self.user_display = ''
# Update 46
        self.update_display(f"Welcome to {self.name}'s Calculator!")


# Update 80
    # Debug: 684
    def update_display(self, to_update):
        self.user_display = to_update
# Update 78
        print(self.user_display)
# Random update 3547
# Debug: 972
# Random update 8722

# Update 44
    def store_value_to_register(self, value_to_store):
# Debug: 659
# Random update 5661
# Random update 3604
        if (self.numbers_index > 21):

# Random update 4379
# Update 30
            # Debug: 427
            self.numbers_index = 1

# Update 40
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
# Random update 6970
        # Debug: 780
        self.numbers_index += 1
# Random update 8741
        self.temp_history_index = self.history_index

    # Debug: 702
    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
# Update 10
# Update 72
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        self.history_registers[self.history_index] = bin(result_to_store)
# Random update 8574

        # Debug: 610
# Update 87
        # Debug: 622
        self.history_index += 1

    def store_value_to_register(self, history_index):
# Random update 9811
# Random update 6808
        if (self.history_index > 9):
# Debug: 989

# Random update 7120
            self.history_index = 0
# Update 4
# Update 72

    def add(self, address_num1, address_num2):
        # Debug: 465
# Random update 8157
        # Debug: 553
        # Debug: 986
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
# Debug: 923
# Update 90

        calculated_value = num1 + num2
# Random update 8771
# Random update 3507

# Random update 4629
# Update 2
# Random update 7975
        return calculated_value

    # Debug: 798
    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
# Update 89
        num2 = self.load_value_from_register(address_num2)
# Update 42
# Update 60

# Random update 2947
        calculated_value = num1 * num2
# Random update 8155
# Debug: 971
# Update 68
# Update 3
        # Debug: 829
        return calculated_value
# Update 67
# Debug: 568

# Random update 7267
    def subtract(self, address_num1, address_num2):
# Update 12
# Update 13
        num1 = self.load_value_from_register(address_num1)
# Random update 9823
        num2 = self.load_value_from_register(address_num2)
# Debug: 828

# Update 81

# Random update 8318
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

# Update 81
        if (num2 != 0):
            calculated_value = int(num1 / num2)
        else:
            # Debug: 961
# Random update 1838
            print(f"Division by 0 error: {num1}/{num2}.")
# Update 41
# Random update 4415

# Update 89
# Update 2
# Random update 9116
# Update 34
        return calculated_value
# Update 83


# Random update 4161
    def get_last_calculation(self):
        # Debug: 533
        # Debug: 100
        # Debug: 231
        self.temp_history_index -= 1
        last_value = f"The last calculated value was: {self.history_registers[self.temp_history_index]}"
# Random update 7593
        self.update_display(last_value)
# Update 53
# Debug: 361

# Update 19
    def binary_reader(self, instruction):
        # Debug: 212
# Random update 3467
        # Debug: 781
        if (len(instruction) != 32):
            self.update_display("Invalid Instruction Length")
            # Debug: 275
            return

        # Debug: 926
        opcode = instruction[0: 6]
# Update 99
        source_one = instruction[6: 11]
        source_two = instruction[11: 16]

        store = instruction[16: 26]
# Random update 4185
        function_code = instruction[26:]

        if (opcode == '000001'):
            self.store_value_to_register(store)
            return
        elif (opcode == '100001'):
            self.get_last_calculation()
            # Debug: 745
            return
        elif (opcode != '000000'):
# Update 42
            self.update_display("Invalid OPCODE")
# Update 93
# Update 32
# Random update 1556
            return

        result = 0
# Debug: 512
# Debug: 627
# Update 80
# Debug: 205

# Random update 8773
# Update 26
# Update 58
# Update 70
# Update 30
        if (function_code == '100000'):

            result = self.add(source_one, source_two)
        # Debug: 563
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

# Update 50
        self.store_to_history_register(result)
# Random update 6387
        self.update_display(f"The result is: {result}")
# Random update 8450

# Debug: 449

calc = UltraSuperCalculator("Your Name")
# Adds 5 and 10 to number registers
calc.binary_reader("00000100000000000000000101000000")
# Debug: 882
# Debug: 967
# Update 97
# Update 45
# Update 99
# Update 40
# Debug: 180
calc.binary_reader("00000100000000000000001010000000")

# Random update 3505
# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
# Update 68

# Random update 2627
# Update 61
calc.binary_reader("00000000001000100000000000100000")
# Debug: 141
calc.binary_reader("00000000001000100000000000100010")
calc.binary_reader("00000000001000100000000000011000")

# Random update 6959

# Update 21
# Random update 6964
# Update 64
calc.binary_reader("00000000001000100000000000011010")

# Gets the last three calculations
calc.binary_reader("10000100000000000000000000000000")
# Update 20
calc.binary_reader("10000100000000000000000000000000")
calc.binary_reader("10000100000000000000000000000000")

# Debug: 480
# Debug: 941


# Debug: 459
# Update 17

# Debug: 762

# Random update 8333
