👏 Congratulations for coding your first Convolutional Neural Networks !

👨🏻‍🏫 For the recap session, let's take a look at the following ideas:

- 😇 __1️⃣ Cats and Dogs:__ A walkthrough of the full process of loading data, comparing different vision models, seeing the benefits of transfer learning and data augmentation, saving/ loading models, then predicting on some data in the wild!

- 🤯 **3️⃣. (Optional Bonus)** Let's review together the challenge `05-Autoencoders`!

<br><br>
🏎️ Run this notebook preferably on Colab or Kaggle with GPU accelaration

<details><summary>⚙️ Working configurations on Colab and Kaggle
</summary>
<ul>
<li>
<strong>Colab</strong>: <code>tensorflow==2.15.0</code>, <code>keras==2.15.0</code>
</li>
<li>
<strong>Kaggle</strong>: <code>tensorflow==2.15.0</code>, <code>keras==3.3.3</code>
</li>
</ul>

These are the configurations at the time of writing (04/07/2024).
</details>

<details><summary>⚙️ Running locally on Apple Silicon
</summary>
<ul>
<li>
Notebook runs with <code>tensorflow-macos==2.10.0</code> but training is slow on models 2 and 3 (because of issues at tensorflow / keras side). GPU acceleration with <code>tensorflow-metal=0.6.0</code> works but doesn't speed up models 2 and 3.
</li>
<li>
Notebook runs with <code>tensorflow==2.16.1</code> and <code>keras==3.3.3</code> but can't use GPU accelaration because there is no compatible <code>tensorflow-metal</code> yet (04/07/2024).
</li>
<li>
<strong>A working configuration with GPU</strong> accelaration is <code>tensorflow-macos==2.13.1</code>, <code>keras==2.13.1</code>, <code>tensorflow-metal==1.0.0</code>.
</details>
</li>
</ul>
