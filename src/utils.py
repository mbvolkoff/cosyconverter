import os
import pandas as pd


def get_ext(fname: str):
    filehead, fileext = os.path.splitext(fname)
    if not fileext:
        filehead, fileext = fileext, filehead
    return filehead, fileext


def convert_excel(infile_head: str, infile_ext: str, outfile_head: str, outfile_ext: str):
    df = pd.read_excel(f"{infile_head}{infile_ext}")
    outfile = f"{outfile_head}{outfile_ext}"
    if outfile_ext == ".csv":
        df.to_csv(outfile, index=False)
        print(f"converted to {outfile}")
    if outfile_ext == ".tsv":
        df.to_csv(outfile, sep="\t", index=False)
        print(f"converted to {outfile}")


def convert(infile_head: str, infile_ext: str, outfile_head: str, outfile_ext: str):
    if (infile_ext == ".xlsx") or (infile_ext == ".xls"):
        convert_excel(infile_head, infile_ext, outfile_head, outfile_ext)
    pass
