
def test_msb():
	for i in range(1024):
		print(f"{i}: {msb64(i)}")
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
##########################################################
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
##########################################################
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
##########################################################
