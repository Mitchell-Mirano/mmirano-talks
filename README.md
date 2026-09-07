# mmirano-talks

Repository that centralizes my academic talks and conference presentations written in LaTeX. It includes technical and outreach sessions on artificial intelligence, machine learning, scientific computing, and research-oriented software development. Each event contains the complete LaTeX source, graphic resources, auxiliary code, and the final compiled PDF ready for distribution.


## Repository Structure

```
.
├── <year>/             # Year of the talk or academic event
│   └── <event-name>/   # Specific conference, workshop, or seminar
│       ├── images/     # Figures, diagrams, and visual resources
│       ├── src/        # Notebooks, scripts, and supporting material
│       ├── veamer.tex  # Main presentation source
│       ├── veamer.pdf  # Compiled presentation
├── main.py             # General-purpose automation tools (optional)
├── pyproject.toml      # Python environment and project metadata
├── uv.lock             # Reproducible environment lockfile
├── LICENSE             # Dual-license specification
└── README.md           # Repository documentation

```

## Purpose of the Repository

This repository is designed to:

* Maintain a consolidated and reproducible record of my academic talks.
* Enable open distribution of scientific and educational material.
* Standardize the development of research-oriented presentations.
* Integrate code, simulations, and analyses directly into the LaTeX workflow.
* Build a verifiable portfolio of my work as a speaker in AI, ML, scientific computing, and research software engineering.


## Conference Catalog

Below is a list of the conferences included in this repository. Each entry provides the title, date, and a brief academic description.

## 2026 – World Youth Festival (WYF 2026 – Ekaterinburg, Russia)

* **Directory**: [2026-wyf-ekaterinburg](https://github.com/Mitchell-Mirano/mmirano-talks/tree/main/2026/wyf-ekaterinburg)
* **Title**: *Beyond Heavy Frameworks: Efficient Machine Learning and Autograd with Sorix, NumPy, and CuPy*
* **Language**: English (EN)
* **Date**: 2026
* **Venue**: World Youth Festival (WYF 2026) – Ekaterinburg, Russian Federation
* **Platform & Documentation**: [sorix.mitchellmirano.com](https://sorix.mitchellmirano.com)
* **Description**: International technical presentation focused on computational autograd mechanics, efficient neural network computing, and democratizing artificial intelligence. The session details how dynamic computational graphs are executed in reverse-mode automatic differentiation, the unified `xp` backend architecture leveraging [NumPy](https://numpy.org/) and [CuPy](https://cupy.dev/), and low-level memory and tensor optimizations in [sorix](https://github.com/Mitchell-Mirano/sorix). It presents benchmark evidence demonstrating that Sorix outperforms PyTorch in CPU training for standard models while slashing system footprint by ~13x to ~28x (54 MB vs 6.8 GB), making it an ideal engine for edge AI and accessible education without high-end clusters.



## 2025 – Scientific Computing Week (UNMSM)

* **Directory**: [2025-11-semana-computacion-cientifica](https://github.com/Mitchell-Mirano/mmirano-talks/tree/main/2025/semana-computacion-cientifica)

* **Title**: *Beyond PyTorch: Building a Machine Learning Engine with NumPy and CuPy*
* **Language**: Spanish (ES)

* **Date**: November 12, 2025

* **Institution**: [Faculty of Mathematical Sciences – UNMSM](https://matematicas.unmsm.edu.pe/)

* **Description**: Academic lecture focused on the mathematical and computational construction of [sorix](https://github.com/Mitchell-Mirano/sorix), a minimalist machine learning engine implemented using [NumPy](https://numpy.org/) and [CuPy](https://cupy.dev/). The talk covers the formal foundations of autograd, neural network architecture, and optimization principles required to design a high-performance framework capable of running on both CPU and GPU.



## 2025 – New Lines of Research (UNMSM)

* **Directory**: [2025-11-new-lines-of-research](https://github.com/Mitchell-Mirano/mmirano-talks/tree/main/2025/nuevas-lineas-de-investigacion)

* **Title**: *From Physics to Machine Learning: Applications in Industrial Process Prediction and Optimization*

* **Language**: Spanish (ES)

* **Date**: November 21, 2025

* **Institution**: [Faculty of Physical Sciences – UNMSM](https://fisica.unmsm.edu.pe/)

* **Description**: Academic lecture focused on the connection between fundamental physics principles and machine learning. The session covered the mathematical foundations of ML, modeling paradigms, and its formulation as an optimization problem. Two real industrial case studies were presented (IT request classification and operational time prediction in concrete logistics), demonstrating quantitative improvements through supervised models and deep learning techniques. Finally, it examined how physical concepts such as energy, diffusion, symmetries, and the principle of least action support the modern design of ML architectures and training algorithms.



## Compiling Presentations

Navigate to any event directory (e.g., the 2026 World Youth Festival talk):

```bash
cd 2026/wyf-ekaterinburg
latexmk -pdf veamer.tex
```

Alternatively, using `uv`:

```bash
uv run latexmk -pdf veamer.tex
```

The resulting compiled slide deck will be `veamer.pdf`.


## Requirements

* Full LaTeX distribution (TeX Live or MiKTeX).
* Python 3.12+ for optional utility scripts.
* `uv` for environment management (optional).

Install the environment:

```bash
uv sync
```


## License

The content is distributed under the terms of the MIT License, as described in the `LICENSE` file.
