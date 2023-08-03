import os
import argparse
import shutil
from src.utils import get_ext


def chext(fpath: str, outext: str) -> None:
    assert  os.path.isfile(fpath), f"File not found: {fpath}"

    fhead, inext = get_ext(fpath)

    assert fhead, "Empty file header"

    trgpath = f"{fhead}{outext}"

    shutil.copyfile(fpath, trgpath)
    os.remove(fpath)

    return None


def chect_to(outext: str) -> callable:
    def chext_for(fpath: str):
        return chext(fpath, outext)
    return chext_for


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infiles", type=str, nargs="+", help="Files, extension of which should be changed")
    parser.add_argument("outext", type=str, help="Target extension")
    args = parser.parse_args()

    infiles = args.infiles
    outext = args.outext

    cwd = os.getcwd()
    trgpaths = [os.path.join(cwd, infile) for infile in infiles]

    chext_f = chect_to(outext)
    _ = list(map(chext_f, trgpaths))


if __name__ == "__main__":
    main()
