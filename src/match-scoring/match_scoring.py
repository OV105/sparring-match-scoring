import argparse
import logging

def main(args_in):
    """process command line arguments.

    Args:
        args_in (list[str]): list of command line arguments
    """
    parser = argparse.ArgumentParser(description="Parse arguments")
    parser.add_argument("-s", "--score", help="Score match")
    args = parser.parse_args(args_in)
    logging.basicConfig(
        filename="match-scoring.log",
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )

if __name__ == "__main__":
    main(sys.argv[:1])
