def find_vowels(phrase: str) -> set:
    """Returns any vowels that appear in provided phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def find_letters(phrase: str, letters: str='aeiou') -> set:
    """Returns set of 'letters' that appear in 'phrase'.
       Omitting 'letters' will search vowels."""
    return set(letters).intersection(set(phrase))
