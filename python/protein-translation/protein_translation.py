from itertools import takewhile, islice


def proteins(rna_seq):
    """Translates RNA sequences into proteins.

    The implementation uses generators and thus would, in theory, be used with a huge chain of codons. However, because it has to return a  list object this generator is consumed completed which might a lot of memory with long chains of codens. Ideally, it would return a generator.

    Parameters
    ----------
    rna_seq (string):
        A RNA sequence of codons, each codon is a sequence of 3 nucleotides.

    Returns
    -------
    list
        a list representing a protein (polypeptide).
    """
    codon_indexes = get_codon_indexes(rna_seq)
    codons = (rna_seq[i : i + 3] for i in codon_indexes)
    protein = (get_amino_acid(codon) for codon in codons)
    return list(takewhile(lambda x: x != "STOP", protein))


def get_codon(rna_seq, codon_index):
    return rna_seq[codon_index : codon_index + 3]


def get_amino_acid(codon):
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
    return codon_to_protein[codon]


def get_codon_indexes(rna_seq):
    i = 0
    while i < len(rna_seq):
        yield i
        i += 3
