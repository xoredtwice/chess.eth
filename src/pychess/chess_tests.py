
def king_tests():
	print_board(king("A4"))
	print_board(king("A5"))
	print_board(king("A7"))
	print_board(king("A8"))
	print_board(king("B8"))
	print_board(king("C8"))
	print_board(king("D8"))
	print_board(king("F8"))
	print_board(king("G8"))
	print_board(king("H8"))
	print_board(king("H7"))
	print_board(king("H6"))
	print_board(king("H3"))
	print_board(king("H2"))
	print_board(king("H1"))
	print_board(king("G1"))
	print_board(king("F1"))
	print_board(king("C1"))
	print_board(king("B1"))

	print_board(king("B2"))
	print_board(king("D4"))
	print_board(king("E4"))
	print_board(king("G6"))

def knight_tests():
	print("A4")
	print_board(knight("A4"))
	print("A5")
	print_board(knight("A5"))
	print("A7")
	print_board(knight("A7"))
	print("A8")
	print_board(knight("A8"))
	print("B8")
	print_board(knight("B8"))
	print("C8")
	print_board(knight("C8"))
	print("D8")
	print_board(knight("D8"))
	print("F8")
	print_board(knight("F8"))
	print("G8")
	print_board(knight("G8"))
	print("H8")
	print_board(knight("H8"))
	print("H7")
	print_board(knight("H7"))
	print("H6")
	print_board(knight("H6"))
	print("H3")
	print_board(knight("H3"))
	print("H2")
	print_board(knight("H2"))
	print("H1")
	print_board(knight("H1"))


def build_mesh1_masks():
	# A1
	mask = build_mask(["A2", "B2", "B1"])
	# print_board(parse_visibility(mask))
	print(f"'*A1' : {hex(mask)},")

	# A2
	mask = build_mask(["A1", "B1", "B2", "B3", "A3"])
	# print_board(parse_visibility(mask))
	print(f"'*A2' : {hex(mask)},")

	# A8
	mask = build_mask(["A7", "B7", "B8"])
	# print_board(parse_visibility(mask))
	print(f"'*A8' : {hex(mask)},")

	# B8
	mask = build_mask(["A8", "A7", "B7", "C7", "C8"])
	# print_board(parse_visibility(mask))
	print(f"'*B8' : {hex(mask)},")

	# H8
	mask = build_mask(["H7", "G7", "G8"])
	# print_board(parse_visibility(mask))
	print(f"'*H8' : {hex(mask)},")

	# H2
	mask = build_mask(["H1", "G1", "G2", "G3", "H3"])
	# print_board(parse_visibility(mask))
	print(f"'*H2' : {hex(mask)},")

	# H1
	mask = build_mask(["H2", "G2", "G1"])
	# print_board(parse_visibility(mask))
	print(f"'*H1' : {hex(mask)},")

	# B1
	mask = build_mask(["A1", "A2", "B2", "C2", "C1"])
	# print_board(parse_visibility(mask))
	print(f"'*B1' : {hex(mask)},")


	# B2
	mask = build_mask(["A1", "A2", "A3", "B3", "C3", "C2", "C1", "B1"])
	# print_board(parse_visibility(mask))
	print(f"'*B2' : {hex(mask)},")
# build_diagonal_masks()
# build_mesh1_masks()


def build_8way_masks():
	for sq in SQUARE_IDS.keys():
		f_code = sq[0]
		r_code = sq[1]
		d_codes = SQUARE_DIAGS[sq]
		d1_code = f"+{(d_codes % 16)}"
		d2_code = f"-{(d_codes // 16)}"		
		# print(f"Visibility of File:{f_code}, Rank:{r_code}")
		# print(f"Visibility of  D+:{d1_code}, D-:{d2_code}")

		m = {}
		sqm = build_mask([sq])
		m["W"] = MASKS[r_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["E"] = MASKS[r_code] & (~m["W"]) & (~sqm)

		m["S"] = MASKS[f_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["N"] = MASKS[f_code] & (~m["S"]) & (~sqm)

		m["NW"] = MASKS[d1_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["SE"] = MASKS[d1_code] & (~m["NW"]) & (~sqm)

		m["SW"] = MASKS[d2_code] & ((1 << SQUARE_IDS[sq]) - 1 )
		m["NE"] = MASKS[d2_code] & (~m["SW"]) & (~sqm)
		for direction in m.keys():
			print(f"MASK['{direction}']['{sq}'] = {hex(m[direction])}")
			# print_board(m[direction])

def build_diagonal_masks():
	d1 = build_mask(["A1"])
	# print_board(parse_visibility(d1))
	print(f"'+1' : {hex(d1)},")

	d2 = d1
	di = 2
	for i in range(7):
		d2 = (d2 | (0x80 << (i*8))) << 1
		# print_board(parse_visibility(d2))
		print(f"'+{di}' : {hex(d2)},")
		di = di + 1

	for i in range(7):
		d2 = (d2 & ~(0x80 << (i*8))) << 1
		# print_board(parse_visibility(d2))
		print(f"'+{di}' : {hex(d2)},")
		di = di + 1

	d16 = build_mask(["H1"])
	# print_board(parse_visibility(d16))
	print(f"'-1': {hex(d2)},")

	d2 = d16
	di = 2
	for i in range(7):
		d2 = (d2  << 1) | (0x01 << ((6-i)*8))
		# print_board(parse_visibility(d2))
		print(f"'-{di}': {hex(d2)},")
		di = di + 1

	for i in range(7):
		d2 = (d2 << 1) & ~(0x101010101010101)
		# print_board(parse_visibility(d2))
		print(f"'-{di}': {hex(d2)},")
		di = di + 1
