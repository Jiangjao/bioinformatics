# !/usr/bin/python3

from base64 import encode
import os, re, sys

class SymbolTable:
	symbols = {
		'SP': 0,
		'LCL': 1,
		'ARG': 2,
		'THIS': 3,
		'THAT': 4,
		'R0': 0,
		'R1': 1,
		'R2': 2,
		'R3': 3,
		'R4': 4,
		'R5': 5,
		'R6': 6,
		'R7': 7,
		'R8': 8,
		'R9': 9,
		'R10': 10,
		'R11': 11,
		'R12': 12,
		'R13': 13,
		'R14': 14,
		'R15': 15,
		'SCREEN': 0x4000,
		'KBD': 0x6000
	}
	# designed by required..
	nextVariableAddress = 16

	def register_label(self, label, address):
		self.symbols[label] = address

	def resolve(self, symbol):
		if not symbol in self.symbols:
			self.symbols[symbol] = self.nextVariableAddress
			self.nextVariableAddress += 1
		return self.symbols[symbol]

class CodeWriter:
	def __init__(self, file, symbol_table) -> None:
		self.file = file
		self.symbol_table = symbol_table

	def encode(self, instruction):
		# a instruciton or c instruction
		if instruction[0] == "@":
			self._write(self._encode_a(instruction))
		else:
			self._write(self._encode_c(instruction))

	def _write(self, line):
		self.file.write(line + '\n')

	def _encode_destination(self, destination):
		""" encode destination

			"null": "000",
			"M": "001",
			"D": "010",
			"A": "100",
			"MD": "011",
			"AM": "101",
			"AD": "110",
			"AMD": "111"
		"""
		if destination == None: return '000'
		encoded = ""
		encoded += '1' if "A" in destination else '0'
		encoded += '1' if "D" in destination else '0'
		encoded += '1' if "M" in destination else '0'
		return encoded

	def _encode_opcode(self, opcode):
		"""
		# these three dictionaries store the translations of the 3 parts
		# of a c-instruction
		comp = {
			"0": "0101010",
			"1": "0111111",
			"-1": "0111010",
			"D": "0001100",
			"A": "0110000",
			"!D": "0001101",
			"!A": "0110001",
			"-D": "0001111",
			"-A": "0110011",
			"D+1": "0011111",
			"A+1": "0110111",
			"D-1": "0001110",
			"A-1": "0110010",
			"D+A": "0000010",
			"D-A": "0010011",
			"A-D": "0000111",
			"D&A": "0000000",
			"D|A": "0010101",
			"M": "1110000",
			"!M": "1110001",
			"-M": "1110011",
			"M+1": "1110111",
			"M-1": "1110010",
			"D+M": "1000010",
			"D-M": "1010011",
			"M-D": "1000111",
			"D&M": "1000000",
			"D|M": "1010101"
			}

		"""
		if "M" in opcode:
			opcode = opcode.replace("M", "A")
			firstbit = "1"
		else:
			firstbit = '0'
		if opcode == '0': return firstbit + "101010"
		if opcode == '1': return firstbit + "111111"
		if opcode == '-1': return firstbit + "111010"
		if opcode == 'D': return firstbit + "001100"
		if opcode == 'A': return firstbit + "110000"
		if opcode == '!D': return firstbit + "001101"
		if opcode == '!A': return firstbit + "110001"
		if opcode == '-D': return firstbit + "001111"
		if opcode == '-A': return firstbit + "110011"
		if opcode == 'D+1': return firstbit + "011111"
		if opcode == 'A+1': return firstbit + "110111"
		if opcode == 'D-1': return firstbit + "001110"
		if opcode == 'A-1': return firstbit + "110010"
		if opcode == 'D+A': return firstbit + "000010"
		if opcode == 'D-A': return firstbit + "010011"
		if opcode == 'A-D': return firstbit + "000111"
		if opcode == 'D&A': return firstbit + "000000"
		if opcode == 'D|A': return firstbit + "010101"
		raise Exception("Unknown opcode " + opcode)

	def _encode_jump(self, jump):
		"""
			"null": "000",
			"JGT": "001",
			"JEQ": "010",
			"JGE": "011",
			"JLT": "100",
			"JNE": "101",
			"JLE": "110",
			"JMP": "111"
		"""
		if jump == 'JGT': return "001"
		if jump == 'JEQ': return "010"
		if jump == 'JGE': return "011"
		if jump == 'JLT': return "100"
		if jump == 'JNE': return "101"
		if jump == 'JLE': return "110"
		if jump == 'JMP': return "111"
		return "000"

	def _encode_a(self, instruction):
		address = instruction[1:]
		if not address.isdigit():
			address = self.symbol_table.resolve(address)
		return "{0:016b}".format(int(address))


	def _encode_c(self, instruction):
		if ";" in instruction:
			operation, jump = instruction.split(";")
		else:
			operation = instruction
			jump = ""
		if "=" in operation:
			destination, opcode = operation.split("=")
		else:
			destination = ""
			opcode = operation
		return "111" + self._encode_opcode(opcode) + self._encode_destination(destination) + self._encode_jump(jump)

class Parser:
	def __init__(self, code_writer, symbol_table) -> None:
		self.writer = code_writer
		self.symbol_table = symbol_table

	def parseFile(self, filename):
		# First pass: register labels in symbol table and keep only instructions
		instructions = []
		with open(filename) as file:
			for line in file.readlines():
				line = self._strip(line)
				if len(line):
					if line[0] == '(':
						self.symbol_table.register_label(line[1:-1], len(instructions))
					else:
						instructions.append(line)
		# Second pass: encode instructions
		for instruction in instructions:
			self.writer.encode(instruction)

	def _stip(self, line):
		line = re.sub("//.*", "", line)
		line = re.sub(r"\s", "", line)
		return line

def translate_file(asm_filename):
	hack_file = os.path.splitext(asm_filename)
	with open(hack_file, "w") as asm_file:
		symbol_table = SymbolTable()
		writer = CodeWriter(asm_file, symbol_table)
		parser = Parser(writer, symbol_table)
		parser.parseFile(asm_filename)

def main(argv):
	if len(argv) == 1 and os.path.splitext(argv[0][1] == ".asm"):
		translate_file(argv[0])
	else:
		print("Usage:HackAssembler.py <filename>.asm")
		sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])



























