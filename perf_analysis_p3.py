import os
from tqdm import tqdm
from main import run
from pprint import pprint
from datetime import datetime
import argparse
from pathlib import Path
from multiprocessing import Pool
import re


def main(dir, out):

    algs = ["BFS", "IDS", "h1", "h2", "h3"]

    dirs = os.listdir(dir)
    # sort by digits in string
    dirs.sort(key=lambda f: int(re.sub(r"\D", "", f)))

    start_time = datetime.now()
    with tqdm(
        total=len(dirs),
    ) as t:
        for d in dirs:
            avgs = {}

            t.set_description(f"Running for {d}")
            files = os.listdir(f"{dir}/{d}")
            files.sort()

            total_files_cnt = len(files)

            for alg in algs:
                t.set_description(f"Running {alg}")
                total_time = 0
                total_nodes = 0

                with Pool(processes=5) as pool:
                    results = pool.starmap(
                        run, [(f"{dir}/{d}/{file}", alg, 1) for file in files]
                    )

                for result in results:
                    total_time += result["time"]
                    total_nodes += result["nodes"]

                # calculate averages
                avg_time = total_time / total_files_cnt
                avg_nodes = total_nodes / total_files_cnt

                # format seconds to min:sec:microsec
                avg_time = datetime.fromtimestamp(avg_time).strftime("%M:%S:%f")

                avgs[alg] = (avg_nodes, avg_time)

            with open(f"{out}/part3.txt", "a") as f:
                f.write(f"Level: {d} \n")
                pprint(avgs, stream=f)

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
