# Eikosograms
Inspired by [R eikosograms](https://cran.r-project.org/web/packages/eikosograms/vignettes/Introduction.html), I decided to create a similar library for Python since there was no such library at the time (only a few crude implementations: [[1]](https://andrewtruong.com/data_visualization), [[2]](https://github.com/wtsi-hgi/spack-repo/blob/b5bd14ed3a34bae3ad4677be09af070f0f544293/packages/r-eikosograms/package.py#L9)). 

Also, I created [interactive visualization](https://www.desmos.com/calculator/81hy17u2bt) in Desmos.

## Install
```
pip install eikosograms
```

## Usage
```python
>>> from eikosograms import eikosograms
>>> eikosogram.draw_chart(.8, .3, .4, names=('Rain', 'Cloudy'), min_labels=False)
```
Check function docstring for more details.