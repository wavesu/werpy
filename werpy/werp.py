import numpy as np
from metrics import metrics


def werp(reference, hypothesis, insertions_weight=1, deletions_weight=1, substitutions_weight=1):
    """
    This function calculates a weighted Word Error Rate for the entire reference and hypothesis texts. It allows the
    insertion, deletion and substitution errors to be penalized or weighted at different rates.

    Parameters
    ----------
    reference : str, list or numpy array
        The ground truth transcription of a recorded speech or the expected output of a live speech.
    hypothesis : str, list or numpy array
        The text generated by a speech-to-text algorithm/system which will be compared to the reference text.
    insertions_weight: int or float, optional
        The weight multiplier for an insertion error
    deletions_weight: int or float, optional
        The weight multiplier for a deletion error
    substitutions_weight: int or float, optional
        The weight multiplier for a substitution error

    Raises
    ------
    ValueError
        if the two input parameters do not contain the same amount of elements.
    AttributeError
        if input text is not a string, list or np.ndarray data type.

    Returns
    -------
    float
        This function will return a single weighted Word Error Rate.

    Examples
    --------
    >>> ref = ['it was beautiful and sunny today']
    >>> hyp = ['it was a beautiful and sunny day']

    >>> werp_example_1 = werp(ref, hyp)
    >>> print(werp_example_1)
    0.3333333333333333

    >>> werp_example_2 = werp(ref, hyp, insertions_weight=1, deletions_weight=1, substitutions_weight=1)
    >>> print(werp_example_2)
    0.3333333333333333

    >>> werp_example_3 = werp(ref, hyp, insertions_weight=0.5, deletions_weight=0.5, substitutions_weight=1)
    >>> print(werp_example_3)
    0.25

    >>> werp_example_4 = werp(ref, hyp, 0.5, 0.5, 1)
    >>> print(werp_example_4)
    0.25
    """
    try:
        word_error_rate_breakdown = metrics(reference, hypothesis)
    except ValueError:
        print("ValueError: The Reference and Hypothesis input parameters must have the same number of elements.")
    except AttributeError:
        print(
            "AttributeError: All text should be in a string format. Please check your input does not include any "
            "Numeric data types.")
    else:
        if type(word_error_rate_breakdown[0]) == np.ndarray:
            transform_word_error_rate_breakdown = np.transpose(word_error_rate_breakdown.tolist())
            weighted_insertions = transform_word_error_rate_breakdown[3] * insertions_weight
            weighted_deletions = transform_word_error_rate_breakdown[4] * deletions_weight
            weighted_substitutions = transform_word_error_rate_breakdown[5] * substitutions_weight
            m = np.sum(transform_word_error_rate_breakdown[2])
        else:
            weighted_insertions = word_error_rate_breakdown[3] * insertions_weight
            weighted_deletions = word_error_rate_breakdown[4] * deletions_weight
            weighted_substitutions = word_error_rate_breakdown[5] * substitutions_weight
            m = np.sum(word_error_rate_breakdown[2])

        weighted_errors = np.sum([weighted_insertions, weighted_deletions, weighted_substitutions])
        werp_result = weighted_errors / m
        return werp_result