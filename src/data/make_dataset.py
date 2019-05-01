# -*- coding: utf-8 -*-
import argparse
import logging
from dotenv import find_dotenv, load_dotenv


def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    logger.info(f'{input_filepath}, {output_filepath}')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path of input file")
    parser.add_argument("output_file", help="Path of output file")
    args = parser.parse_args()

    main(args.input_file, args.output_file)
