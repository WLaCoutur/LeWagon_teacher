# Scatter Plot
### Introduction

In this exercise, we are going to **recreate** plots from this [article](https://www.data-to-viz.com/story/ThreeNum.html).

To learn more **best practices** around bubble plots, read these **3 short articles**.

[Radius or Area](https://www.data-to-viz.com/caveat/radius_or_area.html),
[Area readability](https://www.data-to-viz.com/caveat/area_hard.html),
[Overplotting](https://www.data-to-viz.com/caveat/overplotting.html)

### Dataset

You will work with the **GDP per capita** dataset. You can find it [here](https://wagon-public-datasets.s3.amazonaws.com/02-Data-Toolkit/03-Data-Visualization/4_ThreeNum.csv).

### First steps

Open a notebook named `scatter_plot.ipynb` in the **same folder** as this **README**.
Now you can **import** the necessary **libraries**.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
```

Then **import** the **dataset** from  [here](https://wagon-public-datasets.s3.amazonaws.com/02-Data-Toolkit/03-Data-Visualization/4_ThreeNum.csv) in your challenge folder as `gdp_df`.

### Part 1

Try to recreate **approximately** this bubble plot using seaborn

<img src="https://wagon-public-datasets.s3.amazonaws.com/data-science-images/02-Data-Toolkit/03-Data-Visualization/country-plots-part-1.png" width="760">

<details>
  <summary markdown='span'>💡Hints</summary>
  <ul>
    <li>The colors of the bubbles are for the different continents</li>
    <li>You will need to use <code>hue</code> and <code>size</code> arguments</li>
    <li>You will have to adjust bubble size with <code>sizes</code></li>
    <li>You can adjust the legend with <code>bbox_to_anchor</code> and <code>loc</code> argument</li>
    <li>You can change axes visibility with <code>Axes.spines()</code></li>
    <li>You can display the grid with <code>Axes.grid()</code></li>
    <li>You can change ticks aspect with <code>Axes.tick_params()</code></li>
    <li><code>handles, labels = ax.get_legend_handles_labels()</code> could be helpful</li>
    <li>You can change the <code>palette</code> of colors</li>
  </ul>
</details>

### Part 2

Now add country name as **labels** for the countries where both:
- the gdp per capita is greater than **5000**.
- the life expectancy is smaller than **65** years old.

<img src="https://wagon-public-datasets.s3.amazonaws.com/data-science-images/02-Data-Toolkit/03-Data-Visualization/country_plots.png" width="760">

<details>
  <summary markdown='span'>💡Hint</summary>
  You can use <code>Axes.text()</code> and <code>DataFrame.iterrows()</code>
</details>

### Part 3

We will now use [Plotly](https://plot.ly/python/bubble-charts/) to create an **interactive** plot.
That way we will be able to:
- zoom in the chart
- lookup values for each data point


<img src="https://wagon-public-datasets.s3.amazonaws.com/data-science-images/02-Data-Toolkit/03-Data-Visualization/country-plots-part-3.png" width="760">
