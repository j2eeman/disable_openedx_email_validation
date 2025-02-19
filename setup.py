from setuptools import setup, find_packages

setup(
    name='disable-openedx-email-validation',
    version='0.1.0',
    description='Disable email validation in Open edX',
    packages=find_packages(),
    include_package_data=True,  # This is crucial!
    package_data={
        'disable_openedx_email_validation': ['hooks.py'],
    },
    entry_points={
        'tutor.plugins': [
            'disable_openedx_email_validation = disable_openedx_email_validation.hooks',
        ],
    },
)