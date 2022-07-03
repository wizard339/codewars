"""
There is an array of strings. All strings contains similar letters except one.
Try to find it!

Examples:

findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) === 'BbBb'
findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) === 'foo'

Strings may contain spaces. Spaces are not significant, only non-spaces symbols
matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.
"""
import doctest


def find_uniq(arr):
    """
    :param arr: an array of strings, all strings contains similar letters except one
    :return: an array element that contains dissimilar letters than other array elements
    -----------
    Doctest tests:
        >>> find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
        'BbBb'
        >>> find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
        'foo'
    """
    for i in range(2, len(arr)):
        x = set(arr[i - 2].lower())
        y = set(arr[i - 1].lower())
        z = set(arr[i].lower())

        if x != y and x != z:
            return arr[i - 2]
        elif x == y and x != z:
            return arr[i]
        elif x != y and x == z:
            return arr[i - 1]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
