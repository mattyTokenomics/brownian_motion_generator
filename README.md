# Intro

Library of functions to generate Brownian motion random walks for multiple series that exhibit mean reversion, correlation, skew, kurtosis, and/or custom distributions that do not follow typical normal distributions.

This can be used for testing trading straggles, risk analysis, tokenomics design stress testing, Monte Carlo simulations, and inputs into existing testing, modeling, and simulation frameworks such as cadCAD and radCAD - see the Examples folder for details.

# Installation

To install, run:
`pip install brownian-motion-generator`

https://pypi.org/project/brownian-motion-generator/

# Common Use Cases

- Stress testing collateral based systems. Generating random walks of asset prices can help to identify potential exploits or risks of undercollateralization.
- Optimizing rates of emission/inflation. Generating random walks of TVL/users/revenue growth can help to identify how emissions may need to be tweaked.
- Identifying critical thresholds. Generating random walks of user activity, TVL, and/or protocol revenues can help identify any crucial levels to hit (or avoid) where sustainable growth kicks in (or death spiral feedback loops begin).
- Understanding risks and levels of exposure to general market conditions or the performance of a given asset outside your control. Generating random walks of S&P 500 or BTC prices can help identify the degree and critical levels in macro risks.
- Model positive feedback loops and/or death spirals in user behavior. For example generating random walks of NFT marketplace trading activity helps protocols identify and minimize the risks of wash trading.
- Assumption testing. Generating random walks of critical model inputs can stress test any general system design to identify which assumptions must hold true for the system to be sustainable, and/or identity any assumptions which are unlikely to hold true in practice based on realistic random walks.

# How to Use

See the examples folder for tutorials in Jupyter notebook and equivalent html file format. Tutorials cover quick examples of generating multiple simulations of multiple correlated series with mean reverting, correlated, and/or non-normal distributions of returns, and how to integrate the generated random walks into existing simulation frameworks such as radCAD.

# Feedback, Questions, Improvements?

Please open an issue on GitHub or [get in touch](https://linktr.ee/tokenomics).

# Credits

Original credit to these two resources which were the building blocks:
- https://towardsdatascience.com/stochastic-processes-simulation-brownian-motion-the-basics-c1d71585d9f9
- https://gist.github.com/raddy/4084ade3d3a82911d43df9375f9697f4


