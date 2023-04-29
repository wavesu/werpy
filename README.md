
![werpy-logo-word-error-rate](https://user-images.githubusercontent.com/52817125/235063664-2f21629c-0fad-46b6-a487-c2b5ef6f80e9.png)
# werpy - Word Error Rate for Python
<!-- badges: start -->
[![Python Version](https://img.shields.io/badge/python-3.8%7C3.9%7C3.10%7C3.11-blue?logo=python&logoColor=ffdd54)](https://www.python.org/downloads/)&nbsp;&nbsp;
[![werpy License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://github.com/analyticsinmotion/werpy/blob/main/LICENSE)&nbsp;&nbsp;
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)&nbsp;&nbsp;
[![CodeQL](https://github.com/analyticsinmotion/werpy/actions/workflows/codeql.yml/badge.svg)](https://github.com/analyticsinmotion/werpy/actions/workflows/codeql.yml)&nbsp;&nbsp;
<!-- badges: end -->

## What is it?
**werpy** is a powerful yet lightweight Python package that rapidly calculates and analyzes the Word Error Rate (WER) between two sets of text. 
It has been designed with the flexibility to handle multiple input data types such as strings, lists and numpy arrays.<br />

The package also includes a full set of features such as normalizing the input text to account for data collection variability and the capability to easily assign different weights/penalties to specific error classifications (insertions, deletions, and substitutions).
Additionally, the summary function provides a comprehensive breakdown of the calculated results to assist in analyzing the specific errors quickly and in more detail.
<br />

## Installation
You can install the latest **werpy** release with Python's pip package manager:

```python
# install werpy via PyPi
pip install werpy
```

## Main Functions
The following table provides an overview of the functions that can be used in werpy.

| Function  | Description | 
| ------------- | ------------- |
| normalize(text)  | Preprocess input text to remove punctuation, remove duplicated spaces, leading/trailing blanks and convert all words to lowercase. |
| wer(reference, hypothesis)  | Calculate the overall Word Error Rate for the entire reference and hypothesis texts. |
| wers(reference, hypothesis)  | Calculates a list of the Word Error Rates for each of the reference and hypothesis texts. |
| werp(reference, hypothesis)  | Calculates a weighted Word Error Rate for the entire reference and hypothesis texts. |
| werps(reference, hypothesis)  | Calculates a list of weighted Word Error Rates for each of the reference and hypothesis texts. |
| summary(reference, hypothesis)  | Provides a comprehensive breakdown of the calculated results including the WER, Levenshtein Distance and all the insertion, deletion and substitution errors. |


## Usage
**Import the werpy package**
```python
>>> import werpy
```

**Example 1 - Normalize a list of text**
```python
>>> input_data = ["It's very popular in Antarctica.","The Sugar Bear character"]
>>> reference = werpy.normalize(input_data)
>>> print(reference)
['its very popular in antarctica', 'the sugar bear character']
```

**Example 2 - Calculate the overall Word Error Rate on a set of strings**
```python
>>> wer = werpy.wer('i love cold pizza', 'i love pizza')
>>> print(wer)
0.25
```

**Example 3 - Calculate the overall Word Error Rate on a set of lists**
```python
>>> ref = ['i love cold pizza','the sugar bear character was popular']
>>> hyp = ['i love pizza','the sugar bare character was popular']
>>> wer = werpy.wer(ref, hyp)
>>> print(wer)
0.2
```

**Example 4 - Calculate the Word Error Rates for each set of texts**
```python
>>> ref = ['no one else could claim that','she cited multiple reasons why']
>>> hyp = ['no one else could claim that','she sighted multiple reasons why']
>>> wers = werpy.wers(ref, hyp)
>>> print(wers)
[0.0, 0.2]
```

**Example 5 - Calculate the weighted Word Error Rates for the entire set of text**
```python
>>> ref = ['it was beautiful and sunny today']
>>> hyp = ['it was a beautiful and sunny day']
>>> werp = werpy.werp(ref, hyp, insertions_weight=0.5, deletions_weight=0.5, substitutions_weight=1)
>>> print(werp)
0.25
```

**Example 6 - Calculate a list of weighted Word Error Rates for each of the reference and hypothesis texts**
```python
>>> ref = ['it blocked sight lines of central park', 'her father was an alderman in the city government']
>>> hyp = ['it blocked sightlines of central park', 'our father was an elder man in the city government']
>>> werps = werpy.werps(ref, hyp, insertions_weight = 0.5, deletions_weight = 0.5, substitutions_weight = 1)
>>> print(werps)
[0.21428571428571427, 0.2777777777777778]
```

**Example 7 - Provide a complete breakdown of the Word Error Rate calculations for each of the reference and hypothesis texts**
```python
>>> ref = ['it is consumed domestically and exported to other countries', 'rufino street in makati right inside the makati central business district', 'its estuary is considered to have abnormally low rates of dissolved oxygen', 'he later cited his first wife anita as the inspiration for the song', 'no one else could claim that']
>>> hyp = ['it is consumed domestically and exported to other countries', 'rofino street in mccauti right inside the macasi central business district', 'its estiary is considered to have a normally low rates of dissolved oxygen', 'he later sighted his first wife anita as the inspiration for the song', 'no one else could claim that']
>>> summary = werpy.summary(ref, hyp)
>>> print(summary)
```
<!-- <img src=".github/assets/images/werpy-example-summary-results-word-error-rate-breakdown.png" width=100% height=100%> -->
<!-- <img src="https://github.com/analyticsinmotion/werpy/blob/main/.github/assets/images/werpy-example-summary-results-word-error-rate-breakdown.png" width=100% height=100%> -->
<!-- ![werpy summary DataFrame](.github/assets/images/werpy-example-summary-results-word-error-rate-breakdown.png)-->

![werpy-example-summary-results-word-error-rate-breakdown](https://user-images.githubusercontent.com/52817125/234950114-7efcce9b-7a76-4413-830f-7deda20cad75.png)



## Dependencies
 - <a href="https://www.numpy.org">NumPy</a> - Provides an assortment of routines for fast operations on arrays
 - <a href="https://pandas.pydata.org/">Pandas</a> - Powerful data structures for data analysis, time series, and statistics

## Licensing

``werpy`` is released under the terms of the BSD 3-Clause License. Please refer to the LICENSE file for full details.

This project also includes third-party packages distributed under the BSD-3-Clause license, including NumPy and Pandas.

The full NumPy and Pandas licenses can be found in the <a href="https://github.com/analyticsinmotion/werpy/tree/main/LICENSES">LICENSES</a> directory in this repository. 

They can also be found directly in the following source codes:

 - NumPy - <a href="https://github.com/numpy/numpy/blob/main/LICENSE.txt">https://github.com/numpy/numpy/blob/main/LICENSE.txt</a>
 - Pandas - <a href="https://github.com/pandas-dev/pandas/blob/main/LICENSE">https://github.com/pandas-dev/pandas/blob/main/LICENSE</a>

