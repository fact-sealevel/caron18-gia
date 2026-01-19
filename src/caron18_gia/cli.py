import click
import logging
from caron18_gia.caron18_GIA_preprocess import caron18_preprocess_GIA
from caron18_gia.caron18_GIA_postprocess import caron18_postprocess_GIA

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--pipeline-id",
    required=True,
    type=str,
    help="Unique identifier for the pipeline running this code",
)
@click.option(
    "--gia-stats-input-file",
    required=True,
    type=str,
    help="Path to the GIA statistics netCDF file",
)
@click.option("--nsamps", required=True, type=int, help="Number of samples to generate")
@click.option(
    "--rng-seed", required=True, type=int, help="Seed for the random number generator"
)
@click.option(
    "--baseyear",
    required=True,
    type=int,
    help="The year from which projections should be zeroed",
)
@click.option("--pyear-start", required=True, type=int, help="Projection start year")
@click.option("--pyear-end", required=True, type=int, help="Projection end year")
@click.option("--pyear-step", required=True, type=int, help="Projection year step")
@click.option(
    "--location-file",
    required=True,
    type=str,
    help="File that contains points for localization",
)
@click.option(
    "--chunksize",
    required=False,
    type=int,
    default=1000,
    help="Number of locations to process in each chunk",
)
@click.option(
    "--output-lslr-file",
    required=False,
    type=str,
    default="caron18_gia_lsrl_results.nc",
    help="Output file for local sea level rise results",
)
@click.option(
    "--output-quantiles-file",
    required=False,
    type=str,
    default="caron18_gia_quantiles.nc",
    help="Output file for quantiles results",
)

def main(
    pipeline_id: str,
    gia_stats_input_file: str,
    location_file: str,
    chunksize: int,
    nsamps: int,
    rng_seed: int,
    baseyear: int,
    pyear_start: int,
    pyear_end: int,
    pyear_step: int,
    output_lslr_file: str,
    output_quantiles_file: str,
) -> None:
    click.echo("Hello from caron18-gia!")

    logger.info("Starting preprocessing...")
    preprocess_dict = caron18_preprocess_GIA(
        pipeline_id, gia_rate_file=gia_stats_input_file
    )

    logger.info("Starting postprocessing...")
    caron18_postprocess_GIA(
        nsamps,
        rng_seed,
        baseyear,
        pyear_start,
        pyear_end,
        pyear_step,
        chunksize,
        preprocess_dict,
        pipeline_id,
        location_file,
        output_lslr_file,
        output_quantiles_file,
    )
    logger.info("Post-processing complete.")
