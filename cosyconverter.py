import os
import argparse
from src.utils import (
    get_ext,
    convert,
)
from src.data import (
    supported_exts_from,
    supported_exts_to,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=str)
    parser.add_argument("outfile", type=str)
    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile

    if not os.path.isfile(infile):
        raise OSError(f"file {infile} not found")

    infile_head, infile_ext = get_ext(infile)
    outfile_head, outfile_ext = get_ext(outfile)

    if infile_ext not in supported_exts_from:
        raise IOError(f"unsupported input format {infile_ext}")
    if outfile_ext not in supported_exts_to:
        raise IOError(f"unsupported input format {outfile_ext}")

    if not outfile_head:
        outfile_head = infile_head

    convert(infile_head, infile_ext, outfile_head, outfile_ext)


if __name__ == "__main__":
    main()
