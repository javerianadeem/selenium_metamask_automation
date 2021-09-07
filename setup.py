from setuptools import setup


setup(name='selenium_metamask_automation',
      version='0.0.1',
      packages=['selenium_metamask_automation'],
      description="Python package, for automating metamask transaction on testnet",
      keywords="python metamask blockchain automate-metamask install-metamask-extention-selenium selenium-metamask",
      install_requires=["selenium>=3.141.0", "pywin32", "wheel"],
      python_requires='>=3.8',
      url='git@github.com:javerianadeem/selenium_metamask_automation',
      author='Javeria Nadeem',
      author_email='javerianadeem03@gmail.com',
      long_description='long_description',
      long_description_content_type='text/x-rst',

)