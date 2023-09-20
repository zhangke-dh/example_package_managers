from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='1.0.0',
    description='Your package description',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/your-package',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',  # 不指定版本
        'numpy>=1.21,<=1.22',  # 版本范围（包括边界）
        'Django==3.2.10',  # 指定版本
        'flask~=2.1',  # 兼容性版本
        'pandas>1.2.0,<1.4.0',  # 版本范围（不包括边界）
        'beautifulsoup4!=4.9.0',  # 排除特定版本
    ],
    extras_require={
        'dev': [
            'pytest',
            'coverage',
        ],
        'docs': [
            'Sphinx',
            'sphinx_rtd_theme',
        ],
    },
    dependency_links=[
        'https://custom.package.repo/simple/package_name/#egg=package_name-version',
    ],
    entry_points={
        'console_scripts': [
            'your_script = your_package.module:function',
        ],
    },
)



