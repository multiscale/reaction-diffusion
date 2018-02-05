from setuptools import setup
setup(
        name = 'reaction_diffusion',
        packages = ['reaction_diffusion'],
        version = 'develop',
        description = 'Some simple reaction-diffusion models using LittleMuscle',
        author = 'Lourens Veen',
        author_email = 'l.veen@esciencecenter.nl',
        url = 'https://github.com/multiscale/reaction-diffusion',
        license = 'Apache License 2.0',
        python_requires='>=3.5, <4',
        install_requires=[
                'littlemuscle',
                'overrides'
            ],
        keywords = ['multiscale', 'reaction', 'diffusion', 'Gray-Scott'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'],
        )
