import setuptools 

setuptools.setup(
    name='TN_code',
    version='0.91',
    description='Code gebruikt bij de opleiding TN van de Haagse Hogeschool',
    url='https://hhs-tn.github.io',
    license='MIT',
    author='Derek Land',
    author_email='d.d.land@hhs.nl',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 
                      'matplotlib',
                      'pandas',
                      'sympy',
                      ],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Natural Language :: Dutch',
                 'Programming Language :: Python :: 3',
                 'Topic :: Utilities',
        ],
)

