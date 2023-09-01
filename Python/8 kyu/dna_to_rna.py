def dna_to_rna(dna: str) -> str:
    """
        This functions translates a given DNA string into RNA

    Args:
        dna (str): DNA string

    Returns:
        str: RNA string
    """        
    return dna.replace("T","U")
    

if __name__ == "__main__":
    assert dna_to_rna("TTTT") == "UUUU"
    assert dna_to_rna("GCAT") == "GCAU"
    assert dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"
    print("All tests passed")