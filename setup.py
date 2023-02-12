import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='brownian_motion_generator',
    version='1.0.0',
    author='MattyTokenomics',
    author_email='mattytokenomics@protonmail.com',
    description='Generating brownian motion random walks with custom skew, kurtosis, mean reversion, correlation, and non-normality.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mattyTokenomics/brownian_motion_generator',
    project_urls = {},
    license='GNU General Public License v3.0',
    packages=['brownian_motion_generator'],
    install_requires=['multiprocessing',
    'typing',
    'dataclasses',
    'sklearn',
    'numpy',
    'scipy',
    'statsmodels',
    'tqdm',
    'warnings'],
)