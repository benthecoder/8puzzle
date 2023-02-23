import os
from tqdm import tqdm
from main import run
from pprint import pprint
from datetime import datetime
import argparse
from pathlib import Path
from multiprocessing import Pool
import re
import concurrent.futures


def main(dir, out):
    def run_helper(args):
        return run(*args)

    algs = ["BFS", "IDS", "h1", "h2", "h3"]

    dirs = os.listdir(dir)
    # sort by digits in string
    dirs.sort(key=lambda f: int(re.sub(r"\D", "", f)))

    # create dictionary to store results

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

                # # This doesn't work because signal only works on main thread
                # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                #    results = list(
                #        tqdm(
                #            executor.map(
                #                run_helper,
                #                ((f"{dir}/{d}/{file}", alg, 1) for file in files),
                #            ),
                #            total=total_files_cnt,
                #        )
                #    )

                #    for result in results:
                #        total_time += result["time"]
                #        total_nodes += result["nodes"]

                ## This is slower than running in serial (time out is happening for BFS)
                # with Pool() as pool:
                #    results = list(
                #        tqdm(
                #            pool.starmap(
                #                run, [(f"{dir}/{d}/{file}", alg, 1) for file in files]
                #            ),
                #            total=total_files_cnt,
                #        )
                #    )

                # for result in results:
                #    total_time += result["time"]
                #    total_nodes += result["nodes"]

                for file in files:
                    t.set_description(f"Running {alg} on {file}")
                    result = run(f"{dir}/{d}/{file}", alg, 1)
                    total_time += result["time"]
                    total_nodes += result["nodes"]

                    t.update(1)

                # calculate averages
                avg_time = total_time / total_files_cnt
                avg_nodes = total_nodes / total_files_cnt

                # format seconds to min:sec:microsec
                avg_time = datetime.fromtimestamp(avg_time).strftime("%M:%S:%f")

                avgs[alg] = (avg_nodes, avg_time)

            with open(f"{out}/part3.txt", "a") as f:
                f.write(f"Level: {d} \n")
                pprint(avgs, stream=f)

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
