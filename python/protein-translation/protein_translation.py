import itertools


def proteins(strand):
    """Translates RNA sequences into proteins.

    Parameters
    ----------
    strand (string):
        A RNA sequence of codons, each codon is a sequence of 3 nucleotides.

    Returns
    -------
    list
        a list of proteins (polypeptide).
    """
    codon_to_protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
    indexes = range(len(strand))[::3]
    proteins = map(lambda i: codon_to_protein[strand[i : i + 3]], indexes)
    return list(itertools.takewhile(lambda x: x != "STOP", proteins))
