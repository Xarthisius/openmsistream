# imports
import setuptools

# version tag
version = "1.5.2"

long_description = ""
with open("README.md", "r") as readme:
    for il, line in enumerate(readme.readlines(), start=1):
        if il >= 18:
            long_description += line

setupkwargs = dict(
    name="openmsistream",
    packages=setuptools.find_packages(include=["openmsistream*"]),
    include_package_data=True,
    version=version,
    description=(
        "Python applications for materials data streaming using Apache Kafka. "
        "Developed for Open MSI (NSF DMREF award #1921959)"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="OpenMSIStream",
    author_email="openmsistream@gmail.com",
    url="https://github.com/openmsi/openmsistream",
    download_url=f"https://github.com/openmsi/openmsistream/archive/refs/tags/v{version}.tar.gz",
    license="GNU GPLv3",
    entry_points={
        "console_scripts": [
            "UploadDataFile=openmsistream.data_file_io.entity.upload_data_file:main",
            "DataFileUploadDirectory=openmsistream.data_file_io.actor.data_file_upload_directory:main",
            "DataFileDownloadDirectory=openmsistream.data_file_io.actor.data_file_download_directory:main",
            "InstallService=openmsistream.services.install_service:main",
            "ManageService=openmsistream.services.manage_service:main",
            "ProvisionNode=openmsistream.utilities.provision_wrapper:main",
            "S3TransferStreamProcessor=openmsistream.s3_buckets.s3_transfer_stream_processor:main",
        ],
    },
    python_requires=">=3.7,<3.10",
    install_requires=[
        "atomicwrites>=1.4.1",
        "boto3>=1.26.84",
        "confluent-kafka>=2.0.2",
        "kafkacrypto>=0.9.10.0",
        "matplotlib",
        "methodtools",
        "msgpack",
        "watchdog>=3.0.0",
    ],
    extras_require={
        "test": [
            "beautifulsoup4",
            "black",
            "gitpython",
            "lxml",
            "marko[toc]",
            "pyflakes>=3.0.1",
            "pylint>=2.16.3",
            "tempenv>=2.0.0",
        ],
        "docs": [
            "sphinx>=6.1.3",
            "sphinx_rtd_theme>=1.2.0",
        ],
        "dev": [
            "twine",
        ],
    },
    keywords=[
        "data_streaming",
        "stream_processing",
        "apache_kafka",
        "materials",
        "data_science",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)

setupkwargs["extras_require"]["all"] = sum(setupkwargs["extras_require"].values(), [])

setuptools.setup(**setupkwargs)
