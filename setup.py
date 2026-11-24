from setuptools import setup

setup(
    name="lexibank_martinvalladolidiberian",
    py_modules=["lexibank_martinvalladolidiberian"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["martinvalladolidiberian=lexibank_martinvalladolidiberian:Dataset"]},
    install_requires=["pylexibank>=3.0"],
)
