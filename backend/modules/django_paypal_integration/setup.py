from setuptools import setup, find_packages

setup(
    name='django_paypal_integration',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'paypalrestsdk',
        'Django>=3.2,<4.0',
    ],
    zip_safe=False,
)