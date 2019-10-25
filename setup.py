from setuptools import setup
setup(
    name='vader_fr',
    version=0.1,
    packages=['vader_fr'],
    package_dir={'vader_fr': 'vader_fr'},
    include_package_data=True,
    package_data={
        "vader_fr": ["*.txt", "*.xml"]
    },
)