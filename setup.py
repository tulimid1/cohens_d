from distutils.core import setup
setup(
  name = 'cohens_d',         # How you named your package folder (MyLib)
  packages = ['cohens_d'],   # Chose the same as "name"
  version = '0.1.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Calculate cohen''s d for 1 sample, 2 independent samples, or 2 paired samples',   # Give a short description about your library
  author = 'Duncan Tulimieri',                   # Type in your name
  author_email = 'tulimid@udel.edu',      # Type in your E-Mail
  url = 'https://tulimid1.github.io/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/tulimid1/cohens_d/archive/refs/tags/v_01.3.tar.gz',    # I explain this later on
  keywords = ['cohens d'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)