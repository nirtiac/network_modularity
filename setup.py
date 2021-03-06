from setuptools import setup

setup(name="network_modularity",
      version=0.1,
      description="Returns common modularity scores given an edgelist in Ncol format",
      url="https://github.com/nirtiac/network_modularity",
      author="Caitrin  Armstrong",
      author_email="caitrin.armstrong@mail.mcgill.ca",
      licence="MIT",
      packages=["network_modularity"],
      entry_points = {
        "console_scripts": ['network_modularity = network_modularity.network_modularity:main']},
      install_requires=[
          'python-igraph',
          'argparse'
      ],
      zip_safe=False)
