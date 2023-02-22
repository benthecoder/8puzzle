import os
import subprocess
from tqdm import tqdm
from datetime import datetime
import argparse
from pathlib import Path


def main(dir, out):

    algs = ["BFS", "IDS", "h1", "h2", "h3"]
    files = os.listdir(dir)
    files.sort()

    start_time = datetime.now()
    with tqdm(
        total=len(files * len(algs)),
    ) as t:
        for file in files:
            for alg in algs:
                t.set_description(f"Running {alg} on {file}")
                result = subprocess.run(
                    ["python", "main.py", "--fPath", f"{dir}/{file}", "--alg", alg],
                    capture_output=True,
                )
                if result.stderr:
                    raise subprocess.CalledProcessError(
                        returncode=result.returncode,
                        cmd=result.args,
                        stderr=result.stderr,
                    )
                with open(f"{out}/part2.txt", "a") as f:
                    f.write(f"--Fpath {file} --alg {alg} \n")
                    f.write(f"{result.stdout.decode('utf-8')} \n")

                t.update(1)

    end_time = datetime.now()

    time = end_time - start_time

    print(f"Total time taken:, {time.seconds} secs")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run 8puz performance analysis",
    )

    parser.add_argument("--in_dir", required=True, help="file input directory")
    parser.add_argument("--out_dir", required=True, help="file output directory")
    args = parser.parse_args()

    Path(args.out_dir).mkdir(parents=True, exist_ok=True)

    main(dir=args.in_dir, out=args.out_dir)
