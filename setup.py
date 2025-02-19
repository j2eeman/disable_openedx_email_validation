from setuptools import setup, find_packages

setup(
    name='disable-openedx-email-validation',
    version='0.1.0',
    description='Disable email validation in Open edX',
    packages=find_packages(include=['disable_openedx_email_validation*']),
    include_package_data=True,  # This is crucial!

    entry_points={
        'tutor.plugins': [
            'disable-openedx-email-validation = disable_openedx_email_validation.hooks',
        ],
    },
)