# GIA/caron18

This module uses GIA estimates and uncertainties estimated by Carol et al.  2018. 

Caron, L., Ivins, E. R., Larour, E., Adhikari, S., Nilsson, J., & Blewitt, G. (2018). GIA model statistics for GRACE hydrology, cryosphere, and ocean science. Geophysical Research Letters, 45(5), 2203-2212.

> [!CAUTION]
> This is a prototype. It is likely to change in breaking ways. It might delete all your data. Don't use it in production.

## Usage example

This application takes provided input data. Download the data at the following Zenodo record, placing it in a sub-directory of the project root named `./data/input`:

```shell
mkdir -p ./data/input
curl -sL https://zenodo.org/records/15975768/files/caron18_GIA_preprocess_data.tgz | tar -zx -C ./data/input

# Add a location file
echo "New_York	12	40.70	-74.01" > ./data/input/location.lst

# Make output dir
mkdir -p ./data/output
```

Now, run the application, for example in a Docker container as follows:
```shell
docker run --rm \
-v ./data/input:/mnt/caron_data_in:ro \
-v ./data/output:/mnt/caron_data_out \
ghcr.io/fact-sealevel/caron18-gia:latest \
--pipeline-id MY_PIPELINE \
--gia-stats-input-file /mnt/caron_data_in/GIA_stats.nc \
--rng-seed 1234 \
--baseyear 2000 \
--pyear-start 2000 \
--pyear-end 2100 \
--pyear-step 10 \
--location-file /mnt/caron_data_in/location.lst \
--chunksize 50 \
--nsamps 2000 \
--output-lslr-file /mnt/caron_data_out/gia_lslr.nc \
--output-quantiles-file /mnt/caron_data_out/gia_quantiles.nc
```

If the run is successful, the output projection will appear in `./data/output`.

## Features
Several options and configurations are available when running the application. See them by running:
```shell
docker run --rm caron18-gia --help
```

The features are: 
```shell
Usage: caron18-gia [OPTIONS]

Options:
  --pipeline-id TEXT            Unique identifier for the pipeline running
                                this code  [required]
  --gia-stats-input-file TEXT   Path to the GIA statistics netCDF file
                                [required]
  --nsamps INTEGER              Number of samples to generate  [required]
  --rng-seed INTEGER            Seed for the random number generator
                                [required]
  --baseyear INTEGER            The year from which projections should be
                                zeroed  [required]
  --pyear-start INTEGER         Projection start year  [required]
  --pyear-end INTEGER           Projection end year  [required]
  --pyear-step INTEGER          Projection year step  [required]
  --location-file TEXT          File that contains points for localization
                                [required]
  --chunksize INTEGER           Number of locations to process in each chunk
  --output-lslr-file TEXT       Output file for local sea level rise results
  --output-quantiles-file TEXT  Output file for quantiles results
  --help                        Show this message and exit.
```

## Build the container locally
You can build the container with Docker by cloning the repository locally and then running

```shell
docker build -t caron18-gia .
```

from the repository root.

## Support

Source code is available online at https://github.com/fact-sealevel/caron18-gia. This software is open source, available under the MIT license.

Please file issues in the issue tracker at https://github.com/fact-sealevel/caron18-gia/issues.
