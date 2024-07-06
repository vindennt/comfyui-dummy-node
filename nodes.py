class Test:
    RETURN_TYPES = ("FLOAT",)
    INPUT_TYPES = ""
    FUNCTION="TEST"
    
    def TEST():
	    print("[stanleyui] calling TEST")

NODE_CLASS_MAPPINGS = {
    "test": Test
}