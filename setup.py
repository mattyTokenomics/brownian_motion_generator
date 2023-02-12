import setuptools

setuptools.setup(
    name='brownian_motion_generator',
    version='1.0.3',
    author='MattyTokenomics',
    author_email='mattytokenomics@protonmail.com',
    description='Generating brownian motion random walks with custom skew, kurtosis, mean reversion, correlation, and non-normality.',
    readme = "README.md",
    url='https://github.com/mattyTokenomics/brownian_motion_generator',
    project_urls = {},
    license='GNU General Public License v3.0',
    packages=['brownian_motion_generator'],
    install_requires=['typing',
    'dataclasses',
    'sklearn',
    'numpy',
    'scipy',
    'statsmodels',
    'tqdm',
    'warnings'],
)