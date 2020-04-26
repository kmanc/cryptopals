from cryptopals.attacks import xor


class XorAttacks:

	@staticmethod
	def test_xor_break_byte():
		test_in = b"\x1b77316?x\x15\x1b\x7f+x413=x9x(7-6<x7>x:9;76"
		test_correct = {
			"key": b"X",
			"score": 23,
			"result": b"Cooking MC's like a pound of bacon"
		}
		my_output = xor.xor_break_byte_ciphertext(test_in)

		assert my_output == test_correct

	@staticmethod
	def test_xor_break_key_length():
		test_in = b"\x1dH\x01\x12V\x0cSAM\nE\x17\x17\x16\x00iP\x04\x00\x1f\x0bT\x04X\x07KC;\x11T>I\x04\rV\x07EAX\x1c\x17\x06\x16E\x03 T\x00A\x17EK\x04YRDC&\r\x11iO\x06\r\x0fET\tI\x1d\x02C\x1b\x16T=H\t\x15V\x11H\x04\x00\x03\t\x02\x1b\x0b\x00,X\x1cA\x1e\x04SAT\x1cE\x01\x17E\x1f N\x0c\x00V\tO\x0fGS\x16\x0cR\x11\x1c(TH\x15\x1e\x00\x00\x00T\x07\x04\x00\x19E\x17(NH\x05\x19EW\tA\x07E\n\x06E\x1c(SH\x15\x19K\x00(FS\x11\x0b\x17E\x04%A\x01\x0f\x02\x00X\x15\x00\x1a\x16C\x06\n\x1biS\x00\x0e\x04\x11\x0cAT\x1b\x00C\x13\x11\x00(C\x03A\x1b\x0cG\tTS\x03\x02\x1b\tZiiH\x16\x1f\tLAA\x1f\x16\x0cR\x06\x1c&O\x1b\x04V\x04\x00\x12E\x1e\x0cN\x1e\n\x1a.\x00\x03\x04\x0fEB\x04C\x12\x10\x10\x17E\x03!YH\x0f\x19\x11\x1fAi\x15E\x1a\x1d\x10T:U\x1b\x11\x13\x06TAT\x1b\x04\x17R\x00\x1d=H\r\x13V\x11H\x04YS\x0e\x06\x0bE\x1b;\x00\x1c\t\x13EP\rA\x1a\x0b\x17\x17\x1d\x00iI\x1bA\x05\rO\x13T_E\n\x06E\x1d:\x00\x18\x13\x19\x07A\x03L\nE\x01\x17\x16\x00iT\x07A\x1c\x10S\x15\x00\x11\x17\x16\x06\x00T/O\x1a\x02\x13ET\tES\x12\x0b\x1d\t\x11iT\x00\x08\x18\x02\x0eAi\x07E\x0e\x13\x1cT:E\r\x0cV\x12E\x08R\x17E\x01\x07\x11T>H\r\x0fV\x0cTAC\x1c\x08\x06\x01E\x00&\x00\x10\x0e\x04I\x00\x15H\x16\x17\x06R\x0c\x07iR\r\x00\x1a\tYAN\x1cE\x07\x1b\x03\x12,R\r\x0f\x15\x00\x00\x03E\x07\x12\x06\x17\x0bT=H\rA\x06\tA\x08N\x07\x00\x1b\x06E\x15'DH\x15\x1e\x00\x00\nE\nEK\x1f\n\x06,\x00\x07\x0fV\x11H\x00TS\x16\x0c\x1f\x00T&T\x00\x04\x04ET\x08M\x16LM"
		test_correct = {
			"first": 30,
			"second": 15,
			"third": 10
		}
		my_output = xor.xor_break_key_length(test_in)

		assert my_output == test_correct

	@staticmethod
	def test_xor_break_keyed():
		test_in = b"\x1dH\x01\x12V\x0cSAM\nE\x17\x17\x16\x00iP\x04\x00\x1f\x0bT\x04X\x07KC;\x11T>I\x04\rV\x07EAX\x1c\x17\x06\x16E\x03 T\x00A\x17EK\x04YRDC&\r\x11iO\x06\r\x0fET\tI\x1d\x02C\x1b\x16T=H\t\x15V\x11H\x04\x00\x03\t\x02\x1b\x0b\x00,X\x1cA\x1e\x04SAT\x1cE\x01\x17E\x1f N\x0c\x00V\tO\x0fGS\x16\x0cR\x11\x1c(TH\x15\x1e\x00\x00\x00T\x07\x04\x00\x19E\x17(NH\x05\x19EW\tA\x07E\n\x06E\x1c(SH\x15\x19K\x00(FS\x11\x0b\x17E\x04%A\x01\x0f\x02\x00X\x15\x00\x1a\x16C\x06\n\x1biS\x00\x0e\x04\x11\x0cAT\x1b\x00C\x13\x11\x00(C\x03A\x1b\x0cG\tTS\x03\x02\x1b\tZiiH\x16\x1f\tLAA\x1f\x16\x0cR\x06\x1c&O\x1b\x04V\x04\x00\x12E\x1e\x0cN\x1e\n\x1a.\x00\x03\x04\x0fEB\x04C\x12\x10\x10\x17E\x03!YH\x0f\x19\x11\x1fAi\x15E\x1a\x1d\x10T:U\x1b\x11\x13\x06TAT\x1b\x04\x17R\x00\x1d=H\r\x13V\x11H\x04YS\x0e\x06\x0bE\x1b;\x00\x1c\t\x13EP\rA\x1a\x0b\x17\x17\x1d\x00iI\x1bA\x05\rO\x13T_E\n\x06E\x1d:\x00\x18\x13\x19\x07A\x03L\nE\x01\x17\x16\x00iT\x07A\x1c\x10S\x15\x00\x11\x17\x16\x06\x00T/O\x1a\x02\x13ET\tES\x12\x0b\x1d\t\x11iT\x00\x08\x18\x02\x0eAi\x07E\x0e\x13\x1cT:E\r\x0cV\x12E\x08R\x17E\x01\x07\x11T>H\r\x0fV\x0cTAC\x1c\x08\x06\x01E\x00&\x00\x10\x0e\x04I\x00\x15H\x16\x17\x06R\x0c\x07iR\r\x00\x1a\tYAN\x1cE\x07\x1b\x03\x12,R\r\x0f\x15\x00\x00\x03E\x07\x12\x06\x17\x0bT=H\rA\x06\tA\x08N\x07\x00\x1b\x06E\x15'DH\x15\x1e\x00\x00\nE\nEK\x1f\n\x06,\x00\x07\x0fV\x11H\x00TS\x16\x0c\x1f\x00T&T\x00\x04\x04ET\x08M\x16LM"
		test_correct = {
			"key": b"I have a secret",
			"result": b'This is my test plaintext. It will be xored with a key!! The only thing is that the plaintext has to be kinda long so that the attack can do what it has to. If the plaintext is too short, the attack might fail. I will also choose a semi-long key because why not? If you suspect that either they key or the plaintext is short, it is probably best to just brute force the whole thing. It may seem weird but when it comes to xor, there is really no difference between the plaintext and the key (more on that some other time).'
		}
		my_output = xor.xor_break_keyed_ciphertext(test_in)

		assert my_output == test_correct
